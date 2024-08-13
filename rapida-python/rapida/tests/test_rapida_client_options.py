"""
author: prashant.srivastav
"""
import unittest
from unittest.mock import patch
from rapida.rapida_client_options import RapidaClientOptions, RapidaEnvironment, \
    RapidaRegion


class TestRapidaClientOptions(unittest.TestCase):

    def test_initialization_with_all_parameters(self):
        """Test initialization with all parameters provided."""
        client_options = RapidaClientOptions(
            api_key="test_key",
            endpoint_url="http://example.com",
            environment=RapidaEnvironment.DEVELOPMENT,
            region=RapidaRegion.US,
            is_secure=False
        )

        self.assertEqual(client_options.rapida_api_key, "test_key")
        self.assertEqual(client_options.rapida_endpoint_url, "http://example.com")
        self.assertEqual(client_options.rapida_environment, RapidaEnvironment.DEVELOPMENT)
        self.assertEqual(client_options.rapida_region, RapidaRegion.US)
        self.assertFalse(client_options.is_secure)

    def test_initialization_with_default_parameters(self):
        """Test initialization with default parameters."""
        with patch.dict('os.environ', {}):  # Ensure environment variables are not set
            client_options = RapidaClientOptions()

        self.assertIsNone(client_options.rapida_api_key)
        self.assertEqual(client_options.rapida_endpoint_url, client_options.ENDPOINT_URL)
        self.assertEqual(client_options.rapida_environment, RapidaEnvironment.PRODUCTION)
        self.assertEqual(client_options.rapida_region, RapidaRegion.ALL)
        self.assertTrue(client_options.is_secure)

    def test_initialization_with_environment_variables(self):
        """Test initialization when environment variables are set."""
        with patch.dict('os.environ', {
            "RAPIDA_API_KEY": "env_key",
            "RAPIDA_ENDPOINT_URL": "http://env.example.com",
            "RAPIDA_ENVIRONMENT": "development",
            "RAPIDA_REGION": "eu"
        }):
            client_options = RapidaClientOptions()

        self.assertEqual(client_options.rapida_api_key, "env_key")
        self.assertEqual(client_options.rapida_endpoint_url, "http://env.example.com")
        self.assertEqual(client_options.rapida_environment, RapidaEnvironment.DEVELOPMENT)
        self.assertEqual(client_options.rapida_region, RapidaRegion.EU)
        self.assertTrue(client_options.is_secure)

    def test_environment_from_str(self):
        """Test `from_str` method of `RapidaEnvironment` enum."""
        self.assertEqual(RapidaEnvironment.from_str("production"), RapidaEnvironment.PRODUCTION)
        self.assertEqual(RapidaEnvironment.from_str("development"), RapidaEnvironment.DEVELOPMENT)
        self.assertEqual(RapidaEnvironment.from_str("invalid"), RapidaEnvironment.PRODUCTION)  # Default value

    def test_region_from_str(self):
        """Test `from_str` method of `RapidaRegion` enum."""
        self.assertEqual(RapidaRegion.from_str("ap"), RapidaRegion.AP)
        self.assertEqual(RapidaRegion.from_str("us"), RapidaRegion.US)
        self.assertEqual(RapidaRegion.from_str("eu"), RapidaRegion.EU)
        self.assertEqual(RapidaRegion.from_str("invalid"), RapidaRegion.ALL)  # Default value

