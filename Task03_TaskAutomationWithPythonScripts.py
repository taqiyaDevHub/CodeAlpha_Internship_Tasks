# CODEALPHA INTERNSHIP TASK#03:  "TASK AUTOMATION WITH PYTHON SCRIPTS"

import re

def read_file(input_filename):
    """Read and return content of the file."""
    try:
        with open(input_filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
        return None

def extract_emails(text):
    """Extract unique email addresses from the text of a given file."""
    
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    emails_found = re.findall(email_pattern, text)
    unique_emails = sorted(set(emails_found))
    return unique_emails

def save_emails(output_filename, emails, input_filename):
    """Save extracted emails into an output file."""
    
    with open(output_filename, "w") as file:
        file.write("==== Extracted Email Addresses ====\n\n")
        
        if emails:
            for email in emails:
                file.write(email + "\n")
            file.write("\nTotal Emails Found: " + str(len(emails)))
            print(f"Emails saved successfully in {output_filename} file.")
        else:
            file.write(f"No emails found in {input_filename} file.\n")
            print(f"Output saved in {output_filename} file.") 

def main():
    # Specify the input file name
    input_file = "sample_text.txt"

    # Specify the output file name (the program will automatically create this file)
    output_file = "extracted_emails.txt"

    content = read_file(input_file)
    if content is None:
        return
    if not content.strip():
        print(f"The {input_file} file is empty.")
        return

    emails = extract_emails(content)
    if emails:
        print(f"Emails Found: {len(emails)}")
    else:
        print(f"No emails found in {input_file} file.")

    save_emails(output_file, emails, input_file)

# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    main()
