import markdown
import pdfkit
import argparse
import os
import platform
from pathlib import Path

def get_wkhtmltopdf_path():
    """Get the path to wkhtmltopdf based on the operating system"""
    system = platform.system().lower()
    if system == 'windows':
        # Стандартные пути установки на Windows
        possible_paths = [
            r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None
    elif system == 'linux':
        return '/usr/bin/wkhtmltopdf'
    elif system == 'darwin':  # macOS
        return '/usr/local/bin/wkhtmltopdf'
    return None


def convert_md_to_pdf(input_file, output_file=None, css_file=None, css_string=None, wkhtmltopdf_path=None):
    try:
        # Configure wkhtmltopdf
        if wkhtmltopdf_path is None:
            wkhtmltopdf_path = get_wkhtmltopdf_path()

        if wkhtmltopdf_path is None:
            raise Exception(
                "wkhtmltopdf not found. Please install it from https://wkhtmltopdf.org/downloads.html "
                "or specify path using --wkhtmltopdf argument"
            )

        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Read markdown content
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Preserve newlines by adding two spaces at the end of lines
        md_content = '\n'.join(line + '  ' if line.strip() else line
                                   for line in md_content.splitlines())
        # Convert markdown to HTML with specific extensions
        html_content = markdown.markdown(
            md_content,
            extensions=[
                'tables',
                'fenced_code',
                'codehilite',
                'toc',
                'attr_list',
                'md_in_html',
                'nl2br'
            ]
        )

        # Wrap tables with div for better styling
        html_content = html_content.replace('<table>', '<div class="table-wrapper"><table>')
        html_content = html_content.replace('</table>', '</table></div>')

        # Prepare CSS
        if css_file:
            with open(css_file, 'r', encoding='utf-8') as f:
                css = f.read()

        # Create complete HTML document with specific meta tags
        html_doc = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                {css}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # Set output filename if not provided
        if not output_file:
            output_file = Path(input_file).stem + '.pdf'

        # Enhanced PDF options
        pdfkit_options = {
            'encoding': 'UTF-8',

            'enable-local-file-access': None,
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'print-media-type': None,
            'no-outline': None,
            'page-size': 'A4',
            'dpi': 300,
            'image-quality': 100,
            'enable-smart-shrinking': None,
            'javascript-delay': 1000
        }

        # Convert to PDF
        pdfkit.from_string(html_doc, output_file, options=pdfkit_options, configuration=config)
        print(f"Successfully converted {input_file} to {output_file}")

    except Exception as e:
        print(f"Error converting file: {str(e)}")
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
                print(f"Removed incomplete output file: {output_file}")
            except:
                pass


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF with CSS styling')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PDF file')
    parser.add_argument('-c', '--css', help='Custom CSS file')
    parser.add_argument('--wkhtmltopdf', help='Path to wkhtmltopdf executable')
    args = parser.parse_args()

    convert_md_to_pdf(args.input_file, args.output, args.css, wkhtmltopdf_path=args.wkhtmltopdf)


if __name__ == '__main__':
    main()
