import unittest
import os
import requests

import anansi_menu.actions


def cleanup_env():
    """make sure no env vars are set"""
    for e in anansi_menu.actions.ALL_ENV:
        if e in os.environ:
            del os.environ[e]


class TestCleanup(unittest.TestCase):
    def test_cleanup(self):
        for e in anansi_menu.actions.ALL_ENV:
            os.environ[e] = "test_cleanup"
        cleanup_env()
        for e in anansi_menu.actions.ALL_ENV:
            self.assertFalse(e in os.environ)


class TestActions(unittest.TestCase):
    def setUp(self):
        cleanup_env()

    def testGetConfig(self):
        config = anansi_menu.actions.get_config()
        self.assertEqual(config.url, anansi_menu.actions.DEFAULT_URL)
        self.assertEqual(config.name, anansi_menu.actions.DEFAULT_NAME)
        self.assertEqual(config.username, anansi_menu.actions.DEFAULT_USERNAME)
        self.assertEqual(config.password, anansi_menu.actions.DEFAULT_PASSWORD)

    def testGetConfigWithEnv(self):
        custom_url = 'http://custom_url'
        custom_username = 'custom_username'
        custom_password = 'custom_password'
        custom_name = 'custom_name'

        os.environ['SENSOR_URL'] = custom_url
        os.environ['SENSOR_USERNAME'] = custom_username
        os.environ['SENSOR_PASSWORD'] = custom_password
        os.environ['SENSOR_NAME'] = custom_name

        config = anansi_menu.actions.get_config()

        self.assertEqual(config.url, custom_url)
        self.assertEqual(config.name, custom_name)
        self.assertEqual(config.username, custom_username)
        self.assertEqual(config.password, custom_password)

    def testGetOpenVpnConfig(self):
        config = anansi_menu.actions.get_config()

        # should not work with default settings
        self.assertRaises(requests.exceptions.RequestException, anansi_menu.actions.fetch_openvpn_config, config)


if __name__ == '__main__':
    unittest.main()
