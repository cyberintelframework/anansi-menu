
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

debian package::

    # echo "deb https://dl.bintray.com/anansi/anansi stable main" > /etc/apt/sources.list.d/anansi.list
    # apt-key adv --keyserver hkps.pool.sks-keyservers.net --recv-keys 7B515ADA
    # apt-get update
    # apt-get install python-anansi-menu


Customization
-------------

You can manipulate the default config variables by setting these environment variables:

 * **SENSOR_URL** - URL used for generating a configuration
 * **SENSOR_USERNAME** - username used for URL authentication
 * **SENSOR_PASSWORD** - password used for URL authentication
 * **SENSOR_NAME** - name of the probe


Release procedure
-----------------

We use travis to publish debian binaries on bintray.

https://bintray.com/anansi/anansi/anansi-menu/

developer note: Make sure the version number is correct in setup.py, descriptor.json and debian/changelog


travis
------

.. image:: https://travis-ci.org/cyberintelframework/anansi-menu.svg
    :target: https://travis-ci.org/cyberintelframework/anansi-menu
