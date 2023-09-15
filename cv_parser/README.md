
# PDF Text Highlighter and Redactor

This is a Python application that allows you to highlight or redact text in PDF files. You can specify a search string and choose to either highlight or redact the matching text. The application supports processing individual PDF files or entire folders of PDF files.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Command Line Arguments](#command-line-arguments)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Highlight or redact text in PDF files.
- Process individual PDF files or entire folders.
- Optional recursive processing for folders.
- Specify search strings to find and act upon.
- Choose between highlighting or redacting matching text.
- Extract and display basic file information.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- [PyMuPDF (MuPDF)](https://pypi.org/project/PyMuPDF/): A Python binding for MuPDF, used for working with PDF files.
- [Pillow (PIL Fork)](https://pypi.org/project/Pillow/): A Python Imaging Library, used for image processing.

You can install the required Python packages using pip:

```bash
pip install PyMuPDF Pillow
