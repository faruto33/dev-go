import pickle
import bz2
import _pickle as cPickle
import os

def load_compressed_embedding():
    '''
    Load from the compressed embedding
    '''
    data = bz2.BZ2File(open(os.environ.get("EMBEDDING_COMPRESSED"), 'rb'))
    embedding = cPickle.load(data)
    return embedding

def load_embedding():
    '''
    Load embedding
    '''
    embedding = pickle.load(open(os.environ.get("EMBEDDING_PICKLE"), 'rb'))
    return embedding

def save_embedding(embedding):
    '''
    Save embedding in pickle format
    '''
    pickle.dump(embedding, open(os.environ.get("EMBEDDING_PICKLE"), 'wb'))

def save_compressed_embedding(embedding):
    '''
    Save embedding in compressed pickle format
    '''
    cPickle.dump(embedding, open(os.environ.get("EMBEDDING_COMPRESSED"), 'rb'))
