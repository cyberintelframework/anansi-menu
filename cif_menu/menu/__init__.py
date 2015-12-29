#! /usr/bin/env python3

import locale
from dialog import Dialog


def openvpn(d):
    code, tag = d.menu("What OpenVPN thing do you want to do?:",
                            choices=[
                                ("config", "Manage configuration"),
                                ("fetch", "Fetch latest config"),
                                ("restart", "Restart OpenVPN daemon"),
                            ])
    if code == d.OK:
        if tag == "config":
            pass
        elif tag == "fetch":
            pass
        elif tag == "restart":
            pass
    else:
        exit()


def update(d):
    return


def restart(d):
    if d.yesno("Are you sure you want to restart?") == d.OK:
        print("restarting...")
        exit(0)
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
    d.set_background_title("Cyber Intel Framework")
    while True:
        mainmenu(d)


if __name__ == '__main__':
    main()
