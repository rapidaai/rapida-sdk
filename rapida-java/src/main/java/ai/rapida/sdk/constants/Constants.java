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

package ai.rapida.sdk.constants;

import ai.rapida.sdk.artifacts.Common;

public class Constants {
    public static final String ENDPOINT_URL = "connect.rapida.ai";
    public static final String ASSISTANT_URL = "assistant.rapida.ai:8080";

    public static final String ENV_KEY_ENDPOINT_URL = "RAPIDA_ENDPOINT_URL";

    public static final String ENV_KEY_ASSISTANT_URL = "RAPIDA_ASSISTANT_URL";

    public static final String ENV_API_KEY = "RAPIDA_API_KEY";

    public static final String HEADER_API_KEY = "x-api-key";
    public static final String HEADER_SOURCE_KEY = "x-client-source";
    public static final String HEADER_ENVIRONMENT_KEY = "x-rapida-environment";
    public static final String HEADER_REGION_KEY = "x-rapida-region";

    public static final Common.Source DEFAULT_SOURCE = Common.Source.JAVA_SDK;


}
