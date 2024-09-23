# import packages
import os
import pandas as pd
from sentence_transformers import SentenceTransformer
import torch

class Encoder:
    def __init__(self) -> None:
        '''
        Get the model to encode data
        '''
        # Get the encoder sentence transformer model
        self.model = SentenceTransformer(os.environ.get("TRANSFORMER"))

    def get_embeddings(self,text_list):
        '''
        Get the embedding encoding of on specific text value
        '''
        # Add index to embeddings
        embeddings = self.model.encode(text_list)
        # return embeddings to save
        return embeddings

    def search(self,keywords:str,corpus_embeddings,corpus,nbresults):
        '''
        Get indexes of the nearest results
        '''
        top_k = min(nbresults, len(corpus))
        # get the keywords embedding
        keyword_embedding = self.get_embeddings(keywords)
        # We use cosine-similarity and torch.topk to find the highest 5 scores
        similarity_scores = self.model.similarity(keyword_embedding, corpus_embeddings)[0]
        scores, indices = torch.topk(similarity_scores, k=top_k)
        # filter and format results
        results = self.filter_format(None,corpus.iloc[indices])
        # return results uids
        return results

    # filter by category and format results to be displayed
    def filter_format(self,category:str,data):
        '''
        Filter category results
        '''
        # filter results and convert it back to dataset
        filtered_results = data[data['topics'].str.contains(category)] if category else data
        # drop unecessary column
        filtered_results = filtered_results.drop(columns={"id","lang","text"})
        # format results to be in list format
        final_results={}
        for k,r in filtered_results.items(): final_results[k]=r.to_list()
        # return results
        return final_results
