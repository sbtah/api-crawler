import asyncio
from typing import Dict, Iterator, List

import httpx

from crawler.logic.base_crawler import BaseApiCrawler
from crawler.options.endpoints import SINGLE_PRODUCT_BY_ID


class ApiCrawler(BaseApiCrawler):
    """
    Specialized crawler that works with defined endpoints.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_single_product_by_id(self, product_id):
        """
        Requests SINGLE_PRODUCT_BY_ID endpoint synchronously.
        Returns JSON with Product data.
        - :arg product_id: Integer that will represent ID of Product.
        """
        pass

    async def discover_products_by_ids(
        self,
        range_of_ids: Iterator[int],
    ) -> Dict:
        """
        Sends requests to SINGLE_PRODUCT_BY_ID,
        if there is a response we found a product.
        - :arg range_of_ids: Iterator of integers that will be looped over,
            to search for products.
        """
        async with httpx.AsyncClient() as client:

            tasks = []
            for num in range_of_ids:
                tasks.append(
                    asyncio.ensure_future(
                        self.async_get(
                            client,
                            SINGLE_PRODUCT_BY_ID.format(num),
                        )
                    )
                )

            products = await asyncio.gather(*tasks)
            return products

    async def get_product_data_for_local_store():
        pass
