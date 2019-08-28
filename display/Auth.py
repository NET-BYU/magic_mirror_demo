from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import Images as IMG
import keyboard
import json


class PinData:
    def __init__(self):
        self.pin_no = "0000"

    def update(self, topic, payload):
        try:
            topic = topic.split("/")
            if topic[1] != "pin":
                return

            self.pin_no = payload

        except Exception as e:
            print("Something happened", e)


class AuthData:
    def __init__(self):
        """
        Possible options will be OFF, ON, and UNLOCKED
        """
        self.auth_state = "OFF"

    def update(self, topic, payload):
        try:
            topic = topic.split("/")
            if topic[1] != "auth":
                return

            auth_data = json.loads(payload)
            self.auth_state = auth_data["State"]

        except Exception as e:
            print("Something happened", e)


class Auth(Gtk.Layout):
    def __init__(self, auth_data, pin_data):
        Gtk.Layout.__init__(self)

        self.auth_data = auth_data
        self.pin_data = pin_data

        self.code = Gtk.Label()
        self.instruction = Gtk.Label()
        self.arrow = Gtk.Image()

        ### ----- I need to find a way to get the unlock animation ----- ###

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        instructionbox = Gtk.VBox()
        codebox = Gtk.VBox()

        instrdesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        self.instruction.override_font(instrdesc)
        self.instruction.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        codedesc = Pango.FontDescription("AnjaliOldLipi Bold 50")
        self.code.override_font(codedesc)
        self.code.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        self.update()

        instructionbox.pack_start(self.arrow, False, False, 0)
        instructionbox.pack_start(self.instruction, False, False, 0)
        instructionbox.pack_start(self.code, False, False, 0)

        center.pack_start(instructionbox, True, False, 0)

        self.put(center, 20, 20)

    def update(self):
        if self.auth_data.auth_state == "OFF":
            self.code.set_text("")
            self.instruction.set_text("")
            self.arrow.set_from_pixbuf(IMG.blankpix)

        elif self.auth_data.auth_state == "UNLOCKED":
            self.code.set_text(self.pin_data.pin_no)
            self.instruction.set_text("Scan QR code to begin \n"
            "Enter in PIN to continue")
            self.arrow.set_from_pixbuf(IMG.arrowpix)

        elif self.auth_data.auth_state == "ON":
            print("State is on")

        return True
