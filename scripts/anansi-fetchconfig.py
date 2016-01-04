#!/usr/bin/env python3

import os
import logging
from anansi_menu.actions.debian import fetch_openvpn_config
from anansi_menu.actions import get_config, fetch_openvpn_config

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    config = get_config()

    for i in os.environ.items():
        print i

    print fetch_openvpn_config(config)
