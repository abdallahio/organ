import os
from textract import process

folder_path = "/Users/ramal/Desktop/organ/dborg"

# Create folders if they don't exist
categories = ["Finance", "HR", "Sales","Other"]
for category in categories:
    category_folder = os.path.join(folder_path, category)
    if not os.path.exists(category_folder):
        os.mkdir(category_folder)

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf") or filename.endswith(".docx"):
        file_path = os.path.join(folder_path, filename)
        text_bytes = process(file_path)

        # Perform content analysis here to determine the category
        # For simplicity, let's assume we're looking for specific keywords
     # Decode the bytes to a string using UTF-8 encoding
        text = text_bytes.decode('utf-8')
        
        if "finance" in text.lower():
            category = "Finance"
        elif "human resources" in text.lower() or "hr" in text.lower():
            category = "HR"
        elif "sales" in text.lower():
            category = "Sales"
        else:
            category = "Other"

        # Move the file to the appropriate category folder
        destination_folder = os.path.join(folder_path, category)
        new_file_path = os.path.join(destination_folder, filename)

        if not os.path.exists(new_file_path):
            os.rename(file_path, new_file_path)
        else:
            # Handle file name collisions or duplicates
            # You might want to add a timestamp or unique identifier
            # to the file name in such cases.
            pass

        print(f"Moved {filename} to {category} folder.")
