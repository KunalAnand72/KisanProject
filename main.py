import re
import os

def redact_sensitive_info(file_path):
    patterns = {
        'Email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'Phone': r'(?:(?:\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?)\d{3}[\s-]?\d{4}',
        'CreditCard': r'\b(?:\d[ -]*?){13,16}\b',
        'SSN': r'\b\d{3}-\d{2}-\d{4}\b'
    }

    redaction_log = {key: 0 for key in patterns}

    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ File not found at: {file_path}")
        return
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    original_content = content

    for label, pattern in patterns.items():
        matches = re.findall(pattern, content)
        redaction_log[label] += len(matches)
        content = re.sub(pattern, '[REDACTED]', content)

    file_dir = os.path.dirname(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    if content == original_content:
        print("ℹ️ No sensitive data found to redact.")
    else:
        output_path = os.path.join(file_dir, f'redacted_output_{base_name}.txt')
        with open(output_path, 'w') as outfile:
            outfile.write(content)
        print(f"✅ Redacted file saved to: {output_path}")

        log_path = os.path.join(file_dir, f'redaction_log_{base_name}.txt')
        with open(log_path, 'w') as logfile:
            for key, count in redaction_log.items():
                logfile.write(f'{key} redactions: {count}\n')
        print(f"📄 Log file saved to: {log_path}")

def main():
    while True:
        file_path = input("\nEnter the full path to your text file: ").strip()
        redact_sensitive_info(file_path)

        choice = input("\nDo you want to continue redaction for another text file? Enter Y for Yes and N for No [Y/N]: ").strip().upper()
        while choice not in ['Y', 'N']:
            choice = input("Please enter a valid choice [Y/N]: ").strip().upper()

        if choice == 'N':
            print("👋 Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
