import os
from datetime import datetime
 
def parse_api_not_responding_logs(log_file_path):
    """
    Reads a log file and extracts lines indicating an API is not responding.
 
    Args:
        log_file_path (str): The full path to the log file (e.g., "/var/log/2025-07-25-log.txt").
 
    Returns:
        list: A list of strings, where each string is a line from the log
              indicating an API is not responding.
    """
    if not os.path.exists(log_file_path):
        print(f"Error: Log file not found at '{log_file_path}'")
        return []
 
    not_responding_messages = []
    search_phrase = "is not responding" # The specific part of the message to look for
 
    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                # Check if the search phrase is in the current line
                if search_phrase in line:
                    not_responding_messages.append(line.strip()) # .strip() removes leading/trailing whitespace including newline
    except Exception as e:
        print(f"Error reading log file '{log_file_path}': {e}")
        return []
 
    return not_responding_messages
 
# --- Main execution ---
if __name__ == "__main__": # Corrected from _name_ == "_main_"
    # --- Configuration ---
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.now().strftime("%Y-%m-%d")
      
    # Construct the log file path dynamically
    # Make sure '/var/log/' is accessible or change to a local directory for testing
    LOG_DIRECTORY = "/var/log" 
    LOG_FILE_NAME = f"{today_date}-log.txt"
    FULL_LOG_FILE_PATH = os.path.join(LOG_DIRECTORY, LOG_FILE_NAME)
 
    print(f"Attempting to read log file: {FULL_LOG_FILE_PATH}")
 
    # Get the messages
    failed_api_checks = parse_api_not_responding_logs(FULL_LOG_FILE_PATH)
 
    if failed_api_checks:
        print("\n--- APIs Not Responding ---")
        for message in failed_api_checks:
            print(message)
        print("---------------------------")
    else:
        print("\nNo 'API not responding' messages found in the log file.")
