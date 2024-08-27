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
package ai.rapida.sdk.definitions;
import ai.rapida.sdk.artifacts.Common;
import ai.rapida.sdk.artifacts.InvokerApi;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.util.JsonFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

/**
 * @author prashant.srivastav
 */
public class InvokeResponseWrapper {
    private final InvokerApi.CallerResponse data;
    private final boolean success;
    private final int code;
    private final InvokerApi.InvokerError error;

    private static final Logger logger = Logger.getLogger(InvokeResponseWrapper.class.getName());

    public InvokeResponseWrapper(InvokerApi.InvokeResponse data) {
        this.data = data.getData();
        this.success = data.getSuccess();
        this.code = data.getCode();
        this.error = data.getError();
    }

    public long getTimeTaken() {
        return data.getTimeTaken();
    }

    public long getRequestId() {
        return data.getRequestId();
    }

    public String toJson() {
        try {
            return JsonFormat.printer().print(data);
        } catch (InvalidProtocolBufferException e) {
            e.printStackTrace();
            return null;
        }
    }

    public Map<String, Object> toDict() {
        try {
            // Convert the Protobuf message to a JSON string
            String jsonString = JsonFormat.printer().print(data);

            // Create a Jackson ObjectMapper to parse the JSON string
            ObjectMapper objectMapper = new ObjectMapper();

            // Convert JSON string to Map
            return objectMapper.readValue(jsonString, new TypeReference<Map<String, Object>>() {});

        } catch (InvalidProtocolBufferException | JsonProcessingException e) {
            return new HashMap<>();
        }

    }

    public List<Content> getData() {
        List<Content> contentList = new ArrayList<>();
        for (Common.Content cnt : data.getResponsesList()) {
            contentList.add(new Content(cnt));
        }
        return contentList;
    }

    public Map<String, Object> getMetadata() {
        try {
            // Convert the Protobuf message to a JSON string
            String jsonString = JsonFormat.printer().print(data.getMeta());

            // Create a Jackson ObjectMapper to parse the JSON string
            ObjectMapper objectMapper = new ObjectMapper();

            // Convert JSON string to Map
            return objectMapper.readValue(jsonString, new TypeReference<Map<String, Object>>() {});

        } catch (InvalidProtocolBufferException | JsonProcessingException e) {
            return new HashMap<>();
        }
    }

    public List<Metric> getMetrics() {
        List<Metric> metricList = new ArrayList<>();
        for (Common.Metric mtr : data.getMetricsList()) {
            metricList.add(new Metric(mtr));
        }
        return metricList;
    }

    public int getCode() {
        return this.code;
    }

    public boolean isSuccess() {
        return this.success;
    }

    public boolean isError() {
        return !this.isSuccess();
    }

    public long getErrorCode() {
        return error != null ? error.getErrorCode() : 0;
    }

    public InvokerApi.InvokerError getError() {
        return this.error;
    }

    public String getErrorMessage() {
        if (error != null) {
            return error.getErrorMessage();
        } else {
            String message = "No error message found in response";
            logger.warning(message);
            return message;
        }
    }

    public String getHumanErrorMessage() {
        if (error != null) {
            return error.getHumanMessage();
        } else {
            logger.warning("No error message found in response");
            return "No human error message found in response";
        }
    }
}
