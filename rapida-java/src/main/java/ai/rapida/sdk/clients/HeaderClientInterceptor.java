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
import io.grpc.CallOptions;
import io.grpc.Channel;
import io.grpc.ClientCall;
import io.grpc.ClientInterceptor;
import io.grpc.Metadata;
import io.grpc.MethodDescriptor;
import io.grpc.ForwardingClientCall;

public class HeaderClientInterceptor implements ClientInterceptor {
    private final Metadata headers;

    public HeaderClientInterceptor(Metadata headers) {
        this.headers = headers;
    }

    @Override
    public <ReqT, RespT> ClientCall<ReqT, RespT> interceptCall(
            MethodDescriptor<ReqT, RespT> methodDescriptor, CallOptions callOptions, Channel channel) {
        return new ForwardingClientCall.SimpleForwardingClientCall<ReqT, RespT>(
                channel.newCall(methodDescriptor, callOptions)) {

            @Override
            public void start(ClientCall.Listener<RespT> responseListener, Metadata headers) {
                super.start(responseListener, headers);
                headers.merge(HeaderClientInterceptor.this.headers);
            }
        };
    }
}