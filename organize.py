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
        # Skip the script itself, hidden files, and any directories
        if item == 'organize.py' or os.path.isdir(item) or item.startswith('.'):
            continue
            
        # 4. Extract the file extension
        _, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower()

        # 5. Determine the target folder (default to 'Others' if unknown)
        target_folder = "Others" 
        for folder, extensions in EXTENSION_MAP.items():
            if file_extension in extensions:
                target_folder = folder
                break

        # 6. Create the folder if it doesn't exist
        target_path = os.path.join(base_dir, target_folder)
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # 7. Move the file
        source_path = os.path.join(base_dir, item)
        destination_path = os.path.join(target_path, item)
        
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {item} -> {target_folder}/")
        except Exception as e:
            print(f"Error moving {item}: {e}")

if __name__ == "__main__":
    organize_directory()