# load package
import pandas as pd
from datasets import Dataset

def semantic_dataset(file_to_encode):
    '''
    Load from the compressed model
    '''
    # panda dataframe from a CSV file
    data = pd.read_csv(file_to_encode,delimiter=";")
    # extract french FAQ
    data = data[data['lang']=='fr']
    # Combine a new text field for semantic search
    data['text'] = data['label'] + ' ' + data['body'] + ' ' + data['topics']
    # Create a Dateset from panda dataframe
    text_dataset = Dataset.from_pandas(data)
    # Return the dataset
    return text_dataset
