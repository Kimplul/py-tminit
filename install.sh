#!/bin/sh

if [ "$1" = "remove" ]
then
        rm /usr/bin/tminit.py
        rm /etc/udev/rules.d/99-tm.rules
else
        # Just place tminit.py into /usr/bin and 99-tm.rules into /etc/udev.rules.d
        install tminit.py /usr/bin
        cp 99-tm.rules /etc/udev/rules.d
fi
