#!/usr/bin/env python3

import json
import os

CONFIG_DIR = os.path.join(
    os.path.expanduser("~"),
    ".config",
    "ventoy-plugson-companion"
)

CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def load_config():

    if not os.path.exists(CONFIG_FILE):
        return {}

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):

    os.makedirs(CONFIG_DIR, exist_ok=True)

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def get_ventoy_path():

    config = load_config()

    path = config.get("ventoy_path")

    if path and os.path.exists(
        os.path.join(path, "VentoyPlugson.sh")
    ):
        return path

    return None


def set_ventoy_path(path):

    config = load_config()

    config["ventoy_path"] = path

    save_config(config)


if __name__ == "__main__":

    print(get_ventoy_path())
