#!/usr/bin/env python3

import subprocess
import json


def get_device_info(device_name):

    result = subprocess.run(
        [
            "lsblk",
            "-J",
            "-o",
            "NAME,SIZE,FSTYPE,MOUNTPOINT,TRAN"
        ],
        capture_output=True,
        text=True
    )

    data = json.loads(result.stdout)

    for device in data["blockdevices"]:

        if device["name"] == device_name:

            return {
                "device": "/dev/" + device["name"],
                "size": device["size"],
                "filesystem": device.get("fstype") or "Unknown",
                "mountpoint": device.get("mountpoint") or "Not Mounted",
                "connection": device.get("tran") or "Unknown"
            }

    return None


if __name__ == "__main__":

    info = get_device_info("sdb")

    print(info)
