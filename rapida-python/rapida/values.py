"""
author: prashant.srivastav
"""
import mimetypes

from google.protobuf.any_pb2 import Any
from google.protobuf.wrappers_pb2 import StringValue as _StringValue, BytesValue, Int32Value, FloatValue
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
    if not mime_type or not mime_type.startswith('audio'):
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
            code= 400,
            message=f"An error occurred while reading the file: {e}",
            source="local",
        )
    except ValueError as e:
        raise RapidaException(
            code= 400,
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
        any_message.Pack(bytes_value)

        return any_message
    except IOError as e:
        raise RapidaException(
            code=  400,
            message=f"An error occurred while reading the file: {e}",
            source="local",
        )
    except ValueError as e:
        raise RapidaException(
            code=  400,
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
