/*
 *  Copyright (c) 2024. Rapida
 *
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the "Software"), to deal
 *  in the Software without restriction, including without limitation the rights
 *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *  copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in
 *  all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *  THE SOFTWARE.
 *
 *  Author: Prashant <prashant@rapida.ai>
 *
 */

package ai.rapida.sdk.clients;

import ai.rapida.sdk.RapidaClientOption;
import ai.rapida.sdk.artifacts.InvokerApi;
import ai.rapida.sdk.definitions.EndpointDefinition;
import ai.rapida.sdk.definitions.InvokeResponseWrapper;
import com.google.protobuf.Any;

import java.util.Map;

public class RapidaBridge {

    private final DeploymentClient deploymentClient;
    private final TalkServiceClient talkServiceClient;

    public RapidaBridge(RapidaClientOption options) {
        this.deploymentClient = new DeploymentClient(options.getRapidaEndpointUrl().get());
        this.talkServiceClient = new TalkServiceClient(options.getAssistantUrl().get());
    }


    public InvokeResponseWrapper invokeCall(
            EndpointDefinition endpoint,
            Map<String, Any> inputs,
            Map<String, Any> metadata,
            Map<String, Any> options
    ) {
        InvokerApi.InvokeResponse invokeResponse = deploymentClient.invoke(
                InvokerApi.InvokeRequest.newBuilder()
                        .setEndpoint(InvokerApi.EndpointDefinition.newBuilder()
                                .setEndpointId(endpoint.endpoint)
                                .setVersion(endpoint.endpointVersion)
                                .build())
                        .putAllArgs(inputs)
                        .putAllMetadata(metadata)
                        .putAllOptions(options)
                        .build());
        return new InvokeResponseWrapper(invokeResponse);
    }
}
