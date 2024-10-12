#  Copyright (c) 2024. Rapida
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#  Author: Prashant <prashant@rapida.ai>

import mimetypes
import re

from google.protobuf.any_pb2 import Any
from google.protobuf.wrappers_pb2 import (
    StringValue as _StringValue,
    BytesValue,
    Int32Value,
    FloatValue,
)
import os
from PIL import Image

from rapida import RapidaException


def StringValue(_in: str) -> Any:
    """
    Args:
        _in: any string

    Returns:
        string representation of proto.any
    """
    string_value = _StringValue(value=_in)

    # Create an instance of Any
    any_message = Any()

    # Pack the StringValue instance into the Any object
    any_message.Pack(string_value)

    #
    return any_message


def FileValue(file_path: str) -> Any:
    """
    Convert a file to a proto.Any message.

    Args:
        file_path (str): Path to the file.

    Returns:
        any_pb2.Any: Packed proto.Any message containing the file data.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an error occurs while reading the file.
        ValueError: If the file is empty or an error occurs while packing.
    """
    if not os.path.isfile(file_path):
        raise RapidaException(
            code=400,
            message=f"The file at {file_path} does not exist.",
            source="local",
        )

    # Check file type
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        raise RapidaException(
            code=400,
            message="The file is not a valid file type.",
            source="local",
        )
    try:
        # Read the file data
        with open(file_path, "rb") as file:
            file_data = file.read()

        if not file_data:
            raise RapidaException(
                code=400,
                message="The file is empty or invalid.",
                source="local",
            )

        # Create an Any message and pack the BytesValue into it
        any_message = Any()
        any_message.value = file_data

        return any_message

    except IOError as e:
        raise RapidaException(
            code=400,
            message=f"An error occurred while reading the file: {e}",
            source="local",
        )
    except ValueError as e:
        raise RapidaException(
            code=400,
            message=f"Error packing the file data: {e}",
            source="local",
        )


def AudioValue(file_path: str) -> Any:
    """
    Convert an audio file to a proto.Any message.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        any_pb2.Any: Packed proto.Any message containing the audio data.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an error occurs while reading the file.
        ValueError: If the file is empty or an error occurs while packing.
    """
    if not os.path.isfile(file_path):
        raise RapidaException(
            code=400,
            message=f"The file at {file_path} does not exist.",
            source="local",
        )

        # Check file type
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type or not mime_type.startswith("audio"):
        raise RapidaException(
            code=400,
            message="The file is not a valid audio file.",
            source="local",
        )
    try:
        # Read the audio file data
        with open(file_path, "rb") as file:
            audio_data = file.read()

        if not audio_data:
            raise RapidaException(
                code=400,
                message="Please provide a valid audio file.",
                source="local",
            )

        # Create a BytesValue protobuf message with the audio data
        # bytes_value = BytesValue(value=audio_data)

        # Create an Any message and pack the BytesValue into it
        any_message = Any()
        # file_any = any_pb2.Any()
        any_message.value = audio_data

        return any_message

    except IOError as e:
        raise RapidaException(
            code=400,
            message=f"An error occurred while reading the file: {e}",
            source="local",
        )
    except ValueError as e:
        raise RapidaException(
            code=400,
            message=f"Error packing the file data: {e}",
            source="local",
        )


def ImageValue(file_path: str) -> Any:
    """
    Convert an image file to a proto.Any message with file type checking.

    Args:
        file_path (str): Path to the image file.

    Returns:
        any_pb2.Any: Packed proto.Any message containing the image data.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an error occurs while reading the file.
        ValueError: If the file is not an image or is empty.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    # Check file type
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verify the file is an image
    except (IOError, SyntaxError) as e:
        raise ValueError("The file is not a valid image.")

    try:
        # Read the image file data
        with open(file_path, "rb") as file:
            image_data = file.read()

        if not image_data:
            raise ValueError("The file is empty.")

        # Create a BytesValue protobuf message with the image data
        bytes_value = BytesValue(value=image_data)

        # Create an Any message and pack the BytesValue into it
        any_message = Any()
        any_message.value = bytes_value

        return any_message
    except IOError as e:
        raise RapidaException(
            code=400,
            message=f"An error occurred while reading the file: {e}",
            source="local",
        )
    except ValueError as e:
        raise RapidaException(
            code=400,
            message=f"Error packing the file data: {e}",
            source="local",
        )


def NumberValue(number: float) -> Any:
    """
    Convert a number to a proto.Any message.

    Args:
        number (float): The number to convert.

    Returns:
        any_pb2.Any: Packed proto.Any message containing the number.

    Raises:
        ValueError: If the number is not valid.
    """
    if not isinstance(number, (int, float)):
        raise RapidaException(
            code=400,
            message="The number must be an integer or a float.",
            source="local",
        )

    # Use Int32Value for integers or FloatValue for floating-point numbers
    if isinstance(number, int):
        number_value = Int32Value(value=number)
    elif isinstance(number, float):
        number_value = FloatValue(value=number)
    else:
        raise RapidaException(
            code=400,
            message="Unsupported number type.",
            source="local",
        )
    # Create an Any message and pack the number value into it
    any_message = Any()
    any_message.Pack(number_value)

    return any_message


def URLValue(url: str) -> Any:
    """
    Convert a URL to a proto.Any message.

    Args:
        url (str): The URL to convert.

    Returns:
        any_pb2.Any: Packed proto.Any message containing the URL.

    Raises:
        ValueError: If the URL is not valid.
    """
    # Validate the URL
    url_pattern = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ...or ipv4
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # ...or ipv6
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    if not re.match(url_pattern, url):
        raise RapidaException(
            code=400,
            message="The URL is not valid.",
            source="local",
        )

    # Create a StringValue protobuf message with the URL
    string_value = StringValue(value=url)

    # Create an Any message and pack the StringValue into it
    any_message = Any()
    any_message.Pack(string_value)

    return any_message
