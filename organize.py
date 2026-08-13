import os
import shutil
import argparse

# 1. Define the mapping of target folders to file extensions
EXTENSION_MAP = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    "Code": ['.py', '.js', '.html', '.css', '.json'],
    "Audio": ['.mp3', '.wav'],
    "Video": ['.mp4', '.mkv', '.avi'],
    "Archives": ['.zip', '.tar', '.gz', '.rar']
}

def organize_directory(base_dir, dry_run=False):
    print(f"Scanning directory: {base_dir}")
    if dry_run:
        print("--- DRY RUN MODE: No files will actually be moved ---\n")
        
    for item in os.listdir(base_dir):
        # Skip the script itself, hidden files, and any directories
        if item == 'organize.py' or os.path.isdir(os.path.join(base_dir, item)) or item.startswith('.'):
            continue
            
        _, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower()

        target_folder = "Others" 
        for folder, extensions in EXTENSION_MAP.items():
            if file_extension in extensions:
                target_folder = folder
                break

        target_path = os.path.join(base_dir, target_folder)
        source_path = os.path.join(base_dir, item)
        destination_path = os.path.join(target_path, item)
        
        # If dry run is active, just print what WOULD happen
        if dry_run:
            print(f"[DRY RUN] Would move: {item} -> {target_folder}/")
        else:
            # Actually move the files
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {item} -> {target_folder}/")
            except Exception as e:
                print(f"Error moving {item}: {e}")

if __name__ == "__main__":
    # 2. Set up the Command Line Interface
    parser = argparse.ArgumentParser(description="Organize files in a directory by extension.")
    
    # 3. Add arguments for custom directory and dry-run
    parser.add_argument("-d", "--directory", type=str, default=os.getcwd(), 
                        help="The target directory to organize. Defaults to current directory.")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Simulate the organization without actually moving any files.")
    
    args = parser.parse_args()
    
    # 4. Resolve the path and run the script
    target_dir = os.path.abspath(args.directory)
    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory.")
    else:
        organize_directory(target_dir, args.dry_run)