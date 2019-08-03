from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import Images as IMG


class Messages(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.messagespix)

        title = Gtk.Label()
        title.set_text("Messages")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        self.add(center)
