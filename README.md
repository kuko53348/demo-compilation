---

🔒 Python to .SO Compiler – Code Obfuscation Demo

🎥 Demo Video: How to Obfuscate Python Code by Compiling to .SO

⚠️ Note: This is a demonstration project to test compiling .py files to .so (binaries) as a code obfuscation method. It's not a functional app, but a tool for developers to understand the current limitations with Flet's build system.

🎯 Purpose

Convert Python code into shared libraries (.so) to:

· Obfuscate source code in commercial projects
· Protect intellectual property
· Distribute applications without exposing source code
· Reduce loading time on mobile devices

---

❗ Critical Issue with Flet Build

Specific Error:

```
Traceback (most recent call last):
  File "/data/user/0/com.fletbox.codehex/files/flet/app/main.py", line 1, in <module>
    from main_page import main
ModuleNotFoundError: No module named 'main_page'
```

🔍 Why Does This Happen?

When we compile main_page.py to main_page.so:

1. Locally it works because the original .py file still exists and Python finds it
2. In GitHub Actions it fails because:
   · We delete the original .py files (to obfuscate the code)
   · The generated .so files have names like:
     · main_page.cpython-313-aarch64-linux-android.so
     · libmain_page.so
   · But the import in main.py is looking for exactly main_page!

📌 The Root Problem:

Python expects to find a module named main_page, but the compiled .so file has a different name than expected. Cython's naming convention for compiled modules doesn't match the import statement.

---

🧪 Current Project Status

Environment .py Files .so Files Works?
Local (development) ✅ Preserved ✅ Generated ✅ Works
GitHub Actions (CI/CD) ❌ Deleted ✅ Generated ❌ Fails with ModuleNotFoundError

This project serves as a proof of concept to document and visualize this error, hoping to find a solution or workaround in the future.

---

📋 Prerequisites

For Ubuntu/Linux:

```bash
# Install dependencies
sudo apt update
sudo apt install python3-dev cython3 build-essential

# Install Python and pip
sudo apt install python3-pip python3-venv

# Install Cython
pip install cython
```

For Termux (Android):

```bash
# In Termux
pkg update && pkg upgrade
pkg install python cython clang
pip install cython
```

---

🏗️ Option 1: Compile on Ubuntu/Linux

Script: create_ubuntu_so.sh

```bash
# Give execution permissions
chmod +x create_ubuntu_so.sh

# Run compilation
./create_ubuntu_so.sh
```

📸 Expected Output:

```
🔒 Starting compilation...
🗑️ Deleting all __init__.py...
📦 Backing up main.py...
   ➜ Compiling: main_page
   ➜ Compiling: utils
🗑️ Deleting main.so
📦 Restoring main.py...
📁 Creating __init__.py in all folders...
🧹 Cleaning temporary files...
✅ Compilation completed
📊 Generated .so files:
src/main_page.cpython-313-aarch64-linux-android.so
src/utils.cpython-313-aarch64-linux-android.so
```

✅ Locally, the app still works because the original .py files still exist.

---

📱 Option 2: Compile on Termux (Android)

Script: create_termux_so.sh

```bash
# Give permissions
chmod +x create_termux_so.sh

# Execute
./create_termux_so.sh
```

🔄 Key Difference:

· Uses cythonize -i which generates .so files with standard Python naming convention
· Also preserves original .py files for local testing

---

🧠 Compilation Behavior

· main.py → NEVER compiled (entry point)
· __init__.py → NEVER compiled (deleted and regenerated)
· main_page.py → Compiled to .so but import fails without the original .py
· All other .py files → Same problem: imports fail without the source file

---

🤖 Automatic Compilation with GitHub Actions

The file .github/workflows/build-apk-ipa-mobile.yml attempts to:

```yaml
# STEP 1: Compile to .so
find src -name "*.py" ! -name "main.py" | while read pyfile; do
    cython -3 --embed "$pyfile" -o "${pyfile%.py}.c"
    aarch64-linux-android21-clang -shared ... -o "src/lib${module}.so"
done

# STEP 2: DELETE all .py files (THIS IS WHERE IT BREAKS!)
find src -name "*.py" ! -name "main.py.backup" -delete

# STEP 3: Build APK (WILL FAIL)
flet build apk
```

🐛 The Exact Error We Get:

```
Traceback (most recent call last):
  File "/data/user/0/com.fletbox.codehex/files/flet/app/main.py", line 1, in <module>
    from main_page import main
ModuleNotFoundError: No module named 'main_page'
```

Why? Because main_page.py was deleted and replaced by libmain_page.so, but Python doesn't recognize that file as the main_page module.

---

🔬 Root Cause Analysis

Generated .so File Naming:

Method Generated File Does Python recognize it as 'main_page'?
cythonize -i main_page.cpython-311-aarch64-linux-android.so ✅ Yes (standard naming)
Manual compilation libmain_page.so ❌ No (wrong name)
Manual compilation main_page.so ⚠️ Depends on configuration

The Import in main.py:

```python
from main_page import main  # Python looks for: main_page.py, main_page.so, main_page.pyc, etc.
```

If the file is not named exactly main_page.so (without extra prefixes or suffixes), Python won't find it.

---

🧪 Testing Locally (Simulating the Error)

```bash
# 1. Compile
./create_ubuntu_so.sh

# 2. Temporarily move .py files to simulate production
mkdir temp_backup
find src -name "*.py" ! -name "main.py" ! -name "main.py.backup" -exec mv {} temp_backup/ \;

# 3. Try to run (SHOULD FAIL)
python src/main.py
# ERROR: ModuleNotFoundError: No module named 'main_page'

# 4. Restore to continue development
mv temp_backup/* src/
```

---

📝 Possible Solutions (To Be Investigated)

1. Always use cythonize -i which generates the correct naming convention
2. Rename the .so files after compilation to match the import
3. Modify sys.path or use custom import hooks
4. Keep empty __init__.py files and use a different package structure
5. Compile everything into a single .so file instead of separate modules
6. Patch Flet's build process to recognize compiled modules during APK packaging

---

📦 Example Structure That Causes the Error

```
src/
├── main.py                 # Entry point
│   └── from main_page import main  # ← LINE THAT FAILS
├── main_page.py            # Compiled to libmain_page.so ❌
├── utils.py                # Compiled to libutils.so ❌
├── subfolder/
│   ├── __init__.py
│   └── helpers.py          # Compiled to libhelpers.so ❌
```

After deleting .py files:

```
src/
├── main.py
├── libmain_page.so         # ❌ Python doesn't recognize this as 'main_page'
├── libutils.so             # ❌ Python doesn't recognize this as 'utils'
├── subfolder/
│   ├── __init__.py
│   └── libhelpers.so       # ❌ Python doesn't recognize this as 'helpers'
```

---

🎥 Demo Video

https://img.youtube.com/vi/K2K_ElKLYHY/0.jpg

Click the image to watch the video on YouTube

The video shows:

· ✅ Successful compilation on Termux
· ✅ Local execution with .py files present
· ❌ Simulation of the error that occurs in GitHub Actions

---

⚠️ Important Notes for Flet Developers

· main.py and init.py are never compiled
· Original .py files must be kept locally for the app to work during development
· True obfuscation is not yet possible with Flet due to this import error
· The Python import system expects module names to match file names exactly
· flet build seems to perform static analysis that doesn't recognize compiled modules

What Flet Could Do:

1. Modify the build process to recognize .so files as valid modules
2. Patch the import system in the packaged app to look for compiled modules
3. Use a different packaging strategy that preserves module names
4. Implement a custom importer for compiled extensions in the Flet runtime
