import os

from rapida_sdk import Rapida, RapidaClientOptions

api_key = os.environ.get("RAPIDA_API_KEY", "__KEY__")

options = RapidaClientOptions(
    api_key=api_key,
    environment="production"
)

client = Rapida(options)

response = client.deployments.invoke(
    template="customer_service",
    model="gpt-4.0",
    retry_count=2,
    cache=False,
    webhook_url="http://localhost:5000/webhook",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"}, # template parameters
    metadata={"request_id": "Qwtqwty90281", "batch_id":"XXXXXXXXX"},
)

# print(deployment.choices[0].message.content)


