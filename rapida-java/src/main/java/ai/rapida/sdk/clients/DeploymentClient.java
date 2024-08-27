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
import ai.rapida.sdk.artifacts.DeploymentGrpc;
import ai.rapida.sdk.artifacts.InvokerApi;
import ai.rapida.sdk.constants.Constants;
import ai.rapida.sdk.enums.RapidaEnvironment;
import ai.rapida.sdk.enums.RapidaRegion;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.Metadata;

public class DeploymentClient {

    private final DeploymentGrpc.DeploymentBlockingStub blockingStub;

    public DeploymentClient(String host, int port,
                            String rapidaKey,
                            RapidaRegion region,
                            RapidaEnvironment environment,
                            boolean isSecure) {


        Metadata headers = new Metadata();
        headers.put(Metadata.Key.of(Constants.HEADER_API_KEY, Metadata.ASCII_STRING_MARSHALLER), rapidaKey);
        headers.put(Metadata.Key.of(Constants.HEADER_ENVIRONMENT_KEY, Metadata.ASCII_STRING_MARSHALLER), environment.name());
        headers.put(Metadata.Key.of(Constants.HEADER_SOURCE_KEY, Metadata.ASCII_STRING_MARSHALLER), Constants.DEFAULT_SOURCE.name());
        headers.put(Metadata.Key.of(Constants.HEADER_REGION_KEY, Metadata.ASCII_STRING_MARSHALLER), region.name());

        ManagedChannel channel = ManagedChannelBuilder.forAddress(host, port)
                .usePlaintext()
                .intercept(new HeaderClientInterceptor(headers))
                .build();
        blockingStub = DeploymentGrpc.newBlockingStub(channel);
    }

    public DeploymentClient(String url, String rapidaKey,
                            RapidaRegion region,
                            RapidaEnvironment environment,
                            boolean isSecure) {

        Metadata headers = new Metadata();
        headers.put(Metadata.Key.of(Constants.HEADER_API_KEY, Metadata.ASCII_STRING_MARSHALLER), rapidaKey);
        headers.put(Metadata.Key.of(Constants.HEADER_ENVIRONMENT_KEY, Metadata.ASCII_STRING_MARSHALLER), environment.name());
        headers.put(Metadata.Key.of(Constants.HEADER_SOURCE_KEY, Metadata.ASCII_STRING_MARSHALLER), Constants.DEFAULT_SOURCE.name());
        headers.put(Metadata.Key.of(Constants.HEADER_REGION_KEY, Metadata.ASCII_STRING_MARSHALLER), region.name());
        ManagedChannel channel = ManagedChannelBuilder.forTarget(url)
                .usePlaintext()
                .intercept(new HeaderClientInterceptor(headers))
                .build();
        blockingStub = DeploymentGrpc.newBlockingStub(channel);
    }

    public InvokerApi.InvokeResponse invoke(InvokerApi.InvokeRequest request) {
        return blockingStub.invoke(request);
    }

    public InvokerApi.UpdateResponse update(InvokerApi.UpdateRequest request) {
        return blockingStub.update(request);
    }

    public InvokerApi.ProbeResponse probe(InvokerApi.ProbeRequest request) {
        return blockingStub.probe(request);
    }
}
