# 🔒 Text File Redactor

This Python script scans a given text file for sensitive information and redacts it. It detects and replaces data such as:

- 📧 Email addresses
- 📞 Phone numbers
- 💳 Credit card numbers
- 🧾 Social Security Numbers (SSNs)

Redacted content is saved in a new file along with a redaction log for reference.

---

## 🚀 Features

- Automatically finds and redacts sensitive information
- Creates a uniquely named redacted output file and log file per input file
- Allows multiple files to be redacted in one session
- Handles file-not-found and read errors gracefully

---

## 🛠️ Requirements

- Python 3.x

No additional libraries required — uses only Python's built-in modules.

---

## 🧪 Usage

1. Clone this repo or copy the script to your local machine.
2. Run the script:

```bash
python main.py
