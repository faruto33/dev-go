from datasets import Dataset
from transformers import AutoTokenizer, AutoModel
import pandas as pd

class Encoder:
    def __init__(self,model_ckpt:str):
        """
        Init a new embedding encoder
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
        self.model = AutoModel.from_pretrained(model_ckpt)

    def get_embeddings(self,text_list):
        '''
        Get the embedding encoding of on specific text value
        '''
        encoded_input = self.tokenizer(text_list, padding=True, truncation=True, return_tensors="pt")
        encoded_input = {k: v for k, v in encoded_input.items()}
        model_output = self.model(**encoded_input)
        return model_output.last_hidden_state[:, 0]

    def encode_dataset(self,text_dataset:Dataset):
        '''
        Encode a whole dataset with FAISS index
        '''
        embeddings_dataset =  text_dataset.map(
            lambda x: {"embeddings": self.get_embeddings(x["text"]).detach().numpy()[0]}
        )
        embeddings_dataset.add_faiss_index(column="embeddings")

        return embeddings_dataset

    def get_nearest(self,keywords,embeddings_dataset):
        '''
        Get the nearest results
        '''
        # encode keywords
        keywords_embedding = self.get_embeddings(keywords).detach().numpy()
        # get nearest result from the embeddings dataset
        scores, results = embeddings_dataset.get_nearest_examples("embeddings", keywords_embedding, k=5)

        # delete unused results
        del results['id']
        del results['embeddings']
        del results['lang']
        del results['__index_level_0__']
        # add scores
        results['scores'] = scores.tolist()
        # return results
        return results
