# Translation Program using OpenAI

This Python program demonstrates how to use OpenAI's GPT-3 to translate text from one language to another.

## Usage

To use this program, you need to set up your OpenAI API key. Replace `"your-api-key"` in the code with your actual API key.

```python
import openai

openai.api_key = "your-api-key"

def translate_text(text, target_language):
    # ... (rest of your code)

text = "Zdravo svete"
target_language = "english"
translation = translate_text(text, target_language)
print(translation)

Configuration

    Python 3.7 or higher
    OpenAI API key
