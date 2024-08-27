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

import ai.rapida.sdk.artifacts.TalkApi;
import ai.rapida.sdk.artifacts.TalkServiceGrpc;
import ai.rapida.sdk.constants.Constants;
import ai.rapida.sdk.enums.RapidaEnvironment;
import ai.rapida.sdk.enums.RapidaRegion;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.Metadata;

import java.util.Iterator;

public class TalkServiceClient {
    private final TalkServiceGrpc.TalkServiceBlockingStub blockingStub;
    private final TalkServiceGrpc.TalkServiceStub asyncStub;

    public TalkServiceClient(String host, int port, String rapidaKey,
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
        blockingStub = TalkServiceGrpc.newBlockingStub(channel);
        asyncStub = TalkServiceGrpc.newStub(channel);
    }

    public TalkServiceClient(String url, String rapidaKey,
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
        blockingStub = TalkServiceGrpc.newBlockingStub(channel);
        asyncStub = TalkServiceGrpc.newStub(channel);
    }

    public Iterator<TalkApi.CreateAssistantMessageResponse> createAssistantMessage(TalkApi.CreateAssistantMessageRequest request) {
        return blockingStub.createAssistantMessage(request);
    }

    public TalkApi.GetAllAssistantConversationResponse getAllAssistantConversation(TalkApi.GetAllAssistantConversationRequest request) {
        return blockingStub.getAllAssistantConversation(request);
    }

    public TalkApi.GetAllConversationMessageResponse getAllConversationMessage(TalkApi.GetAllConversationMessageRequest request) {
        return blockingStub.getAllConversationMessage(request);
    }

    public void getAllConversationMessageAsync(
            TalkApi.GetAllConversationMessageRequest request,
            io.grpc.stub.StreamObserver<TalkApi.GetAllConversationMessageResponse> responseObserver
    ) {
        asyncStub.getAllConversationMessage(request, responseObserver);
    }



    public void getAllAssistantConversationAsync(
            TalkApi.GetAllAssistantConversationRequest request,
            io.grpc.stub.StreamObserver<TalkApi.GetAllAssistantConversationResponse> responseObserver
    ) {
        asyncStub.getAllAssistantConversation(request, responseObserver);
    }


    public void createAssistantMessageAsync(
            TalkApi.CreateAssistantMessageRequest request,
            io.grpc.stub.StreamObserver<TalkApi.CreateAssistantMessageResponse> responseObserver
    ) {
        asyncStub.createAssistantMessage(request, responseObserver);
    }

}