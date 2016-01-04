#! /usr/bin/env python3

import locale
import subprocess
import os
from anansi_menu.actions import get_config, fetch_openvpn_config

from dialog import Dialog


def call(command):
    """
    run command, redirect stderr to stdout, capture stdout, don't complain
    about errors
    """
    output = subprocess.check_output(command, stderr=subprocess.STDOUT,
                                     shell=True)
    return output.decode('utf-8')



def openvpn(d):
    """
    display the OpenVPN menu
    """
    while True:
        code, tag = d.menu("What OpenVPN thing do you want to do?:",
                                choices=[
                                    ("config", "Manage configuration"),
                                    ("fetch", "Fetch latest config"),
                                    ("restart", "Restart OpenVPN daemon"),
                                ])
        c = vars(get_config())

        if code == d.OK:
            if tag == "config":
                # elemts: (label, yl, xl, item, yi, xi, field_length, input_length)
                # yl row xl column
                code, list = d.form(text="Where should we retrieve the OpenVPN config?",
                                   elements=(
                                ('username', 1, 1, c['username'], 1, 10, 16, 16),
                                ('password', 2, 1, c['password'], 2, 10, 16, 16),
                                ('name',     3, 1, c['name'],     3, 10, 16, 16),
                          ),
                       width=0, height=10, form_height=3,
                       )
                if code == d.OK:
                    c['username'], c['password'], c['name'] = list
            elif tag == "fetch":
                # TODO: replace this with changed config
                try:
                    fetch_openvpn_config(get_config())
                except Exception as e:
                    d.msgbox(str(e), width=0, height=0)
            elif tag == "restart":
                r = call("/usr/sbin/service openvpn restart; exit 0")
                d.msgbox(r, width=0, height=0)
        else:
            break


def update(d):
    """
    run the debian update commands
    """
    d.infobox("updating sensor operating system...", width=0, height=0)
    r = call("apt-get update && apt-get dist-upgrade -qy; exit 0")
    d.msgbox(r, width=0, height=0)


def restart(d):
    """
    restart the operating system
    """
    if d.yesno("Are you sure you want to restart?") == d.OK:
        print("restarting...")
        r = call("/sbin/reboot; exit 0")
        d.msgbox(r, width=0, height=0)
    else:
        return


def mainmenu(d):
    code, tag = d.menu("Where would you like to go today?:",
                            choices=[
                                ("openvpn", "Manage OpenVPN settings"),
                                ("update", "Force system update"),
                                ("restart", "Restart the sensor"),
                            ])
    if code == d.OK:
        if tag == "openvpn":
            openvpn(d)
        elif tag == "update":
            update(d)
        elif tag == "restart":
            restart(d)
    else:
        exit()


def main():
    locale.setlocale(locale.LC_ALL, '')
    d = Dialog(dialog="dialog")
    d.set_background_title("Anansi")
    while True:
        mainmenu(d)


if __name__ == '__main__':
    main()
