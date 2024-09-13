from datasets import Dataset
from transformers import AutoTokenizer, AutoModel
import pandas as pd

class Encoder:
    def __init__(self,model_ckpt:str):
        """
        Init a new embedding encoder
        """
        # create tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
        # load the pretrained model from huggingface
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

    def get_nearest(self,keywords:str,embeddings_dataset):
        '''
        Get the nearest results
        '''
        # encode keywords
        keywords_embedding = self.get_embeddings(keywords).detach().numpy()
        # get nearest result from the embeddings dataset
        scores, results = embeddings_dataset.get_nearest_examples("embeddings", keywords_embedding, k=5)

        # clean the dataset
        results = self.clean_dataset(results)
        # add scores
        results['scores'] = scores.tolist()
        # return results
        return results


    def filter(self,category:str,embeddings_dataset):
        '''
        Filter category results
        '''
        # convert to pandas
        pandaset = pd.DataFrame(embeddings_dataset)
        # filter results and convert it back to dataset
        pandaset = pandaset[pandaset['topics'].str.contains(category)]
        # clean the dataset
        cleaned_results = self.clean_dataset(pandaset.to_dict())
        final_results={}
        for k,r in cleaned_results.items():
            final_results[k]=list(r.values())
        # return results
        return final_results

    def clean_dataset(self,dataset:Dataset):
        # delete unused fields
        del dataset['id']
        del dataset['embeddings']
        del dataset['lang']
        del dataset['__index_level_0__']
        del dataset['text']
        return dataset
