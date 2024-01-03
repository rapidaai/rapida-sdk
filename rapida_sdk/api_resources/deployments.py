from typing import Any, Dict, Optional

from requests import RequestException

from rapida_sdk.exceptions import handle_request_exception
from rapida_sdk.http_client import post
from rapida_sdk.options import RapidaClientOptions
from rapida_sdk.util import extract_json

DEPLOYMENTS_API = "https://api.rapida.cloud/v2/deployments"

# GET_CONFIG_URL = "{}/get_config".format(DEPLOYMENTS_API)
INVOKE_URL = "{}/invoke".format(DEPLOYMENTS_API)

from typing import Optional, TypedDict


class Deployments:
    body_params = {}

    def __init__(self, options: RapidaClientOptions):
        self.options = options

    def __validate_params(
        self,
        template: str,
        model: str,
        retry_count: Optional[Dict[int, Any]] = 2,
        cache: Optional[Dict[bool, Any]] = False,
        webhook_url: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
        variables: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        if template is None:
            raise Exception(
                "The template key is required. Please provide a template key."
            )

        self.body_params["template"] = template

        if model is None:
            raise Exception(
                "The model is required. Please provide a llm model."
            )

        self.body_params["model"] = model

        if retry_count is not None:
            self.body_params["retry_count"] = retry_count

        if cache is not None:
            self.body_params["cache"] = cache

        if webhook_url is not None:
            self.body_params["webhook_url"] = context

        if context is not None:
            self.body_params["context"] = context

        if variables is not None:
            self.body_params["variables"] = variables

        if metadata is not None:
            self.body_params["metadata"] = metadata

    # def get_config(self, template: str, model: str, context=None, inputs=None, metadata=None):
    #     self.__validate_params(
    #         template=template, model=model, context=context, variables=inputs, metadata=metadata
    #     )

    #     response = post(
    #         url=GET_CONFIG_URL,
    #         api_key=self.options.api_key,
    #         body=self.body_params,
    #         environment=self.options.environment,
    #     )

    #     if response.ok is None or response.status_code != 200:
    #         handle_request_exception(response)

    #     params = response.json()

    #     return DeploymentConfig(options=self.options, **params)

    def invoke(self, template: str, model: str, retry_count=2, cache=False, webhook_url=None, context=None, inputs=None, metadata=None):
        """
        Invokes a deployment with the specified key.

        Args:
            :param template (str): The template key.
            :param model (str): The llm model.
            :param context (dict, optional): The context to pass to the deployment. Defaults to None.
            :param inputs (dict, optional): The input variables to pass to the deployment. Defaults to None.
            :param metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_params(
            template=template, model=model, retry_count=retry_count, cache=cache, webhook_url=webhook_url, context=context, variables=inputs, metadata=metadata
        )

        response = post(
            url=INVOKE_URL,
            api_key=self.options.api_key,
            body=self.body_params,
            environment=self.options.environment,
        )

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        params = response.json()

        return Deployment(options=self.options, **params)

    def invoke_with_stream(self, template: str, model: str, retry_count=2, cache=False, webhook_url=None, context=None, inputs=None, metadata=None):
        """
        Invokes a deployment with the specified key and stream the response.

        Streaming is not supported for model of type `image`.

        Args:
            :param template (str): The template key.
            :param model (str): The llm model.
            :param context (dict, optional): The context to pass to the deployment. Defaults to None.
            :param inputs (dict, optional): The input variables to pass to the deployment. Defaults to None.
            :param metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_params(
            template=template, model=model, retry_count=retry_count, cache=cache, webhook_url=webhook_url, context=context, variables=inputs, metadata=metadata
        )

        response = post(
            url=INVOKE_URL,
            api_key=self.options.api_key,
            body=self.body_params,
            stream=True,
            environment=self.options.environment,
        )

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        for line in response.iter_lines():
            if line:
                data = extract_json(line)

                if data:
                    for item in data:
                        yield Deployment(options=self.options, **item)
