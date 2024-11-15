# Text File Character Analyzer

A Python script that analyzes text files to count words and generate character frequency reports.

## Description

This script reads a text file and generates a detailed report containing:
- Total word count
- Frequency count of each alphabetic character (case-insensitive)
- Characters sorted by frequency in descending order

## Features

- Case-insensitive character counting
- Focuses on alphabetic characters only
- Formatted output report
- Sorts characters by frequency
- Handles large text files efficiently

## Installation

No external dependencies required. Uses Python's built-in libraries.

### Requirements
- Python 3.x

## Usage

1. Place your text file in the `books` directory (or modify the file path in the script)

2. Run the script:
```python
python text_analyzer.py
```

3. By default, the script analyzes `books/frankenstein.txt`. To analyze a different file, modify the file path in the script:
```python
print_report("path/to/your/file.txt")
```

## Example Output

```
--- Begin report of books/frankenstein.txt ---
12431 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
--- End report ---
```

## Functions

### count_characters(text)
Counts the frequency of alphabetic characters in the given text.

Parameters:
- `text` (str): The input text to analyze

Returns:
- dict: A dictionary with characters as keys and their frequencies as values

### print_report(file_path)
Generates and prints a complete analysis report for the specified file.

Parameters:
- `file_path` (str): Path to the text file to analyze

## Error Handling

Add try-except blocks if you need to handle:
- File not found errors
- Permission issues
- Memory constraints with large files

## Contributing

Feel free to submit issues and enhancement requests.

## License

[Add your chosen license here]
