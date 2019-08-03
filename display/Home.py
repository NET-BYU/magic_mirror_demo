from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from datetime import datetime
from dateutil import tz
from time import sleep, time
import Images as IMG


class Home(Gtk.VBox):
    def __init__(self, weather, temp, unread, cal_event):
        Gtk.VBox.__init__(self)

        self.weather = weather
        self.temp = temp
        self.unread = unread
        self.cal_event = cal_event

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        weatherbox = Gtk.HBox()
        messagebox = Gtk.HBox()
        status_bar = Gtk.HBox()

        weather_image = Gtk.Image()
        message_image = Gtk.Image()

        weather_image.set_from_pixbuf(self.weather)
        if int(self.unread) == 1:
            message_image.set_from_pixbuf(IMG.status_message_sing_pix)
        elif int(self.unread) > 1:
            message_image.set_from_pixbuf(IMG.status_message_plu_pix)

        time = str(datetime.now().strftime("%-I:%M %p "))
        date_str = str(datetime.now().strftime("%A %b %d, %Y"))

        time_label = Gtk.Label()
        date_label = Gtk.Label()
        temp_label = Gtk.Label()
        messages_label = Gtk.Label()
        calendar_label = Gtk.Label()

        time_label.set_text(time)
        date_label.set_text(date_str)
        temp_label.set_text("TEMP")
        messages_label.set_text("1")
        calendar_label.set_text("EVENT")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        time_label.override_font(tempdesc)
        time_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_end(time_label, False, True, 0)
        self.add(center)
