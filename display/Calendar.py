from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

import Images as IMG


class Calendar(Gtk.VBox):
    def __init__(self, t1, t2, t3, t4, d1, d2, d3, d4, l1, l2, l3, l4):
        Gtk.VBox.__init__(self)

        self.title_1 = t1
        self.title_2 = t2
        self.title_3 = t3
        self.title_4 = t4

        self.date_1 = d1
        self.date_2 = d2
        self.date_3 = d3
        self.date_4 = d4

        self.loc_1 = l1
        self.loc_2 = l2
        self.loc_3 = l3
        self.loc_4 = l4

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        event_space = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.calendarpix)

        up_image = Gtk.Image()
        down_image = Gtk.Image()
        up_image.set_from_pixbuf(IMG.uppix)
        down_image.set_from_pixbuf(IMG.downpix)

        title = Gtk.Label()
        title.set_text("Calendar")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        event_title = Gtk.Label()
        event_date = Gtk.Label()
        event_location = Gtk.Label()

        titledesc = Pango.FontDescription("AnjaliOldLipi Bold 35")
        event_title.override_font(titledesc)
        event_title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        datedesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        event_date.override_font(datedesc)
        event_date.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        locdesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        event_location.override_font(locdesc)
        event_location.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        event_title.set_text(self.title_1)
        event_date.set_text(self.date_1)
        event_location.set_text("@ " + self.loc_1)

        event_space.pack_start(event_title, True, False, 0)
        event_space.pack_start(event_date, True, False, 0)
        event_space.pack_start(event_location, True, False, 0)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(up_image, True, False, 0)
        center.pack_start(event_space, True, False, 0)
        center.pack_start(down_image, True, False, 0)
        self.add(center)

    def on_key(self, event):
        if event.keyval == Gdk.KEY_Up:
            print("banana")
