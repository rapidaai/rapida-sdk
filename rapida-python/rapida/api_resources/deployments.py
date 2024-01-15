from typing import Any, Dict, Optional

import asyncio

from rapida.options import RapidaClientOptions
from rapida.util import extract_json
from rapida.exceptions.exceptions import RapidaException, handle_request_exception
from rapida.client.rapida_bridge import RapidaBridge

class RapidaData:
    body_params = {}
    update_params = {}

    def __init__(self, options: RapidaClientOptions):
        self.options = options

    def __validate_params(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
    ) -> None:
        if rapida_endpoint is None:
            raise Exception(
                "The endpoint key is required. Please provide a endpoint key.",
            )

        self.body_params["rapida_endpoint"] = rapida_endpoint

        if rapida_endpoint_version is None:
            raise Warning(
                "The version is required. Default latest will be used.",
            )

        self.body_params["rapida_endpoint_version"] = rapida_endpoint_version

    def invoke(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
            rapida_inputs=None,
            rapida_metadata=None,
    ):
        """
        Invokes a deployment with the specified key.

        Args:
            rapida_endpoint (str): The endpoint key.
            rapida_endpoint_version (str): The endpoint version.
            rapida_inputs (dict, optional): The input variables to pass to the deployment. Defaults to None.
            rapida_metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_params(rapida_endpoint=rapida_endpoint, rapida_endpoint_version=rapida_endpoint_version)

        self.body_params["rapida_environment"] = self.options.rapida_environment


        '''
            -------->> FIX THIS
        '''
        response = asyncio.run(
            RapidaBridge(self.options.rapida_endpoint_url).make_call("Invoke", rapida_endpoint, rapida_endpoint_version, self.body_params, {}))

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

    def update(self, rapida_audit_id: str, feedback: int, metadata=None):
        """
        Invokes a audit update with the specified key.

        Args:
            rapida_audit_id (str): The rapida_audit_id key.
            feedback (int): The feedback value.
            metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """

        if rapida_audit_id is not None:
            self.update_params["rapida_audit_id"] = rapida_audit_id

        if feedback is None:
            raise Exception(
                "The feedback value is required. Please provide a value key.",
            )
        if not feedback in range(0, 6):
            raise RapidaException(
                message=str("The feedback value is between 0-5."), code="ERROR", source=self.__class__.__name__
            )

        if feedback is not None:
            self.update_params["rapida_feedback"] = feedback

        '''
            -------->> FIX THIS
        '''
        response = asyncio.run(RapidaBridge.make_call("Invoke", "xxxxx", "v1", self.update_params, []))

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)