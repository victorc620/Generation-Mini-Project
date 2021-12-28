import csv

def load_csv_to_list_of_dict(file_name:str):
    # Unit test completed
    """
    Load from orders.csv to creat a list of order(dict)
    """
    list = []
    with open(file_name, "r") as f:
        csv_file = csv.DictReader(f)
        for line in csv_file:
            list.append(line)
        return list
        
def export_list_of_dict_to_csv(filename: str, list_of_dict: list, fieldnames: list):
    """Export orders_list to a csv file"""
    try:
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for line in list_of_dict:
                writer.writerow(line)
    except:
        print("Failed to open file")