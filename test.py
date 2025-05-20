import pathlib
import os

print("Working directory:", os.getcwd())

folder_path = pathlib.Path("example_data")
folder_path.mkdir(parents=True, exist_ok=True)

print("Created:", folder_path.resolve())
print("Exists:", folder_path.exists())
