# CORTX-CSM: CORTX Management web and CLI interface.
# Copyright (c) 2020 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.

from cortx.utils.log import Log
from csm.common.services import ApplicationService
from csm.common.errors import CsmUnauthorizedError

class InformationService(ApplicationService):
    """Information service class."""

    @Log.trace_method(Log.DEBUG)
    async def get_cortx_information(self, authorized=True, resource=None):
        """
        Method to fetch the cortx information

        :param **request_body: Request body kwargs
        """
        Log.debug(f"Request body: {resource}")
        if not authorized and resource == "certicate":
            raise CsmUnauthorizedError("Invalid authentication credentials for the target resource.")
        # TODO: Call Utils API to get information
        # TODO: Remove code
        # Sample Response
        response = {
            "cluster" : {
                "info": {
                    "CORTX": "2.0.0-123"
                }
            },
            "certificate" : {
                "info": {
                    "key": "value"
                }
            }
        }
        # Filter the Response based on authorization and resource
        if authorized and resource is not None:
            return response.get(resource, None)
        if not authorized:
            response.pop('certificate', None)
        return response

