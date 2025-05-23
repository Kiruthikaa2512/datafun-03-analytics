"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
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

# TODO: Add or replace this with a function that reads and processes your CSV file

def analyze_ladder_score(file_path: pathlib.Path) -> dict:
    """Analyze the Ladder score column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        score_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    score = float(row["Ladder score"])  # Extract and convert to float
                    # append the score to the list
                    score_list.append(score)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(score_list),
            "max": max(score_list),
            "mean": statistics.mean(score_list),
            "stdev": statistics.stdev(score_list) if len(score_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    
    # TODO: Replace with path to your CSV data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "2020_happiness.csv")

    # TODO: Replace with path to your CSV processed file
    stats_output_file = pathlib.Path(PROCESSED_DIR, "happiness_ladder_score_stats.txt")
    
    # TODO: Call your new function to process YOUR CSV file
    stats = analyze_ladder_score(input_file)
    
    # TODO: Create a new local variable to store the result of the function call
    chart_output_file = pathlib.Path(PROCESSED_DIR, "happiness_ladder_score_chart.txt")
   
    # Create the output directory if it doesn't exist
    stats_output_file.parent.mkdir(parents=True, exist_ok=True)

    # Open the output file in write mode and write the results
    with stats_output_file.open('w') as file:
        file.write("Ladder Score Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")

    # TODO: Generate and save the bar chart
    save_star_bar_chart(input_file, chart_output_file)

    # Log both actions
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {stats_output_file}")
    logger.info(f"Text-based bar chart saved to: {chart_output_file}")

#New function to generate a text-based bar chart
def save_star_bar_chart(file_path: pathlib.Path, output_file: pathlib.Path, top_n: int = 10):
    """Generate and save a text-based bar chart using '*' characters."""
    try:
        with file_path.open('r') as file:
            reader = csv.DictReader(file)
            country_scores = [
                (row.get("Country name", "Unknown").strip(), float(row.get("Ladder score", "0").strip()))
                for row in reader if row.get("Ladder score")
            ]
        
        # Sort top N countries and build the bar chart
        chart_lines = ["Top Happiness Scores (Text-based Bar Chart)\n"] + [
            f"{country:20} | {'*' * int(score * 5)} ({score:.2f})"
            for country, score in sorted(country_scores, key=lambda x: x[1], reverse=True)[:top_n]
        ]

        # Ensure output directory exists and save to file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text("\n".join(chart_lines))

        logger.info(f"Text-based bar chart saved to: {output_file}")
    
    except Exception as e:
        logger.error(f"Error generating star bar chart: {e}")


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")