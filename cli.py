import csv

def save_to_csv(parsed_data, filename="output.csv"):
    """
    Save extracted paper details to a CSV file.

    Parameters:
        parsed_data (list): List of dictionaries containing paper details.
        filename (str): Filename for the output CSV.
    """
    # Ensure parsed_data has data before proceeding
    if not parsed_data:
        print("No data to save.")
        return

    # Use the keys from the first dictionary as column headers
    keys = parsed_data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(parsed_data)
    
    print(f"Data saved to {filename}")