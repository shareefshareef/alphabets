# ASCII Art Generator

This project is an ASCII art generator implemented in Python. It allows you to convert text into various ASCII art patterns, representing each letter of the alphabet and some numbers.

## Installation

1. Clone the repository:
git clone <repository-url>
cd <repository-folder>


2. Install dependencies (if any).

## Usage

### Running the ASCII Art Generator

To generate ASCII art for a specific text:

1. Open the `main.py` file.
2. Modify the `text` variable to the desired text you want to convert to ASCII art.
3. Run the script:
python main.py


### Customizing Patterns

You can customize the patterns used in the ASCII art:

- Open `alphabets.py` to view all available patterns for letters and numbers.
- Customize the patterns or add new ones by modifying the methods in the `Alphas` class.

### Example

For example, if you want to generate ASCII art for the text "Angels":

```python
text = "Angels"
printPattern(text)

This will print out the ASCII art representation of each letter in "Angels".

