import pickle
import bz2
import _pickle as cPickle
import os
import pandas as pd

def load_bz2(env_var_path:str):
    '''
    Load compressed
    '''
    data = bz2.BZ2File(open(os.environ.get(env_var_path), 'rb'))
    embedding = cPickle.load(data)
    return embedding

def load_pickle(env_var_path:str):
    '''
    Load pickle
    '''
    embedding = pickle.load(open(os.environ.get(env_var_path), 'rb'))
    return embedding

def save_pickle(data,env_var_path:str):
    '''
    Save in pickle format
    '''
    pickle.dump(data, open(os.environ.get(env_var_path), 'wb'))

def save_bz2(data,env_var_path:str):
    '''
    Save in compressed format
    '''
    cPickle.dump(data, open(os.environ.get(env_var_path), 'wb'))

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
