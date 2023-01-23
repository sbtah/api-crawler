import os
from dotenv import load_dotenv


# Get private data fron .env variable
load_dotenv()
SINGLE_PRODUCT_BY_ID = os.environ.get("SINGLE_PRODUCT_BY_ID")
