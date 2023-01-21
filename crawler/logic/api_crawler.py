from crawler.logic.base_crawler import BaseApiCrawler
from crawler.helpers.logger import logger
from crawler.options.endpoints import SINGLE_PRODUCT_ENDPOINT
import httpx
import asyncio
from typing import List, Dict, Iterator


class ApiCrawler(BaseApiCrawler):
    """
    Specialized crawler that works with defined endpoints.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_single_product_by_id(self, product_id):
        """"""
        pass

    async def search_products_by_ids(self, range_of_ids: Iterator[int]) -> Dict:
        """
        Sends requests to SINGLE_PRODUCT_ENDPOINT,
        if there is a response we found a product.
        """
        async with httpx.AsyncClient() as client:

            tasks = []
            for num in range_of_ids:
                tasks.append(
                    asyncio.ensure_future(
                        self.async_get(
                            client,
                            SINGLE_PRODUCT_ENDPOINT.format(num),
                        )
                    )
                )

            products = await asyncio.gather(*tasks)
            return products
