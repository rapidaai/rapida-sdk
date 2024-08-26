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

package ai.rapida.sdk;
import ai.rapida.sdk.enums.RapidaEnvironment;
import ai.rapida.sdk.enums.RapidaRegion;

import java.util.Optional;
import java.util.logging.Logger;


/**
 * @author prashant.srivastav
 */
public class RapidaClientOption {
    private String rapidaApiKey;
    private String rapidaEndpointUrl;

    private String rapidaAssistantUrl;
    private RapidaRegion rapidaRegion;
    private RapidaEnvironment rapidaEnvironment;
    private boolean isSecure;

    private static final String ENDPOINT_URL = "connect.rapida.ai";
    private static final String ASSISTANT_URL = "assistant.rapida.ai:8080";
    private static final Logger logger = Logger.getLogger(RapidaClientOption.class.getName());


    public RapidaClientOption(
            String apiKey,
            String endpointUrl,
            String rapidaAssistantUrl,
            RapidaEnvironment environment,
            RapidaRegion region,
            boolean isSecure) {
        this.rapidaApiKey = apiKey;
        this.rapidaEndpointUrl = endpointUrl;
        this.rapidaAssistantUrl= rapidaAssistantUrl;
        this.rapidaEnvironment = environment;
        this.rapidaRegion = region;
        this.isSecure = isSecure;
    }

    public RapidaClientOption() {
        this.rapidaApiKey = System.getenv("RAPIDA_API_KEY");
        this.rapidaEndpointUrl = ENDPOINT_URL;
        this.rapidaAssistantUrl = ASSISTANT_URL;
        this.rapidaEnvironment = RapidaEnvironment.PRODUCTION;
        this.rapidaRegion = RapidaRegion.ALL;
        this.isSecure = true;
    }

    public Optional<String> getRapidaApiKey() {
        return Optional.ofNullable(rapidaApiKey);
    }

    public Optional<String> getRapidaEndpointUrl() {
        // Return the rapidaEndpointUrl wrapped in an Optional if it's not null
        if (this.rapidaEndpointUrl != null) {
            return Optional.of(this.rapidaEndpointUrl);
        }

        // If rapidaEndpointUrl is null, get the environment variable, or return the default endpoint URL
        String endpointUrl = Optional.ofNullable(System.getenv("RAPIDA_ENDPOINT_URL")).orElse(ENDPOINT_URL);
        return Optional.of(endpointUrl);
    }

    public Optional<String> getAssistantUrl() {
        // Return the rapidaEndpointUrl wrapped in an Optional if it's not null
        if (this.rapidaEndpointUrl != null) {
            return Optional.of(this.rapidaEndpointUrl);
        }

        // If rapidaEndpointUrl is null, get the environment variable, or return the default endpoint URL
        String endpointUrl = Optional.ofNullable(System.getenv("RAPIDA_ENDPOINT_URL")).orElse(ENDPOINT_URL);
        return Optional.of(endpointUrl);
    }

    public Optional<RapidaRegion> getRapidaRegion() {
        if (rapidaRegion != null) return Optional.of(this.rapidaRegion);
        return Optional.of(RapidaRegion.ALL);
    }

    public Optional<RapidaEnvironment> getRapidaEnvironment() {
        if (this.rapidaEnvironment != null) return Optional.of(this.rapidaEnvironment);
        return Optional.of(RapidaEnvironment.PRODUCTION);
    }

    public boolean isSecure() {
        return isSecure;
    }

    public void setRapidaEndpointUrl(String rapidaEndpointUrl) {
        this.rapidaEndpointUrl = rapidaEndpointUrl;
    }

    public void setRapidaAssistantUrl(String rapidaAssistantUrl) {
        this.rapidaAssistantUrl = rapidaAssistantUrl;
    }

    public void setRapidaRegion(RapidaRegion rapidaRegion) {
        this.rapidaRegion = rapidaRegion;
    }

    public void setRapidaEnvironment(RapidaEnvironment rapidaEnvironment) {
        this.rapidaEnvironment = rapidaEnvironment;
    }

    public void setSecure(boolean secure) {
        isSecure = secure;
    }
}

