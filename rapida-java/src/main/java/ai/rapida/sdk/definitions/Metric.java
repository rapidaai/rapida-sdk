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
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.util.JsonFormat;

import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

/**
 * @author prashant.srivastav
 */

public class Metric {
    private final Common.Metric _original;
    private final String description;
    private final String name;
    private final String value;

    public Metric(Common.Metric data) {
        this._original = data;
        this.value = data.getValue();
        this.name = data.getName();
        this.description = data.getDescription();
    }

    public String toJson() {
        try {
            return JsonFormat.printer().print(_original);
        } catch (InvalidProtocolBufferException e) {
            Logger.getLogger(Metric.class.getName()).warning("Failed to convert metric to JSON: " + e.getMessage());
            return null;
        }
    }

    public Map<String, Object> toDict() {
        try {
            // Convert the Protobuf message to a JSON string
            String jsonString = JsonFormat.printer().print(_original);

            // Create a Jackson ObjectMapper to parse the JSON string
            ObjectMapper objectMapper = new ObjectMapper();

            // Convert JSON string to Map
            return objectMapper.readValue(jsonString, new TypeReference<Map<String, Object>>() {});

        } catch (InvalidProtocolBufferException | JsonProcessingException e) {
            return new HashMap<>();
        }
    }
}

