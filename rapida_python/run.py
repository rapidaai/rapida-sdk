import os

from rapida import Rapida, RapidaClientOptions

api_key = os.environ.get("RAPIDA_API_KEY", "__KEY__")

options = RapidaClientOptions(
    api_key=api_key,
    environment="production"
)

client = Rapida(options)

response = client.rapida_instances.invoke(
    template="customer_service",
    model="gpt-4.0",
    retry_count=2,
    cache=False,
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"}, # template parameters
    metadata={"request_id": "Qwtqwty90281", "batch_id":"XXXXXXXXX"},
)

# rapida_audit_id = response.choices[0].message.content

response = client.rapida_instances.update(
    rapida_audit_id="xxxxxxxxxxxxxxxxxx",
    feedback=5,
    metadata={"request_id": "Qwtqwty90281", "batch_id":"XXXXXXXXX"},
)




# 


