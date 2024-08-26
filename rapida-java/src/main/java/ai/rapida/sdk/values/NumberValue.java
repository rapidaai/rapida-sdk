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

package ai.rapida.sdk.values;

import ai.rapida.sdk.execptions.RapidaException;
import com.google.protobuf.Any;
import com.google.protobuf.FloatValue;
import com.google.protobuf.Int32Value;

public class NumberValue {
    public static Any numberValue(Number number) throws RapidaException {
        if (!(number instanceof Integer) && !(number instanceof Float) && !(number instanceof Double)) {
            throw new RapidaException(400, "The number must be an integer or a float.", "local");
        }

        Any anyMessage;
        if (number instanceof Integer) {
            Int32Value intValue = Int32Value.newBuilder().setValue((Integer) number).build();
            anyMessage = Any.pack(intValue);
        } else {
            FloatValue floatValue = FloatValue.newBuilder().setValue(number.floatValue()).build();
            anyMessage = Any.pack(floatValue);
        }

        return anyMessage;
    }
}