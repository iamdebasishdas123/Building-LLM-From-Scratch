import tiktoken #ignore


class Preprocessing():
    def __init__(self,data):
        self.data = data
        self.tokenizer=tiktoken.get_encoding("gpt2")
    def create_token_id(self):
        # use BPE tokens
        encode=self.tokenizer.encode(self.data)
        # print(encode[:10])
        return encode
    def decode_token_id(self,encoded_data):
        decode=self.tokenizer.decode(encoded_data)
        # print(decode)
        return decode
    def vocab(self):
        pass
    def create_token_ids(self):
        pass
    
    