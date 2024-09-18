# import packages
from fastapi import FastAPI
# import os
import os
from faq.encoder import Encoder
from faq.data import save_pickle,load_pickle,extract_categories
from faq.utils import semantic_dataset
from fastapi.middleware.cors import CORSMiddleware

# init the API
app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# load the embeddings from pickle data
app.state.embeddings = load_pickle("EMBEDDING_PICKLE") if os.path.isfile(os.environ.get("EMBEDDING_PICKLE")) else None
# load categories from pickle data
app.state.categories = load_pickle("CATEGORIES_PICKLE") if os.path.isfile(os.environ.get("CATEGORIES_PICKLE")) else None
# load pandas data from pickle data
app.state.pandas = load_pickle("PANDAS_DATA_PICKLE") if os.path.isfile(os.environ.get("PANDAS_DATA_PICKLE")) else None

# encoder service
@app.get("/encode")
def encode(  ):
    # get CSV source file path
    file_to_encode =  os.environ.get("SOURCE_FILE")
    # if file exists
    if os.path.isfile(file_to_encode):
        # prepare the dataset for semantic search
        dataset = semantic_dataset(file_to_encode)
        # save pandas data
        save_pickle(dataset,"PANDAS_DATA_PICKLE")
        # get embeddings from the dataset
        corpus_embeddings = Encoder().get_embeddings(dataset['text'].to_list())
        # save embeddings in pickle data
        save_pickle(corpus_embeddings,"EMBEDDING_PICKLE")
        # return success
        return { 'status': 'embeddings list saved'}
    else:
        # return failed
        return { 'error': "file does not found" }

# search service
@app.get("/search")
def search(
        keywords: str = None,
        category: str = None,
        limit: int = 5
    ):
    # define a new encoder
    encoder = Encoder()
    # init empty results list
    results = []
    # if keywords search, get the nearest results in the embeddings
    if keywords:
        results = Encoder().search(keywords,app.state.embeddings,app.state.pandas,limit)
    # if category search, filter results per category in the embeddings
    if category:
        results = encoder.filter_format(category,app.state.pandas)
    # return results or failed
    if len(results):
        return results
    else :
        return { 'status': 'no result' }

# reset categories service
@app.get("/category_reset")
def save():
    # save category list in pickle data
    save_pickle(extract_categories("SOURCE_FILE"),"CATEGORIES_PICKLE")
    return { 'status': 'saved category' }

# get all categories
@app.get("/category")
def get():
    # return the list of all categories
    return app.state.categories
