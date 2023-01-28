import os
from dotenv import load_dotenv


# Get private data fron .env variable
load_dotenv()
SINGLE_PRODUCT_BY_ID = os.environ.get("SINGLE_PRODUCT_BY_ID")
LOCAL_STORES_ENDPOINT = os.environ.get("LOCAL_STORES_ENDPOINT")
SINGLE_PRODUCT_BY_ID_FOR_STORE_ID = os.environ.get(
    "SINGLE_PRODUCT_BY_ID_FOR_STORE_ID",
)
