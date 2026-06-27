# Ventoy Plugson Launcher

A lightweight GTK3 desktop application that makes launching **Ventoy Plugson** on Linux quick, simple, and convenient.

Instead of opening a terminal and manually launching Plugson, Ventoy Plugson Launcher provides a native desktop interface that detects your Ventoy USB drive and starts Plugson with a single click.

![Ventoy Plugson Launcher](assets/ventoy-plugson-launcher.png)

---

## Features

* 🔍 Automatically detects connected Ventoy USB devices
* 🚀 Launches Ventoy Plugson with administrator privileges
* 🌐 Automatically opens Plugson in your default web browser
* 🔄 Detects an already running Plugson server
* 🖥 Native GTK3 desktop interface
* 📋 Desktop menu integration
* 📦 Debian package available

---

## Requirements

* Linux
* Python 3
* GTK3 (PyGObject)
* Ventoy 1.0 or later

---

## Installation

### Debian Package

Download the latest release from the **Releases** page and install it with:

```bash
sudo apt install ./ventoy-plugson-launcher_1.0.0-1_all.deb
```

### Run from Source

```bash
python3 main.py
```

---

## Usage

1. Connect a Ventoy USB drive.
2. Launch **Ventoy Plugson Launcher**.
3. Select your Ventoy device.
4. Click **Launch Plugson**.
5. Your default web browser will automatically open the Plugson interface.

---

## Screenshots

*Coming soon.*

---

## License

This project is licensed under the MIT License.
