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
import com.google.protobuf.BytesValue;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class FileValue {

    public Any FileValue(String filePath) throws RapidaException {
        File file = new File(filePath);
        if (!file.exists()) {
            throw new RapidaException(400, "The file at " + filePath + " does not exist.", "local");
        }

        try (FileInputStream fileInputStream = new FileInputStream(file)) {
            byte[] fileData = fileInputStream.readAllBytes();

            if (fileData.length == 0) {
                throw new RapidaException(400, "The file is empty or invalid.", "local");
            }

            BytesValue bytesValue = BytesValue.newBuilder().setValue(com.google.protobuf.ByteString.copyFrom(fileData)).build();
            return Any.pack(bytesValue);

        } catch (IOException e) {
            throw new RapidaException(400, "An error occurred while reading the file: " + e.getMessage(), "local");
        }
    }
}