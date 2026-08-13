import os
import shutil

# 1. Define the mapping of target folders to file extensions
EXTENSION_MAP = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    "Code": ['.py', '.js', '.html', '.css', '.json'],
    "Audio": ['.mp3', '.wav'],
    "Video": ['.mp4', '.mkv', '.avi'],
    "Archives": ['.zip', '.tar', '.gz', '.rar']
}

def organize_directory():
    # 2. Get the current directory where the script is running
    base_dir = os.getcwd()
    print(f"Scanning directory: {base_dir}")
    
    # 3. Loop through all items in the directory
    for item in os.listdir(base_dir):
        # Skip the script itself and any directories
        if item == 'organize.py' or os.path.isdir(item):
            continue
            
        print(f"Found file: {item}")

if __name__ == "__main__":
    organize_directory()