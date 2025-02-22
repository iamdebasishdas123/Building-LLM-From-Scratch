# Description: This file reads the data from the file and returns the data.

def data_ingestion():
    """
    This function reads the data from the file and returns the data.
    """
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        data = f.read()
    return data