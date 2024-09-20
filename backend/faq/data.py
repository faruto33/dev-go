import os
import pandas as pd
import torch

def load_pickle(env_var_path:str):
    '''
    Load pickle
    '''
    embedding = torch.load(os.environ.get(env_var_path),map_location=torch.device('cpu'))
    return embedding

def save_pickle(data,env_var_path:str):
    '''
    Save in pickle format
    '''
    torch.save(data,os.environ.get(env_var_path))


def extract_categories(env_var_path):
    '''
    Extract categories from CSV file
    '''
    # read in pandas
    data = pd.read_csv(os.environ.get(env_var_path),delimiter=";")
    # keep only french language
    data = data[data['lang']=='fr']
    print(data)
    # init categories
    categories = {}
    # loop into topics
    for v in data['topics']:
        # split topics by ;
        split = v.split(';')
        # if more than 1 level
        if len(split)>1:
            # init parent category
            if split[0] not in categories:
                categories[split[0]]={}
            # add sub category
            categories[split[0]][split[1]]={}
        # if sub sub category
        if len(split)>2:
            # init sub sub category
            if split[2] not in categories[split[0]][split[1]]:
                 # add sub sub category
                categories[split[0]][split[1]][split[2]]={}

    #return categories
    return categories
