import asyncio
import os
import sys

sys.path.append("..")
from rapida import RapidaClient, RapidaClientOptions, RapidaException

rapida_api_key = os.environ.get("RAPIDA_API_KEY", "SEXj82nubm950fS9qdidwYHkKvuUVP8T")
rapida_endpoint_url = os.environ.get("RAPIDA_ENDPOINT_URL", "localhost:9005")

# init rapida client with options
options = RapidaClientOptions(
    rapida_api_key=rapida_api_key,
    rapida_endpoint_url=rapida_endpoint_url,
    rapida_environment="production",
)

client = RapidaClient(options)


async def all_example():
    try:
        response = await client.invoke(
            rapida_endpoint=747474747474,
            rapida_endpoint_version="1.0",
            rapida_environment="Production",
            rapida_inputs={"firstname": "John", "city": "New York"},
            rapida_metadata={"request_id": "Qwtqwty90281", "batch_id": "XXXXXXXXX"},
            rapida_options={
                "cache": False,
                "retry_count": 2,
            },  # {'cache':False, 'retry_count':2}
        )

        print(response)
    except RapidaException as ex:
        print(ex.message)
    #

    try:
        response = await client.update_metadata(
            rapida_audit_id=84848484848,
            rapida_metadata={"request_id": "Qwtqwty90281", "batch_id": "XXXXXXXXX"},
        )

        print(response)
    except RapidaException as ex:
        print(ex.message)

    try:
        response = await client.probe(rapida_audit_id=84848484848)
        print(response)
    except RapidaException as ex:
        print(ex.message)


if __name__ == "__main__":
    asyncio.run(all_example(), debug=True)
