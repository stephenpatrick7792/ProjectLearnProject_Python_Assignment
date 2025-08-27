# 📂 File Read & Write with Error Handling

def modify_content(text):
    """
    Modify file content (example: make it uppercase).
    You can change this logic as needed.
    """
    return text.upper()

try:
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    # Open file safely
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_content(content)

    # Save into a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ File processed successfully! Modified version saved as {new_filename}")

except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
