"""
This example file fetches an Excel file from the web 
and saves it to a local file named feedback.xlsx in a folder named example_data.

Please save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import requests
import pandas as pd

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR = "example_data"

#####################################
# Define Functions
#####################################

def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch Excel data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the Excel file to fetch.
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching Excel data from {url}...")
        response = requests.get(url)

        # FIXED: Allow both valid Excel MIME type and GitHub's octet-stream
        content_type = response.headers.get("Content-Type", "")
        if response.status_code == 200 and (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" in content_type
            or "application/octet-stream" in content_type
        ):
            logger.info("Download successful. Content appears to be an Excel file.")
            write_excel_file(folder_name, filename, response.content)
            logger.info(f"SUCCESS: Excel file fetched and saved as {filename}")
        else:
            logger.error(f"Download failed or unsupported file type. Status: {response.status_code}, Content-Type: {content_type}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_excel_file(folder_name: str, filename: str, binary_data: bytes) -> None:
    """
    Write Excel binary data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        binary_data (bytes): Binary content of the Excel file.
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing Excel data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        logger.info(f"SUCCESS: Excel data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing Excel data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching and reading Excel data.
    """
    excel_url = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/Feedback.xlsx'
    excel_path = pathlib.Path(FETCHED_DATA_DIR, "Feedback.xlsx")

    logger.info("Starting Excel fetch demonstration...")
    fetch_excel_file(FETCHED_DATA_DIR, "Feedback.xlsx", excel_url)

    # ✅ Now try to read it using pandas after download is complete
    try:
        df = pd.read_excel(excel_path)
        print("\nExcel Data Preview:\n")
        print(df.head())
    except Exception as e:
        logger.error(f"Failed to read Excel file with pandas: {e}")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
