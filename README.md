# Markdown to PDF Converter

A robust Python utility that converts Markdown files to professionally styled PDF documents with customizable CSS styling.

## Features

- Convert Markdown files to PDF with high-quality formatting
- Custom CSS styling support
- Cross-platform compatibility (Windows, Linux, macOS)
- Support for tables, code blocks, and other Markdown extensions
- Configurable page settings and margins
- Proper handling of Unicode characters
- Newline preservation in text conversion

## Prerequisites

- Python 3.6 or higher
- wkhtmltopdf (required for PDF conversion)

### Installing wkhtmltopdf

Download and install wkhtmltopdf from the official website:
- [wkhtmltopdf Downloads](https://wkhtmltopdf.org/downloads.html)

#### Default Installation Paths:
- Windows: `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`
- Linux: `/usr/bin/wkhtmltopdf`
- macOS: `/usr/local/bin/wkhtmltopdf`

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd markdown-to-pdf
```

2. Install required Python packages:
```bash
pip install markdown pdfkit
```

## Usage

### Basic Usage

Convert a Markdown file to PDF with default styling:
```bash
python converter.py input.md
```

### Advanced Options

```bash
python converter.py input.md -o output.pdf -c custom_style.css --wkhtmltopdf /path/to/wkhtmltopdf
```

### Command Line Arguments

- `input_file`: Path to input Markdown file (required)
- `-o, --output`: Output PDF file path (optional)
- `-c, --css`: Custom CSS file path (optional)
- `--wkhtmltopdf`: Custom path to wkhtmltopdf executable (optional)

## Supported Markdown Features

- Headers (all levels)
- Paragraphs with proper spacing
- Tables with responsive design
- Code blocks with syntax highlighting
- Lists (ordered and unordered)
- Links
- Images
- Blockquotes
- Line breaks preservation
- Tables of Contents

## CSS Customization

The converter supports custom CSS styling. Create a CSS file with your preferred styles and pass it using the `-c` option.

Example custom CSS structure:
```css
/* Typography */
body {
    font-family: 'Your-Font', sans-serif;
    line-height: 1.6;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
}

/* Add more custom styles as needed */
```

## Error Handling

The converter includes robust error handling:
- Validates wkhtmltopdf installation
- Checks file existence and permissions
- Handles conversion errors gracefully
- Removes incomplete output files on failure

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Python-Markdown](https://python-markdown.github.io/) for Markdown processing
- [pdfkit](https://github.com/JazzCore/python-pdfkit) for PDF conversion
- [wkhtmltopdf](https://wkhtmltopdf.org/) for HTML to PDF conversion

## Troubleshooting

### Common Issues

1. **wkhtmltopdf not found**
   - Ensure wkhtmltopdf is properly installed
   - Verify the installation path
   - Use the `--wkhtmltopdf` argument to specify custom path

2. **Unicode errors**
   - Ensure your Markdown files are UTF-8 encoded
   - Check for proper character encoding in your CSS file

3. **Styling issues**
   - Verify CSS file path and syntax
   - Check for CSS conflicts
   - Ensure proper class names and selectors

For more issues and solutions, please check the [Issues](issues) section.
