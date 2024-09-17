# load package
import pandas as pd

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
    # Return the dataset
    return data
