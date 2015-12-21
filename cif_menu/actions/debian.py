import os
from collections import namedtuple
import requests
import logging


DEFAULT_GEN_URL = "https://vpn.tuxed.net/vpn-user-portal/"
DEFAULT_USERNAME = "foo"
DEFAULT_PASSWORD = "bar"
DEFAULT_NAME = "sensor_1"
DEFAULT_FETCH_URL = "https://vpn.tuxed.net/vpn-user-portal/%s/ovpn" % DEFAULT_NAME


logger = logging.getLogger(__name__)

ALL_ENV = ['SENSOR_GEN_URL', 'SENSOR_FETCH_URL', 'SENSOR_USERNAME', 'SENSOR_PASSWORD', 'SENSOR_NAME']


config = namedtuple('config', ['username', 'password', 'gen_url', 'fetch_url', 'name'])


def get_config():
    """
    Tries to get config from environment variables, if not set will use default values from this file.

    return: config namedtuple
    """
    username = os.environ.get("SENSOR_USERNAME", DEFAULT_USERNAME)
    password = os.environ.get("SENSOR_PASSWORD", DEFAULT_PASSWORD)
    gen_url = os.environ.get("SENSOR_GEN_URL", DEFAULT_GEN_URL)
    fetch_url = os.environ.get("SENSOR_FETCH_URL", DEFAULT_FETCH_URL)
    name = os.environ.get("SENSOR_NAME", DEFAULT_NAME)
    return config(username=username, password=password, gen_url=gen_url, fetch_url=fetch_url, name=name)


def gen_remote_openvpn_config(config):
    """
    raises requests.exceptions.RequestException
    """
    logger.info("Generating remote config on %s with username %s password %s..." % (config.gen_url,
                                                                                    config.username,
                                                                                    '*' * len(config.password)))
    r = requests.get(config.url, auth=(config.username, config.password), data={'name': config.name})
    if r.status_code != 200:
        raise requests.exceptions.RequestException(str(r.status_code))


def fetch_openvpn_config(config):
    """
    raises requests.exceptions.RequestException
    """
    logger.info("retrieving config from %s with username %s password %s..." % (config.fetch_url,
                                                                               config.username,
                                                                               '*' * len(config.password)))
    r = requests.get(config.fetch_url, auth=(config.username, config.password))
    if r.status_code != 200:
        raise requests.exceptions.RequestException(str(r.status_code))
