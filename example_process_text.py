"""
Process a text file to count occurrences of the word "Romeo" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "raw_data"
PROCESSED_DIR: str = "processed_data"

#####################################
# Define Functions
#####################################

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 1

def process_text_file():
    """Read a text file, count occurrences of 'GREGORY', and save the result."""
 
    # TODO: Replace with path to your text data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "Romeo_and_Juliet_Play.txt")

    # TODO: Replace with path to your text processed file
    output_file = pathlib.Path(PROCESSED_DIR, "Text_Gregory_Word_Count.txt")

    # TODO: Replace with the word you want to count from your text file
    word_to_count: str = "GREGORY"

    # TODO: Make any necessary changes to the logic
    # Updated logic: Prevents errors by checking if the file exists first
    # If the file is missing, returns 0 instead of causing a failure
    word_count: int = count_word_occurrences(input_file, word_to_count) if input_file.exists() else 0

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write the results to the output file
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write(f"Occurrences of '{word_to_count}'appears {word_count} times in the text.\n")
    
    # Log the processing of the TEXT file
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")