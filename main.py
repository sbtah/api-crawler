import asyncio
import time
from crawler.helpers.logger import logger
from crawler.helpers.mapper import generate_ids_map
from crawler.helpers.time_it import calculate_time
from crawler.logic.api_crawler import ApiCrawler
from crawler.options.endpoints import SINGLE_PRODUCT_BY_ID


@calculate_time
def search_for_all_products_async():
    """"""
    crawler = ApiCrawler()
    genex = generate_ids_map()

    for generator in genex:
        products = asyncio.run(crawler.discover_products_by_ids(range_of_ids=generator))
        for x in products:
            if x:
                with open("ids_list.txt", "a") as file1:
                    pid = x["data"]["entity_id"]
                    print(pid)
                    file1.write(f"\n{pid}")
            else:
                print(f"{x}...")


if __name__ == "__main__":
    search_for_all_products_async()
