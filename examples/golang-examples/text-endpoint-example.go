package main

import (
	"fmt"

	rapida "github.com/rapidaai/rapida-go/rapida"
	rapida_builders "github.com/rapidaai/rapida-go/rapida/builders"
	rapida_definitions "github.com/rapidaai/rapida-go/rapida/definitions"
)

func main() {
	fmt.Printf("Running an text endpoint example")
	client, _ := rapida.GetClient(rapida_builders.ClientOptionBuilder().
		WithApiKey("05064a056f0a60f309ff1d5cc66cb6bb5ecd1d79238e048b2594b51bfb9d4610").
		Build())
	endpoint, _ := rapida_definitions.NewEndpoint(2084859551571509248, "vrsn_2084859551600869376")
	res, _ := client.Invoke(rapida_builders.InvokeRequestBuilder(endpoint).Build())
	data, err := res.GetData()
	if err == nil {
		for _, c := range data {
			print(c.ToText())
		}
	}

	// _ := rapida.NewClient() // Replace with actual SDK initialization

	// 	import asyncio
	// import os
	// import sys

	// from rapida.values import StringValue, AudioValue

	// sys.path.append("..")
	// rapida_endpoint_url = os.environ.get("RAPIDA_ENDPOINT_URL", "localhost:9005")

	// from rapida import RapidaClient, RapidaClientOptions, RapidaException, RapidaEnvironment

	// rapida_api_key = os.environ.get("RAPIDA_API_KEY", "05064a056f0a60f309ff1d5cc66cb6bb5ecd1d79238e048b2594b51bfb9d4610")

	// # init rapida client with options
	// options = RapidaClientOptions(
	//     api_key=rapida_api_key,
	//     endpoint_url=rapida_endpoint_url,
	//     environment=RapidaEnvironment.PRODUCTION,
	//     is_secure=False,
	// )

	// client = RapidaClient(options)
	// from rapida import RapidaClient, RapidaClientOptions, RapidaException, RapidaEnvironment

	// async def all_example():
	//     # run the example from here

	//     try:
	//         fls = AudioValue("/Users/prashant.srivastav/Downloads/audio/input_test.wav")
	//         response = await client.invoke(
	//             endpoint=(2084859551571509248, "vrsn_2084859551600869376"),
	//             inputs={
	//                 "file": fls
	//             },
	//         )
	//         print(response.get_data())
	//         print(response.get_code())
	//         #
	//         print("time taken")
	//         print(f"{response.get_time_taken()/1000} in second")
	//         print(response.is_success())
	//     except RapidaException as ex:
	//         print(ex.message)

	// if __name__ == "__main__":
	//     asyncio.run(all_example(), debug=True)

}
