import asyncio
import time
from crawler.helpers.logger import logger
from crawler.helpers.mapper import generate_ids_map, generate_ids_map_from_file
from crawler.helpers.time_it import calculate_time
from crawler.logic.api_crawler import ApiCrawler
from crawler.options.endpoints import (
    SINGLE_PRODUCT_BY_ID,
    SINGLE_PRODUCT_BY_ID_FOR_STORE_ID,
)


@calculate_time
def get_stores():
    """"""
    crawler = ApiCrawler()
    stores = crawler.get_local_stores()
    for x in stores:
        print(x)


@calculate_time
def get_products_data_for_local_store_async():

    crawler = ApiCrawler()
    genex = generate_ids_map_from_file()

    for list in genex:
        product_data = asyncio.run(
            crawler.get_products_by_ids_for_local_store(
                local_store_id=8028,
                range_of_product_ids=list,
            )
        )
        for product in product_data:
            try:
                product.json()
            except Exception as e:
                if product.text:
                    print(product.text)
                else:
                    print("Blank response")


def some_test_local():
    crawler = ApiCrawler()
    genex = generate_ids_map_from_file()

    for list in genex:
        for id in list:
            resp = crawler.get(SINGLE_PRODUCT_BY_ID_FOR_STORE_ID.format(8028, id))
            if "ins-" in resp["products"][f"{id}"]["sku"]:
                print("Passing inspiration")
            else:
                if resp.text:
                    print(resp.text)
                else:
                    print("NO DATA!")


# TODO:
# Implement creating products in database.
# Right now I'm saving data to txt just as a test.
@calculate_time
def search_for_all_products_async():
    """
    Sends requests to SINGLE_PRODUCT_BY_ID asynchronously,
    if there is a response we found a product.
    Uses generate_ids_map() that will generate IDs to look for.
    """
    crawler = ApiCrawler()
    genex = generate_ids_map()

    for generator in genex:
        products = asyncio.run(
            crawler.get_products_by_ids(range_of_product_ids=generator)
        )
        for x in products:
            if x:
                with open("ids_list.txt", "a") as file1:
                    pid = x["data"]["entity_id"]
                    print(pid)
                    file1.write(f"\n{pid}")
            else:
                print(f"{x}...")


if __name__ == "__main__":
    get_products_data_for_local_store_async()
