from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from datetime import datetime
import Images as IMG

class TimeDate(Gtk.VBox):
    title = Gtk.Label()
    date_text = Gtk.Label()

    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.timepix)

        time = str(datetime.now().strftime("%-I:%M:%S %p "))
        date_str = str(datetime.now().strftime("%A %b %d, %Y"))

        self.title.set_text(time)
        self.date_text.set_text(date_str)

        timedesc = Pango.FontDescription("AnjaliOldLipi Bold 130")
        self.title.override_font(timedesc)
        self.title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        datedesc = Pango.FontDescription("AnjaliOldLipi Bold 60")
        self.date_text.override_font(datedesc)
        self.date_text.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(self.title, True, False, 0)
        center.pack_start(self.date_text, True, False, 0)

        self.add(center)

    def update_clock(self):
        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.timepix)

        time = str(datetime.now().strftime("%-I:%M:%S %p"))
        date_str = str(datetime.now().strftime("%A %b %-d, %Y"))

        self.title.set_text(time)
        self.date_text.set_text(date_str)
        return True
