"""
author: prashant.srivastav
"""

import unittest
from unittest.mock import AsyncMock, patch, MagicMock
from typing import Dict, Mapping, Tuple, Union

from rapida import RapidaEnvironment, RapidaRegion, RapidaConfigurationException
from rapida.rapida_endpoint_client import (
    RapidaClient,
)  # Replace with the actual module path
from rapida.rapida_client_options import RapidaClientOptions
from rapida.exceptions import RapidaException
from rapida.artifacts.protos.invoker_api_pb2 import InvokerError
from rapida.client.response_wrapper import InvokeResponseWrapper


class TestRapidaClient(unittest.TestCase):

    @patch("rapida.client.rapida_client.RapidaBridge")  # Mock RapidaBridge
    def setUp(self, MockRapidaBridge):
        self.mock_rapida_bridge = MockRapidaBridge.return_value
        self.mock_rapida_bridge.make_invoke_call = AsyncMock()
        self.mock_rapida_bridge.make_update_call = AsyncMock()
        self.mock_rapida_bridge.make_probe_call = AsyncMock()
        self.client_options = RapidaClientOptions(
            api_key="test_key",
            endpoint_url="http://example.com",
            environment=RapidaEnvironment.DEVELOPMENT,
            region=RapidaRegion.US,
            is_secure=False,
        )
        self.client = RapidaClient(options=self.client_options)

    def test_initialization_with_valid_options(self):
        """Test initialization with valid options."""
        self.assertEqual(self.client.options.rapida_api_key, "test_key")
        self.assertEqual(self.client.options.rapida_endpoint_url, "http://example.com")
        self.assertEqual(
            self.client.options.rapida_environment, RapidaEnvironment.DEVELOPMENT
        )
        self.assertEqual(self.client.options.rapida_region, RapidaRegion.US)
        self.assertFalse(self.client.options.is_secure)

    def test_initialization_with_invalid_api_key(self):
        """Test initialization raises exception with invalid API key."""
        with self.assertRaises(RapidaConfigurationException):
            RapidaClient(options=RapidaClientOptions(api_key=""))

    def test_endpoint_params_with_valid_values(self):
        """Test _endpoint_params with valid values."""
        endpoint_id, endpoint_version = self.client._endpoint_params((1, "v1"))
        self.assertEqual(endpoint_id, 1)
        self.assertEqual(endpoint_version, "v1")

    def test_endpoint_params_with_none_version(self):
        """Test _endpoint_params with None version."""
        endpoint_id, endpoint_version = self.client._endpoint_params((1, None))
        self.assertEqual(endpoint_id, 1)
        self.assertEqual(endpoint_version, "latest")

    def test_options_with_allowed_keys(self):
        """Test _options method with allowed keys."""
        options = {"cache": True, "retry_count": 3, "unknown_key": "value"}
        processed_options = self.client._options(options)
        self.assertEqual(processed_options["cache"], "True")
        self.assertEqual(processed_options["retry_count"], "3")
        self.assertNotIn("unknown_key", processed_options)

    async def test_invoke_success(self):
        """Test invoke method on successful call."""
        self.mock_rapida_bridge.make_invoke_call.return_value = MagicMock(
            spec=InvokeResponseWrapper, is_success=MagicMock(return_value=True)
        )
        response = await self.client.invoke((1, "v1"), {"input": "value"})
        self.assertTrue(response.is_success())

    async def test_invoke_failure(self):
        """Test invoke method on failed call."""
        self.mock_rapida_bridge.make_invoke_call.return_value = MagicMock(
            spec=InvokeResponseWrapper,
            is_success=MagicMock(return_value=False),
            error=InvokerError(),  # Mock an InvokerError
        )
        with self.assertRaises(RapidaException):
            await self.client.invoke((1, "v1"), {"input": "value"})

    async def test_update_metadata_success(self):
        """Test update_metadata method on successful call."""
        self.mock_rapida_bridge.make_update_call.return_value = MagicMock(
            spec=InvokeResponseWrapper, success=True
        )
        response = await self.client.update_metadata(123, {"metadata": "value"})
        self.assertTrue(response.success)

    async def test_update_metadata_failure(self):
        """Test update_metadata method on failed call."""
        self.mock_rapida_bridge.make_update_call.return_value = MagicMock(
            spec=InvokeResponseWrapper,
            success=False,
            error=InvokerError(),  # Mock an InvokerError
        )
        with self.assertRaises(RapidaException):
            await self.client.update_metadata(123, {"metadata": "value"})

    async def test_probe_success(self):
        """Test probe method on successful call."""
        self.mock_rapida_bridge.make_probe_call.return_value = MagicMock(
            spec=InvokeResponseWrapper, success=True
        )
        response = await self.client.probe(123)
        self.assertTrue(response.success)

    async def test_probe_failure(self):
        """Test probe method on failed call."""
        self.mock_rapida_bridge.make_probe_call.return_value = MagicMock(
            spec=InvokeResponseWrapper,
            success=False,
            error=InvokerError(),  # Mock an InvokerError
        )
        with self.assertRaises(RapidaException):
            await self.client.probe(123)

    async def test_handle_deployment_exception(self):
        """Test handle_deployment_exception method."""
        with patch(
            "rapida.client.rapida_client.handle_request_exception"
        ) as mock_handle_exception:
            self.client.handle_deployment_exception(InvokerError())
            mock_handle_exception.assert_called_once()
