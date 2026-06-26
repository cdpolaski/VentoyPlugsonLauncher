#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GdkPixbuf, GLib
from drive_detector import get_ventoy_drives
from launcher import launch_plugson
import os
import socket
import webbrowser


class VentoyManager(Gtk.Window):

    def wait_for_plugson(self):

        try:
            with socket.create_connection(("127.0.0.1", 24681), timeout=1):
                webbrowser.open("http://127.0.0.1:24681")
                return False

        except OSError:
            return True

    def __init__(self):

        Gtk.Window.__init__(
            self,
            title="Ventoy Plugson Launcher v1.0"
        )

        self.set_default_size(560, 260)
        self.set_border_width(15)

        grid = Gtk.Grid()
        grid.set_row_spacing(12)
        grid.set_column_spacing(12)
        self.add(grid)

        # -------------------------
        # Logo
        # -------------------------

        icon_path = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "VentoyLogo.png"
        )

        if os.path.exists(icon_path):

            self.set_icon_from_file(icon_path)

            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                icon_path,
                64,
                64,
                True
            )

            image = Gtk.Image.new_from_pixbuf(pixbuf)

            grid.attach(image, 0, 0, 1, 2)

        # -------------------------
        # Title
        # -------------------------

        title = Gtk.Label()

        title.set_markup(
            "<span size='x-large'><b>Ventoy Plugson Launcher</b></span>"
        )

        title.set_xalign(0)

        grid.attach(title, 1, 0, 3, 1)

        # -------------------------
        # Status
        # -------------------------

        self.status = Gtk.Label()

        self.status.set_text("Status: Ready")
        self.status.set_xalign(0)

        grid.attach(self.status, 1, 1, 3, 1)

        # -------------------------
        # Device
        # -------------------------

        label = Gtk.Label(label="Ventoy Device:")
        label.set_xalign(0)

        grid.attach(label, 0, 2, 1, 1)

        self.combo = Gtk.ComboBoxText()

        grid.attach(self.combo, 1, 2, 3, 1)

        # -------------------------
        # Buttons
        # -------------------------

        refresh = Gtk.Button(label="Refresh")
        refresh.connect("clicked", self.refresh_devices)

        self.start = Gtk.Button(label="Launch Plugson")
        self.start.connect("clicked", self.on_launch_plugson)

        exitbtn = Gtk.Button(label="Exit")
        exitbtn.connect("clicked", Gtk.main_quit)

        grid.attach(refresh, 0, 3, 1, 1)
        grid.attach(self.start, 1, 3, 1, 1)
        grid.attach(exitbtn, 2, 3, 1, 1)

        # Populate devices after
        # every widget exists.
        self.refresh_devices(None)

    # -------------------------------------

    def refresh_devices(self, button):

        self.combo.remove_all()

        drives = get_ventoy_drives()

        if not drives:

            self.combo.append_text("No Ventoy device detected")
            self.combo.set_active(0)

            self.status.set_text(
                "Status: No Ventoy devices found"
            )

            self.start.set_sensitive(False)

            return

        for drive in drives:

            self.combo.append_text(
                f"{drive['model']} ({drive['size']})"
            )

        self.combo.set_active(0)

        self.status.set_text(
            f"Status: {len(drives)} Ventoy device(s) detected"
        )

        self.start.set_sensitive(True)

    def on_launch_plugson(self, button):

        index = self.combo.get_active()

        if index < 0:
            return

        drives = get_ventoy_drives()

        if index >= len(drives):
            return

        device = drives[index]["path"]

        # If Plugson is already running,
        # just open the browser.
        try:
            with socket.create_connection(("127.0.0.1", 24681), timeout=1):
                webbrowser.open("http://127.0.0.1:24681")
                return
        except OSError:
            pass

        print(f"Selected device: {device}")

        launch_plugson(device)

        GLib.timeout_add(500, self.wait_for_plugson)

win = VentoyManager()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
