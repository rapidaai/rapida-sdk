import asyncio
import os

import sys
import time

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
                "schoox_reviews": "[{'question': 'Do you find your work load reasonable? Why or why not?', 'attributes': ['Happiness'], 'answer': 'Yes, i find my work load reasonable , because Schoox is a huge company!!!'}, {'question': 'Hey {{first_name}}, If we, at {{company__name}} could do one thing to make Mondays more exciting for you, what would it be?', 'attributes': ['Motivation', 'Happiness'], 'answer': 'Every beginning of the week in my job,is also a happy beginning of life for me!'}, {'question': 'What actions are needed to improve the current culture?', 'attributes': ['Motivation', 'Growth', 'Happiness', 'Recognition'], 'answer': '.'}, {'question': 'What is one thing causing you stress today?', 'attributes': ['Motivation', 'Happiness'], 'answer': 'The many open tasks.'}, {'question': 'What aspects of your job bring you joy?', 'attributes': ['Motivation', 'Happiness'], 'answer': 'Having the chance to use my creativity in my day to day tasks. You can create automated tests in so many different ways and I like to make each one as optimized as possible.'}, {'question': "
                "What part is {{company__name}} playing to help you grow professionally? If we aren't playing any, how can we improve?"
                ", 'attributes': ['Growth'], 'answer': 'I think this could be improved by providing opportunities to work with other teams, to shadow, or be mentored, or work directly with another person outside of the immediate team.'}, {'question': '{{first_name}}, if you could choose a colleague, team member, or any of your leaders to coach you on a particular topic, who would it be and why?', 'attributes': ['Growth'], 'answer': 'She would be my supervisor who always helps me with whatever I need!'}]"
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
