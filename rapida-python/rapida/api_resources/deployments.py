from typing import Any, Dict, Optional

import asyncio

from rapida.options import RapidaClientOptions
from rapida.exceptions.exceptions import RapidaException, handle_request_exception
from rapida.client.rapida_bridge import RapidaBridge
from typing import Any, Dict


class RapidaData:

    # body_params = {}
    # update_params = {}
    # metadata_params = {}
    # override_params = {}

    def __init__(self, options: RapidaClientOptions):
        self.options = options

    def __validate_endpoint_params(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
            rapida_environment: str,
    ) -> None:
        if rapida_endpoint is None:
            raise Exception(
                "The endpoint key is required. Please provide a endpoint key.",
            )

        # self.metadata_params["rapida_endpoint"] = rapida_endpoint

        if rapida_endpoint_version is None:
            raise Warning(
                "The version is required. Default latest will be used.",
            )

        # self.metadata_params["rapida_endpoint_version"] = rapida_endpoint_version

        if rapida_environment is None:
            raise Warning(
                "The environment is required. Default Test will be used.",
            )
        # self.metadata_params["rapida_environment"] = rapida_environment

    def invoke(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
            rapida_environment: str,
            rapida_inputs: Dict[str, str],
            rapida_metadata: Dict[str, str],
            rapida_options: Dict[str, Any]
    ):
        """
        Invokes a deployment with the specified key.

        Args:
            rapida_environment: Environment to run
            rapida_inputs: Dictionary of input parameters for the prompts
            rapida_metadata: Dictionary of metadata for the current execution
            rapida_options: Dictionary of options for the overide parameters for the model
            rapida_endpoint (int): The endpoint key.
            rapida_endpoint_version (str): The endpoint version.
        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_endpoint_params(rapida_endpoint=rapida_endpoint,
                                        rapida_endpoint_version=rapida_endpoint_version,
                                        rapida_environment=rapida_environment)

        response = asyncio.run(
            RapidaBridge(self.options.rapida_endpoint_url).make_invoke_call(rapida_endpoint, rapida_endpoint_version,
                                                                            rapida_inputs, rapida_metadata,
                                                                            rapida_options))

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        return response

    def update(self, rapida_audit_id: int, rapida_metadata: dict):
        """
        Invokes a audit update with the specified key.

        Args:
            rapida_audit_id (int): The rapida_audit_id key.
            metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """

        response = asyncio.run(RapidaBridge(self.options.rapida_endpoint_url).make_update_call(rapida_audit_id, rapida_metadata))

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        return response

    def probe(self, rapida_audit_id: str):
        response = asyncio.run(
            RapidaBridge(self.options.rapida_endpoint_url).make_probe_call(rapida_audit_id))

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        return response
