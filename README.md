#  Python File Organizer

A lightweight, zero-dependency Python script that automatically organizes a messy directory by sorting files into categorized folders based on their file extensions.

---

## 🚀 How It Works

Place the `organize.py` script inside any cluttered folder, such as your **Downloads** folder, and run it.

The script will:

1. Scan the directory for files.
2. Identify each file based on its extension.
3. Create the appropriate category folder.
4. Move the file into its corresponding folder.

### 📁 Categories Supported

| Category | File Extensions |
|---|---|
| 🖼️ `Images/` | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp` |
| 📄 `Documents/` | `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.xls`, `.ppt`, `.pptx` |
| 💻 `Code/` | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.php` |
| 🎵 `Audio/` | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg` |
| 🎬 `Video/` | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv` |
| 📦 `Archives/` | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.tar.gz` |
| 📁 `Others/` | Any unrecognized file type |

---

## ✨ Features

- ⚡ **Fast and lightweight**
- 📂 **Automatically creates category folders**
- 🧹 **Cleans up cluttered directories**
- 🐍 **Built entirely with Python**
- 📦 **Zero external dependencies**
- 🔧 **Easy to customize**
- 💻 **Cross-platform**
- 🗂️ **Supports multiple file categories**
- ♻️ **Can be reused on any directory**

---

## 🛠️ Built With

This project uses only Python's built-in libraries.

- **Python 3**
- `os`
- `shutil`

No external packages or dependencies are required.

---

## 📌 Requirements

Before using the project, make sure you have:

- Python **3.x** installed
- Access to the directory you want to organize
- Permission to move files within that directory

You can check your Python installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 💻 Installation & Usage

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/briankimani640/python-file-organizer.git
```


Navigate into the project directory:

```bash
cd python-file-organizer
```

### 2. Move `organize.py`

Move or copy the `organize.py` file into the directory you want to organize.

For example:

```text
Downloads/
├── organize.py
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
├── project.py
├── archive.zip
└── notes.txt
```

### 3. Run the Script

Open your terminal inside the directory and run:

```bash
python organize.py
```

If your system uses `python3`:

```bash
python3 organize.py
```

---

## 📂 Example

### Before Running

Your directory may look like this:

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
├── project.py
├── archive.zip
├── notes.txt
└── presentation.pptx
```

### After Running

The script automatically organizes the files:

```text
Downloads/
├── organize.py
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   ├── resume.pdf
│   ├── notes.txt
│   └── presentation.pptx
│
├── Audio/
│   └── song.mp3
│
├── Video/
│   └── movie.mp4
│
├── Code/
│   └── project.py
│
└── Archives/
    └── archive.zip
```

---

## 🔧 Customization

You can customize the file categories and supported extensions inside `organize.py`.

For example:

```python
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".java"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"]
}
```

You can add or remove extensions according to your needs.

---

## 🧠 How It Works

The organizer follows this process:

```text
Start
  │
  ▼
Scan Directory
  │
  ▼
Find Files
  │
  ▼
Read File Extension
  │
  ▼
Identify Category
  │
  ├── Images ───────► Images/
  │
  ├── Documents ────► Documents/
  │
  ├── Code ─────────► Code/
  │
  ├── Audio ────────► Audio/
  │
  ├── Video ────────► Video/
  │
  ├── Archives ─────► Archives/
  │
  └── Unknown ──────► Others/
  │
  ▼
Move File
  │
  ▼
Done ✅
```

---

## 📜 Project Structure

```text
python-file-organizer/
│
├── organize.py
├── README.md
└── LICENSE
```

---

## 🐍 Python Concepts Used

This project demonstrates several fundamental Python concepts:

- Variables
- Lists
- Dictionaries
- Conditional statements
- Loops
- Functions
- File handling
- Exception handling
- File extensions
- Directory manipulation
- Built-in Python modules

---

## 📚 Learning Purpose

This project is designed as a beginner-friendly Python automation project.

It demonstrates how Python can interact with the operating system to automate repetitive file-management tasks.

By working on this project, you can learn how to:

- Work with files and directories
- Use Python's built-in modules
- Detect file extensions
- Create directories programmatically
- Move files automatically
- Build simple automation tools

---

## ⚠️ Important Notes

Before running the script on important files:

- Make sure you have backups of important data.
- Test the script on a temporary directory first.
- Do not run it on system directories.
- Make sure you understand which files will be moved.
- Avoid interrupting the script while it is moving files.

---

## 🔒 Safety

The script is designed to organize files based on their extensions.

It does **not**:

- Delete files
- Upload files
- Send files anywhere
- Modify file contents
- Install external software

It simply creates folders and moves files into the appropriate folders.

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Commit your changes.
6. Push your branch to GitHub.
7. Open a Pull Request.

Example:

```bash
git checkout -b feature/new-file-category
```

After making your changes:

```bash
git add .
git commit -m "feat: add new file category"
git push origin feature/new-file-category
```

Then create a Pull Request on GitHub.

---

## 🐛 Reporting Issues

If you find a bug or have a feature request, please open an issue in the GitHub repository.

When reporting a bug, include:

- Operating system
- Python version
- Description of the problem
- Expected behavior
- Actual behavior
- Relevant error message

---

## 💡 Future Improvements

Possible future improvements include:

- [ ] Add a graphical user interface
- [ ] Add a command-line interface
- [ ] Add configurable categories
- [ ] Add duplicate-file detection
- [ ] Add logging
- [ ] Add undo functionality
- [ ] Add recursive directory scanning
- [ ] Add custom folder selection
- [ ] Add a dry-run mode
- [ ] Add file date-based organization
- [ ] Add file-size-based organization
- [ ] Add configuration through a JSON file

---

## 📄 License

This project is open source and available for personal and educational use.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Brian Kimani**

GitHub: `https://github.com/briankimani640`


---

## ⭐ Support

If you find this project useful, consider supporting the project by:

- ⭐ Starring the repository
- 🍴 Forking the repository
- 🐛 Reporting bugs
- 💡 Suggesting improvements
- 🤝 Contributing to the project

---


## 📋 Quick Start

For a quick setup:

```bash
# Clone the repository
git clone https://github.com/briankimani640/python-file-organizer.git

# Enter the project directory
cd python-file-organizer

# Run the organizer
python organize.py
```

That's it! 🎉

Your files will automatically be sorted into categorized folders.

---

⭐ **If you find this project useful, consider giving the repository a star!**


