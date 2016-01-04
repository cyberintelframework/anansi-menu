
Anansi menu
========

This is the configuration frontend for the Anansi sensor probe. It should be
installed inside the sensor.


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

 * **SENSOR_URL** - URL used for generating a configuration
 * **SENSOR_USERNAME** - username used for URL authentication
 * **SENSOR_PASSWORD** - password used for URL authentication
 * **SENSOR_NAME** - name of the probe

