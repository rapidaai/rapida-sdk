import asyncio
import os

import sys
import time

from rapida.util import String

sys.path.append("..")
from rapida import RapidaClient, RapidaClientOptions, RapidaException, RapidaEnvironment

rapida_api_key = os.environ.get(
    "RAPIDA_API_KEY", "9ae8cfd5cf6ed1133618ed65e5ccd306a0318e811c80c96bec053883c93bb42b"
)
#

options = RapidaClientOptions(
    api_key=rapida_api_key,
    environment=RapidaEnvironment.PRODUCTION,
)

client = RapidaClient(options)


async def all_example():
    try:
        started_request = time.time()
        response = await client.invoke(
            endpoint=(2021826518103097344, "vrsn_2021826518124068864"),
            inputs={
                "schoox_reviews": String(
                    "There is change")
            },
        )
        print(
            f"time taken by rapida {(time.time() - started_request) - (response.get_time_taken() / 1000000000)}"
        )
        print(response.get_data())
        print(response.get_code())
        print(response.is_success())
    except RapidaException as ex:
        print(ex.message)


if __name__ == "__main__":
    asyncio.run(all_example(), debug=True)
