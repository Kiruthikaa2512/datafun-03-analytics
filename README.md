```markdown
# **datafun-03-analytics**

## **Overview**
This project focuses on **reading, processing, and analyzing different types of data files** using Python. It covers **CSV, Excel, JSON, and TXT file handling** with structured workflows, including data extraction, filtering, word counting, and logging for debugging.

## **Local Machine Setup**
### **Step 1: Install Python (if not installed)**
- Download from: [Python.org](https://www.python.org/downloads/)
- Verify installation using the terminal.

## **Project Initialization & GitHub Setup**
### **Step 2: Create and Clone GitHub Repo**
1. Navigate to [GitHub](https://github.com/)
2. Create a new repository named `datafun-03-analytics`
3. Select **Add a README.md**
4. Clone the repo locally and navigate to the project directory.

### **Step 3: Set Up Version Control**
- Add a `.gitignore` file to exclude unnecessary files like virtual environments and cache directories.
- Use Git commands to **track changes**, commit updates, and push to the repository.

## **Virtual Environment & Dependency Setup**
### **Step 4: Set Up Python Environment**
- Create a virtual environment for dependency management.
- Activate the virtual environment according to the system you're using.

### **Step 5: Manage Dependencies**
- Install necessary libraries such as `pandas`, `openpyxl`, and `requests` to handle data processing.
- Save all dependencies in a `requirements.txt` file to maintain reproducibility.

## **Folder Structure**
```
project_root/
│── processed_data/   
  |─  excel_feedback_doc_count.txt     # Output of processed Excel file
  │── happiness_ladder_score_chart.txt   # Output of the processed CSV file as Chart
  │── ehappiness_ladder_score_stats.txt    # Output of the processed CSV file as Stats
  │── json_astronaut_names.txt    # Output of the processed Json with astronaut names 
  │─  json_astronaut_craft.txt #Output of processed json: Count of Astronauts by    Crafts
  │── Text_Gregory_Word_Count.txt    # Output of processed text : Count of word Gregory
│── raw_data/              # Stores unprocessed input files (CSV, Excel, JSON, TXT)
  │── example_get_csv.py     # Script for handling CSV files
  │── example_get_excel.py   # Script for processing Excel files
  │── example_get_json.py    # Script for extracting JSON data
  │── example_get_text.py    # Script for text file processing
  │── example_process_csv.py # Script for structured CSV processing
  │── example_process_excel.py # Script for structured excel processing
  │── example_process_json.py # Script for structured json processing
  │── example_process_text.py # Script for structured text processing
│── utils_logger.py        # Utility for logging script execution
│── logs/                  # Log files tracking execution steps                   # Log files tracking execution steps
```
```
## **Processing Different File Types**
### **1️ CSV Processing**
- Read CSV files, apply filtering conditions, and save structured results.
- Handle large datasets efficiently using Python libraries.

### **2️ Excel Processing**
- Extract and analyze data from an Excel file (`.xlsx`).
- Count occurrences of specific words within designated columns.
- Ensure proper handling of Excel formats for structured reporting.

### **3️ JSON Processing**
- Parse and extract structured information from JSON files.
- Process and format data for further analysis.

### **4️ TXT Processing**
- Read text files and extract word occurrences.
- Implement case-insensitive search and basic text analytics.

## **Logging & Debugging**
- Implement logging utilities for tracking execution steps and identifying errors.
- Validate outputs by printing previews and inspecting processed data.
- Ensure robust error handling across all file types.

## **Final Thoughts**
This guide ensures efficient data handling across **CSV, Excel, JSON, and TXT files**, enabling structured workflows for automation and analysis.

```
