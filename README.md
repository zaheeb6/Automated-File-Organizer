# Automated File Organizer

A Python script that automatically organizes files in a specified directory based on their file types.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Features
- Monitors a designated folder (e.g., Downloads) for new files.
- Automatically categorizes files into subfolders based on their extensions (e.g., PDFs, images).
- Runs silently in the background, organizing files as they are added.
- Improves file management and reduces clutter in frequently used directories.

## Technologies
- **Python 3.x**
- **Watchdog**: For real-time file system monitoring.
- **OS and shutil**: For file operations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zaheeb6/automated-file-organizer.git
2. Navigate to the project directory:
   ```bash
   cd automated-file-organizer
3. Install the required packages:
   ```bash
   pip install watchdog
   
## Usage
1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/yourusername/automated-file-organizer.git
   cd automated-file-organizer
   pip install watchdog
2. Open file_organizer.py in a text editor.
  
3. Modify the folder_to_track variable to specify the folder you want to monitor:
   ```bash
   folder_to_track = "/path/to/your/folder"
4. Run the script
   ```bash
   python file_organizer.py
   
5. The script will run in the background, automatically organizing files as they are added to the monitored folder.

## How It Works
- The script uses the Watchdog library to monitor the specified directory for new files.
When a new file is detected, it checks the file extension.
Based on the extension, it moves the file into a corresponding subfolder (e.g., PDFs go into a "pdf" folder).
If the destination subfolder doesn't exist, it creates one automatically.
The script continues running in the background, organizing files in real-time.

## License
- This project is licensed under the MIT License. See the LICENSE file for details.
