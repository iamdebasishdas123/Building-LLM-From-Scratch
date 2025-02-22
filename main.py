from data_read import data_ingestion
from data_prepossing import Preprocessing
import importlib

def main():
    data = data_ingestion()
    processed_data = Preprocessing(data)
    processed_data.create_token_id()
    processed_data.decode_token_id()
    



if __name__ == "__main__":
    main()