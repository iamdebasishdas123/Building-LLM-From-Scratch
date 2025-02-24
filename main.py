from data_read import data_ingestion
from data_prepossing import Preprocessing, create_dataloader_v1
import importlib

def main():
    data = data_ingestion()
    processed_data = Preprocessing(data)
    encode_data=processed_data.create_token_id()
    # processed_data.decode_token_id()
    dataloader=create_dataloader_v1(encode_data)
    data_iter = iter(dataloader)
    first_batch = next(data_iter)
    print("Batch",first_batch)
    



if __name__ == "__main__":
    main()