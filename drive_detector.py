#!/usr/bin/env python3

import subprocess
import json

DEVICE_NAMES = {
    "ESD-S1C": "ROG Arion External SSD",
    "CT1000MX500SSD1": "Crucial MX500",
}


def friendly_name(model):
    model = model.strip()
    return DEVICE_NAMES.get(model, model if model else "Unknown USB Device")


def is_ventoy(device):
    children = device.get("children", [])
    labels = {part.get("label") for part in children if part.get("label")}
    return "Ventoy" in labels and "VTOYEFI" in labels


def get_ventoy_drives():

    result = subprocess.run(
        [
            "lsblk",
            "-J",
            "-o",
            "NAME,SIZE,MODEL,TRAN,TYPE,LABEL"
        ],
        capture_output=True,
        text=True
    )

    data = json.loads(result.stdout)

    drives = []

    for device in data["blockdevices"]:

        if device["type"] != "disk":
            continue

        if device.get("tran") != "usb":
            continue

        if not is_ventoy(device):
            continue

        drives.append({
            "device": device["name"],                  # sdc
            "path": "/dev/" + device["name"],          # /dev/sdc
            "model": friendly_name(device.get("model", "")),
            "size": device["size"]
        })

    return drives


if __name__ == "__main__":

    for drive in get_ventoy_drives():

        print(drive)
