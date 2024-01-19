import asyncio
import os
import sys
import time

sys.path.append("..")
from rapida import RapidaClient, RapidaClientOptions, RapidaException, RapidaEnvironment

rapida_api_key = os.environ.get("RAPIDA_API_KEY", "73d3aa9e909f826e29cd698e416b3f0de7a72f7169ed1044f31f6971cc92dab6")
rapida_endpoint_url = os.environ.get("RAPIDA_ENDPOINT_URL", "connect.rapida.ai")
#
# rapida_endpoint_url = os.environ.get("RAPIDA_ENDPOINT_URL", "localhost:9005")
# init rapida client with options
options = RapidaClientOptions(
    api_key=rapida_api_key,
    endpoint_url=rapida_endpoint_url,
    environment=RapidaEnvironment.PRODUCTION
)

client = RapidaClient(options)


async def all_example():
    try:
        started_request = time.time()
        response = await client.invoke(
            endpoint=(2006367135982419547, "1.0"),
            inputs={"firstname": "John", "city": "New York"},
            metadata={"request_id": "Qwtqwty90281", "batch_id": "XXXXXXXXX"},
            options={
                "cache": False,
                "retry_count": 2,
            },
        )
        print(f"round latency {time.time() - started_request}")
        print(response.to_dict())
    except RapidaException as ex:
        print(ex.message)
    #

    # try:
    #     response = await client.update_metadata(
    #         rapida_audit_id=84848484848,
    #         rapida_metadata={"request_id": "Qwtqwty90281", "batch_id": "XXXXXXXXX"},
    #     )
    #
    #     print(response)
    # except RapidaException as ex:
    #     print(ex.message)
    #
    # try:
    #     response = await client.probe(rapida_audit_id=84848484848)
    #     print(response)
    # except RapidaException as ex:
    #     print(ex.message)
    #

if __name__ == "__main__":
    asyncio.run(all_example(), debug=True)
