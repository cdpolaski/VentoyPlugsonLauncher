#!/bin/bash

VENTOY_DIR="$1"
DEVICE="$2"

cd "$VENTOY_DIR" || exit 1

exec ./VentoyPlugson.sh "$DEVICE"
