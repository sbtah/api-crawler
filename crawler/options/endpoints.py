import os
from dotenv import load_dotenv


# Get private data fron .env variable
load_dotenv()

LOCAL_STORES_ENDPOINT = os.environ.get("LOCAL_STORES_ENDPOINT")
HOME_PAGE_ENDPOINT = os.environ.get("HOME_PAGE_ENDPOINT")
SINGLE_PRODUCT_ENDPOINT = os.environ.get("SINGLE_PRODUCT_ENDPOINT")
