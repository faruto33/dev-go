# import packages
from fastapi import FastAPI
from faq.encoder import Encoder
import os
from faq.utils import semantic_dataset
from faq.data import save_bz2,save_pickle,load_bz2,load_pickle,extract_categories

# init the API
app = FastAPI()

# load the embeddings from pickle file
if os.path.isfile(os.environ.get("EMBEDDING_PICKLE")):
    app.state.embeddings = load_pickle("EMBEDDING_PICKLE")
else:
    app.state.embeddings = None
# load categories from pickle file
if os.path.isfile(os.environ.get("CATEGORIES_PICKLE")):
    app.state.categories = load_pickle("CATEGORIES_PICKLE")
else:
    app.state.categories = None

# encoder service
@app.get("/encode")
def encode(  ):
    file_to_encode =  os.environ.get("SOURCE_FILE")
    if os.path.isfile(file_to_encode):
        text_dataset = semantic_dataset(file_to_encode)
        encoder = Encoder(os.environ.get("TRANSFORMER"))
        embeddings_dataset = encoder.encode_dataset(text_dataset)
        save_pickle(embeddings_dataset,"EMBEDDING_PICKLE")
        return {
            'status': 'embeddings list saved'
                }
    else:
         return {
            'error': "file does not found"
                }

# search service
@app.get("/search")
def search(
        keywords: str = None,
        category: str = None,
    ):
    # define a new encoder
    encoder = Encoder(os.environ.get("TRANSFORMER"))
    if keywords:
        if app.state.embeddings :
            results = encoder.get_nearest(keywords,app.state.embeddings)

    if category:
        if app.state.embeddings :
            encoder = Encoder(os.environ.get("TRANSFORMER"))
            results = encoder.filter(category,app.state.embeddings)

    if results:
        return results
    else :
        return {
            'status': 'no result'
                }


# reset categories service
@app.get("/category_reset")
def save():
    save_pickle(extract_categories("SOURCE_FILE"),"CATEGORIES_PICKLE")
    return {
    'status': 'saved category'
        }

# get all categories
@app.get("/category")
def get():
    return app.state.categories


@app.get("/")
def root():
    return {'greeting':'Welcome to the FAQ search API'}
