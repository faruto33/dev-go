# import packages
import pandas as pd
import numpy as np
from txtai import Embeddings
import os

class Encoder:
    def get_embeddings(self,text_list):
        '''
        Get the embedding encoding of on specific text value
        '''
        # Create embeddings, backed by sentence-transformers (disable GPU)
        embeddings = Embeddings(path=os.environ.get("TRANSFORMER"),gpu=False)
        # Add index to embeddings
        embeddings.index(text_list)
        # return embeddings to save
        return embeddings

    def get_nearest_uids(self,keywords:str,embeddings,data,nbresults):
        '''
        Get indexes of the nearest results
        '''
        # Extract uid of first results
        results = np.array(embeddings.search(keywords, nbresults)[0:nbresults],dtype=int)
        # filter and format results
        results = self.filter(None,data.iloc[results[:,0]])
        # return results uids
        return results

    # filter by category and format results to be displayed
    def filter(self,category:str,data):
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
