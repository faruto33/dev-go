# import packages
from fastapi import FastAPI
from faq.encoder import Encoder
import os
from faq.utils import semantic_dataset
from faq.data import save_embedding,load_embedding


# init the API
app = FastAPI()

# load the embeddings from pickle file
if os.path.isfile(os.environ.get("EMBEDDING_PICKLE")):
    app.state.embeddings = load_embedding()
else:
    app.state.embeddings = None

# encoder service
@app.get("/encode")
def encode(  ):
    file_to_encode =  os.environ.get("SOURCE_FILE")
    if os.path.isfile(file_to_encode):
        text_dataset = semantic_dataset(file_to_encode)
        encoder = Encoder(os.environ.get("TRANSFORMER"))
        embeddings_dataset = encoder.encode_dataset(text_dataset)
        save_embedding(embeddings_dataset)
        return {
            'status': 'embeddings list saved'
                }
    else:
         return {
            'error': "file does not found"
                }


# search service
@app.get("/search")
def root(
        keywords: str,
        category: str,
    ):
    if app.state.embeddings :
        encoder = Encoder(os.environ.get("TRANSFORMER"))
        keywords_embedding = encoder.get_nearest(keywords,app.state.embeddings)

        return {
            'empty': keywords_embedding
                }
    else :
        return {
            'empty': 'ko'
                }


@app.get("/")
def root():
    return {'greeting':'Welcome to the FAQ search API'}
