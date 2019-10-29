#!/bin/sh
ls /dev/sd? | LANG=C xargs -I DISK sudo fdisk -l DISK 2> /dev/null | grep "Linux swap" | cut -d ' ' -f1 | xargs sudo swapon -p 0

