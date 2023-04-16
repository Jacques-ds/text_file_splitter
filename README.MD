# Text File Splitter

This script takes a text file as input and splits it into multiple parts, with a maximum number of characters allowed in each part. The output files are saved with a prefix and an index (e.g., "part_0.txt", "part_1.txt", etc.).

## Requirements

- Python 3.6 or higher
- `click` library

To install the required `click` library, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Save the script as a `.py` file (e.g., `splitter.py`).
2. Run the script from the command line using the following syntax:

```bash
python splitter.py input_file.txt --max_chars 12000
```

Replace `input_file.txt` with the name of your input text file, and `12000` with the desired maximum number of characters per part (optional; default is 12000).

## Parameters

- `input_file` (positional argument): The path of the input text file.
- `--max_chars` (optional): The maximum number of characters allowed in each part. Default value is 12000.

## Example

```bash
python splitter.py example.txt --max_chars 5000
```

This command will split the `example.txt` file into parts, each containing a maximum of 5000 characters, and save the parts as separate files with the "part_" prefix.
