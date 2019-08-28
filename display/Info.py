from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import Images as IMG


class Info(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.infopix)

        title = Gtk.Label()
        description = Gtk.Label()
        creators = Gtk.Label()
        maintainers = Gtk.Label()

        title.set_text("About")
        description.set_text("BYU's Magic Mirror is a project designed to showcase different IoT principles via \n"
                             "mirror apps and possible exterior applications all controlled by this unit.")
        creators.set_text("Written by:\n"
                          "Philip Lundrigan\t\t Mentoring Professor and project architect\n"
                          "Christopher Kitras\t\t Display module and graphical user interface design\n"
                          "Joseph Miera\t\t\t Input module\n"
                          "Levi Fleming\t\t\t Calendar and Messenger APIs and hardware design\n"
                          "Max Warner\t\t\t Quote API and hardware design\n"
                          "Michael Bjerregaard\t Weather API and hardware design")
        maintainers.set_text("Maintained by:\n"
                             "[2019-Present] Creators")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        descriptdesc = Pango.FontDescription("AnjaliOldLipi Bold Italic 20")
        description.override_font(descriptdesc)
        description.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        creatorsdesc = Pango.FontDescription("AnjaliOldLipi Mono 20")
        creators.override_font(creatorsdesc)
        creators.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        maintainersdesc = Pango.FontDescription("AnjaliOldLipi Mono 20")
        maintainers.override_font(maintainersdesc)
        maintainers.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(description, True, False, 0)
        center.pack_start(creators, True, False, 0)
        center.pack_start(maintainers, True, False, 0)
        self.add(center)
