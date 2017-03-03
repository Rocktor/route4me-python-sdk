# codebeat:disable[SIMILARITY, ABC]
import json

from route4me.api_endpoints import AVOIDANCE
from route4me.base import Base
from route4me.exceptions import ParamValueException
from route4me.utils import json2obj


class AvoindanceZones(Base):
    """
    Avoidance Zones Management
    """

    def __init__(self, api):
        """
        Avoidance Zones Instance
        :param api:
        :return:
        """
        self.json_data = {}
        Base.__init__(self, api)

    def get_avoidance_zones(self):
        """
        Get avoidance zones using GET request
        :return: API response
        :raise: ParamValueException if required params are not present.
        """
        if self.check_required_params(self.params, ['api_key', ]):
            self.response = self.api._request_get(AVOIDANCE,
                                                  self.params)
            response = json2obj(self.response.content)
            return response
        else:
            raise ParamValueException('params', 'Params are not complete')

    def get_avoidance_zone(self, **kwargs):
        """
        Get avoidance zones using GET request
        :return: API response
        :raise: ParamValueException if required params are not present.
        """
        kwargs.update({'api_key': self.params['api_key'], })
        if self.check_required_params(kwargs, ['api_key', 'territory_id']):
            self.response = self.api._request_get(AVOIDANCE,
                                                  kwargs)
            response = json2obj(self.response.content)
            return response
        else:
            raise ParamValueException('params', 'Params are not complete')

    def add_avoidance_zone(self, **kwargs):
        """
        Add avoidance zone using POST request
        :return: API response
        :raise: ParamValueException if required params are not present.
        """
        if self.check_required_params(kwargs, ['territory_name',
                                               'territory_color',
                                               'territory']):
            self.response = self.api._request_post(AVOIDANCE,
                                                   self.params,
                                                   data=json.dumps(kwargs))
            response = json2obj(self.response.content)
            return response
        else:
            raise ParamValueException('params', 'Params are not complete')

    def delete_avoidance_zone(self, **kwargs):
        """
        Delete avoidance zone using DELETE request
        :return: API response
        :raise: ParamValueException if required params are not present.
        """
        kwargs.update({'api_key': self.params['api_key'], })
        if self.check_required_params(kwargs, ['territory_id']):
            self.response = self.api._request_delete(AVOIDANCE,
                                                     kwargs)
            response = json2obj(self.response.content)
            return response
        else:
            raise ParamValueException('params', 'Params are not complete')

    def update_avoidance_zone(self, territory_id, **kwargs):
        """
        Delete avoidance zone using DELETE request
        :return: API response
        :raise: ParamValueException if required params are not present.
        """
        self.params.update({'territory_id': territory_id})
        if self.check_required_params(kwargs, ['territory_name',
                                               'territory_color',
                                               'territory']):
            self.response = self.api._request_put(AVOIDANCE,
                                                  self.params,
                                                  data=json.dumps(kwargs))
            response = json2obj(self.response.content)
            return response
        else:
            raise ParamValueException('params', 'Params are not complete')

# codebeat:enable[SIMILARITY, ABC]
