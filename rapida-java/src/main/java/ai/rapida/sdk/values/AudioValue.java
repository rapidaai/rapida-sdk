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

import javax.sound.sampled.AudioFileFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.UnsupportedAudioFileException;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class AudioValue {


    public Any AudioValue(String filePath) throws RapidaException {
        File file = new File(filePath);
        if (!file.exists()) {
            throw new RapidaException(400, "The file at " + filePath + " does not exist.", "local");
        }


        try {
            AudioSystem.getAudioFileFormat(file);
        } catch (UnsupportedAudioFileException | IOException e) {
            throw new RapidaException(400, "The file is not a valid audio file.", "local");
        }


        try (FileInputStream fileInputStream = new FileInputStream(file)) {
            byte[] audioData = fileInputStream.readAllBytes();

            if (audioData.length == 0) {
                throw new RapidaException(400, "Please provide a valid audio file.", "local");
            }

            BytesValue bytesValue = BytesValue.newBuilder().setValue(com.google.protobuf.ByteString.copyFrom(audioData)).build();
            return Any.pack(bytesValue);

        } catch (IOException e) {
            throw new RapidaException(400, "An error occurred while reading the file: " + e.getMessage(), "local");
        }
    }
}
