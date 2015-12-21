import os
from collections import namedtuple
import requests
import logging


DEFAULT_URL = "https://vpn.tuxed.net/vpn-user-portal/new"
DEFAULT_USERNAME = "foo"
DEFAULT_PASSWORD = "bar"
DEFAULT_NAME = "sensor_1"


logger = logging.getLogger(__name__)

ALL_ENV = ['SENSOR_URL', 'SENSOR_USERNAME', 'SENSOR_PASSWORD', 'SENSOR_NAME']


config = namedtuple('config', ['username', 'password', 'url', 'name'])


def get_config():
    """
    Tries to get config from environment variables, if not set will use default values from this file.

    return: config namedtuple
    """
    username = os.environ.get("SENSOR_USERNAME", "") or DEFAULT_USERNAME
    password = os.environ.get("SENSOR_PASSWORD", "") or DEFAULT_PASSWORD
    url = os.environ.get("SENSOR_URL", "") or DEFAULT_URL
    name = os.environ.get("SENSOR_NAME", "") or DEFAULT_NAME
    return config(username=username, password=password, url=url, name=name)


def fetch_openvpn_config(config):
    """
    raises requests.exceptions.RequestException
    """
    logger.info("retrieving config from %s with username %s password %s..." % (config.url,
                                                                               config.username,
                                                                               '*' * len(config.password)))
    r = requests.get(config.url, auth=(config.username, config.password))
    if r.status_code != 200:
        raise requests.exceptions.RequestException(str(r.status_code))
