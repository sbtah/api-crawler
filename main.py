from crawler.logic.base_crawler import BaseApiCrawler
import asyncio
from crawler.options.endpoints import SINGLE_PRODUCT_ENDPOINT
from crawler.helpers.logger import logger
from crawler.helpers.mapper import generate_ids_map
from crawler.helpers.time_it import calculate_time


@calculate_time
def search_all_products():
    """"""
    crawler = BaseApiCrawler()
    genex = generate_ids_map()

    for generator in genex:
        products = asyncio.run(crawler.search_products_by_ids(range_of_ids=generator))
        for x in products:
            if x:
                pid = x["data"]["entity_id"]
                print(pid)


if __name__ == "__main__":
    search_all_products()