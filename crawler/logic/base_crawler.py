import asyncio
from random import choice
from typing import List

import httpx

from crawler.helpers.logger import logger
from crawler.options.endpoints import SINGLE_PRODUCT_ENDPOINT
from crawler.options.settings import USER_AGENTS


class BaseApiCrawler:
    """
    Simple crawler used for requesting APIs.
    """

    def __init__(self, logger=logger):
        self.logger = logger

    @classmethod
    def get_random_user_agent(cls, user_agent_list: List[str]) -> str:
        """Return random User-Agent"""
        agent = choice(user_agent_list)
        return agent

    @property
    def user_agent(self) -> str:
        agent = self.get_random_user_agent(USER_AGENTS)
        return agent

    def get(self, url: str) -> str:
        """
        Requests specified url synchronously. Returns JSON.
        - :param url: Requested URL.
        """
        headers = {"User-Agent": f"{self.user_agent}"}
        try:
            res = httpx.get(url, timeout=10, headers=headers)
            return res.json()
        except httpx._exceptions.TimeoutException:
            self.logger.error("Connection was timed out.")
            return None
        except httpx._exceptions.ConnectError:
            self.logger.error("Connection Error.")
            return None
        except httpx._exceptions.HTTPError:
            self.logger.error("HTTPError was raised.")
            return None
        except Exception as e:
            self.logger.error(f"(get) Exception: {e}")

    async def async_get(self, client: httpx.AsyncClient, url: str) -> str:
        """
        Requests specified URL asynchronously. Returns JSON.
        - :param client: Asynchronous client.
        - :param url: Requested URL.
        """
        headers = {"User-Agent": f"{self.user_agent}"}
        try:
            res = await client.get(url, headers=headers)
            return res.json()
        except Exception as e:
            self.logger.error(f"(async get) Exception: {e}")
            return None

    async def search_products_by_ids(self, range_of_ids):
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
