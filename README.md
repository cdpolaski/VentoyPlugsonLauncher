# Ventoy Plugson Launcher

A lightweight GTK3 desktop application for launching Ventoy Plugson on Linux.

## Features

- Automatically detects Ventoy USB drives
- Launches Plugson with pkexec
- Automatically opens Plugson in your web browser
- Detects an already-running Plugson server
- Uses the official Ventoy logo
- Simple GTK3 graphical interface

## Requirements

- Python 3
- GTK3 (PyGObject)
- pkexec (polkit)
- Ventoy

## Project Structure

```
VentoyPlugsonLauncher/
├── assets/
│   └── VentoyLogo.png
├── desktop/
│   └── ventoy-plugson-launcher.desktop
├── config.py
├── drive_detector.py
├── launcher.py
├── main.py
├── run_plugson.sh
└── README.md
```

## Installation

Clone or download the project.

Launch the application with:

```bash
python3 main.py
```

## License

MIT License
