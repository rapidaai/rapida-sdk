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

from typing import Optional
import os

from rapida import rapida_source
from rapida.constants import ASSISTANT_URL, ENDPOINT_URL, GATEWAY_URL
from rapida.rapida_environment import RapidaEnvironment
from rapida.rapida_region import RapidaRegion


class RapidaClientOptions:
    """
    RapidaAI client options
    """

    rapida_api_key: str
    rapida_endpoint_url: str
    rapida_assistant_url: str
    rapida_gateway_url: str
    rapida_region: Optional[RapidaRegion]
    rapida_environment: Optional[RapidaEnvironment]
    is_secure: bool
    rapida_source = rapida_source.RapidaSource.PYTHON_SDK

    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        environment: Optional[RapidaEnvironment] = RapidaEnvironment.PRODUCTION,
        region: Optional[RapidaRegion] = RapidaRegion.ALL,
        is_secure: bool = True,
        assistant_url: Optional[str] = None,
        gateway_url: Optional[str] = None,
    ):
        """

        Args:
            api_key:
            endpoint_url:
            region:
            environment:
        """
        self.rapida_api_key = api_key or os.environ.get("RAPIDA_API_KEY")
        self.rapida_endpoint_url = (
            endpoint_url or os.environ.get("RAPIDA_ENDPOINT_URL") or ENDPOINT_URL
        )

        self.rapida_assistant_url = (
            assistant_url or os.environ.get("RAPIDA_ASSISTANT_URL") or ASSISTANT_URL
        )
        self.rapida_gateway_url = (
            gateway_url or os.environ.get("RAPIDA_GATEWAY_URL") or GATEWAY_URL
        )
        self.rapida_environment = environment or os.environ.get("RAPIDA_ENVIRONMENT")
        self.rapida_region = region or os.environ.get("RAPIDA_REGION")
        self.is_secure = is_secure
