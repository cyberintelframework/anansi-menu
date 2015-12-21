import unittest
import os
import requests
from cif_menu.actions import debian



def cleanup_env():
    """make sure no env vars are set"""
    for e in debian.ALL_ENV:
        if e in os.environ:
            del os.environ[e]


class TestCleanup(unittest.TestCase):
    def test_cleanup(self):
        for e in debian.ALL_ENV:
            os.environ[e] = "test_cleanup"
        cleanup_env()
        for e in debian.ALL_ENV:
            self.assertFalse(e in os.environ)


class TestDebian(unittest.TestCase):
    def setUp(self):
        cleanup_env()

    def testGetConfig(self):
        config = debian.get_config()
        self.assertEqual(config.url, debian.DEFAULT_URL)
        self.assertEqual(config.name, debian.DEFAULT_NAME)
        self.assertEqual(config.username, debian.DEFAULT_USERNAME)
        self.assertEqual(config.password, debian.DEFAULT_PASSWORD)

    def testGetConfigWithEnv(self):
        custom_url = 'http://custom_url'
        custom_username = 'custom_username'
        custom_password = 'custom_password'
        custom_name = 'custom_name'

        os.environ['SENSOR_URL'] = custom_url
        os.environ['SENSOR_USERNAME'] = custom_username
        os.environ['SENSOR_PASSWORD'] = custom_password
        os.environ['SENSOR_NAME'] = custom_name

        config = debian.get_config()

        self.assertEqual(config.url, custom_url)
        self.assertEqual(config.name, custom_name)
        self.assertEqual(config.username, custom_username)
        self.assertEqual(config.password, custom_password)

    def testGetOpenVpnConfig(self):
        config = debian.get_config()

        # should not work with default settings
        self.assertRaises(requests.exceptions.RequestException, debian.fetch_openvpn_config, config)


if __name__ == '__main__':
    unittest.main()
