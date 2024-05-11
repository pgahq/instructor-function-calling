`main.py` shows how to use Instructor to describe functions that LLMs can call. Includes examples for OpenAI and Groq.

## Prerequisites

Ensure you have Python 3.8 or higher installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Setting Up a Virtual Environment

To avoid conflicts with other Python projects, it's recommended to use a virtual environment. Follow these steps to set it up:

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Create a virtual environment named `venv` by running:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows, run:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```bash
     source venv/bin/activate
     ```

## Installing Dependencies

With the virtual environment activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

## API Keys

You will need to get API keys for OpenAI and Groq. Set as environment variables `OPENAI_API_KEY` and `GROQ_API_KEY` respectively (or put them directly into main.py).

## Running the Script

```bash
python main.py
```

## Debugging

Select the Python interpreter in Cursor or VS Code:

1. Open the Command Palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
2. Type `Python: Select Interpreter` and press Enter.
3. A list of available interpreters will be displayed. Select the interpreter you wish to use from the list (probably the one in your project's virtual environment).

This will set the selected interpreter / environment as the default for your current workspace.


