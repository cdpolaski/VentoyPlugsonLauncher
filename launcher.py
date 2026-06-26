#!/usr/bin/env python3

import os
import subprocess
import socket
import time
import webbrowser

from config import get_ventoy_path


def launch_plugson(device):

    ventoy_path = get_ventoy_path()

    if ventoy_path is None:
        print("Ventoy installation not configured.")
        return False

    script = os.path.join(ventoy_path, "VentoyPlugson.sh")

    if not os.path.exists(script):
        print("VentoyPlugson.sh not found.")
        return False

    print(f"Launching Plugson for {device}")

    command = (
        f'cd "{ventoy_path}" && '
        f'./VentoyPlugson.sh {device}'
    )

    subprocess.Popen(
        [
            "pkexec",
            "bash",
            "-c",
            command
        ]
    )

    return True


if __name__ == "__main__":

    launch_plugson("/dev/sdc")
