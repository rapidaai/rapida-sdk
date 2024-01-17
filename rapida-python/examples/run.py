import asyncio
import os
import sys

sys.path.append('..')

from rapida import Rapida, RapidaClientOptions

rapida_api_key = os.environ.get("RAPIDA_API_KEY", "SEXj82nubm950fS9qdidwYHkKvuUVP8T")
rapida_endpoint_url = os.environ.get("RAPIDA_ENDPOINT_URL", "localhost:9005")

options = RapidaClientOptions(
    rapida_api_key=rapida_api_key,
    rapida_endpoint_url=rapida_endpoint_url,
    rapida_environment="production",
)

client = Rapida(options)

response = asyncio.run(client.rapida_instances.invoke(
    rapida_endpoint=747474747474,
    rapida_endpoint_version = "1.0",
    rapida_environment = "Production",
    rapida_inputs={'firstname': 'John', 'city': 'New York'},
    rapida_metadata = {'request_id': 'Qwtqwty90281', 'batch_id': 'XXXXXXXXX'},
    rapida_options = {'cache':False, 'retry_count':2}   #{'cache':False, 'retry_count':2}
))

print(response)
#
response = asyncio.run(client.rapida_instances.update_metada(
    rapida_audit_id=84848484848,
    rapida_metadata = {'request_id': 'Qwtqwty90281', 'batch_id': 'XXXXXXXXX'},
))

print(response)

response = client.rapida_instances.probe(
    rapida_audit_id=84848484848
)

print(response)

