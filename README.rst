
CIF menu
========

This is the configuration frontend for the CIF sensor probe. It should be installed inside the sensor.


Assumes root privileges.


Should eventually run as a systemd terminal.


For development running this in a docker container is quite useful, see Makefile and Dockerfile.


Installation
------------

::

    $ pip install .



Customization
-------------

You can manipulate the default config variables by setting these environment variables:

 * **DEFAULT_GEN_URL** - URL used for generating a configuration
 * **DEFAULT_FETCH_URL** - URL for fetching openvpn configuration
 * **DEFAULT_USERNAME** - username used for URL authentication
 * **DEFAULT_PASSWORD** - password used for URL authentication
 * **DEFAULT_NAME** - name of the probe
