# File Finder360

## Description

File Finder360 is a Python 3.11.9 script that recursively searches a specified disk drive for files matching a given name or pattern (e.g., `*.txt`). It prints the full path of each found file to the console, making it easy to locate files across all folders on the target drive.

## Installation

1. **Ensure Python**

   * Verify you have Python 3.11.9 installed by running:

     ```bash
     python --version
     ```
   * Download and install from the official site if needed: [https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)

2. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/file-finder360.git
   cd file-finder360
   ```

3. **(Optional) Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**

   * No external dependencies are required; File Finder360 uses only Python’s standard library.

## Usage

Run the script with the disk letter and filename or pattern to search for:

```bash
python file-finder360.py --disk C --name "*.txt"
```

* Replace `C` with your target drive letter.
* Replace `"*.txt"` with the filename or glob pattern you wish to search for.

## License

This project is released under the MIT License. See the `LICENSE` file for details.
