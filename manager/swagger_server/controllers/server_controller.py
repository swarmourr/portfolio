import connexion
import six

from swagger_server.models.db_model import DbModel  # noqa: E501
from swagger_server import util


def add_db_config(payload):  # noqa: E501
    """Add database et data flow configuration

     # noqa: E501

    :param payload: 
    :type payload: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        payload = DbModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_agents(path):  # noqa: E501
    """Get all agent deployed

     # noqa: E501

    :param path: 
    :type path: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_data(path):  # noqa: E501
    """Get all data of an agent

     # noqa: E501

    :param path: 
    :type path: str

    :rtype: None
    """
    return 'do some magic!'