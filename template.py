import os
from pathlib import Path
import logging
from sys import meta_path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for file_path in list_of_files:
    path = Path(file_path)
    # Create parent directories if they don't exist
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {path.parent}")

    # Create the file if it doesn't exist
    if not path.exists():
        path.touch()
        logging.info(f"Created file: {meta_path}")
    else:
        logging.info(f"File already exists: {file_path}")
