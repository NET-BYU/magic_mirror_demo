from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from datetime import datetime
import Images as IMG


class Home(Gtk.VBox):
    def __init__(self, weather_data, calendar_data):
        Gtk.VBox.__init__(self)

        self.cal_data = calendar_data
        self.weather_data = weather_data

        self.weather_img = Gtk.Image()
        self.weather_temp = Gtk.Label()

        self.cal_img = Gtk.Image()
        self.cal_time = Gtk.Label()
        self.cal_title = Gtk.Label()

        self.timedate_time = Gtk.Label()
        self.timedate_date = Gtk.Label()

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        weatherbox = Gtk.HBox()
        eventbox = Gtk.HBox()
        eventdesc = Gtk.VBox()
        timebox = Gtk.VBox()
        statusbar = Gtk.HBox()

        self.weather_img.set_from_pixbuf(self.weather_data.image)
        self.cal_img.set_from_pixbuf(IMG.home_calendarpix)


        desc = Pango.FontDescription("AnjaliOldLipi Bold 15")
        self.weather_temp.override_font(desc)
        self.weather_temp.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.cal_time.override_font(desc)
        self.cal_time.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.cal_title.override_font(desc)
        self.cal_title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.timedate_date.override_font(desc)
        self.timedate_date.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.timedate_time.override_font(desc)
        self.timedate_time.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        self.update_home()

        weatherbox.pack_start(self.weather_img, False, False, 0)
        weatherbox.pack_start(self.weather_temp, False, False, 0)

        timebox.pack_start(self.timedate_time, False, False, 0)
        timebox.pack_start(self.timedate_date, False, False, 0)

        eventdesc.pack_start(self.cal_title, False, False, 0)
        eventdesc.pack_start(self.cal_time, False, False, 0)
        eventbox.pack_start(self.cal_img, False, False, 0)
        eventbox.pack_start(eventdesc, False, False, 0)

        statusbar.pack_start(eventbox, True, True, 0)
        statusbar.pack_start(timebox, True, True, 0)
        statusbar.pack_start(weatherbox, True, True, 0)

        center.pack_end(statusbar, False, False, 0)

        self.add(center)

    def update_home(self):
        self.timedate_date.set_text(str(datetime.now().strftime("%A %b %d, %Y")))
        self.timedate_time.set_text(str(datetime.now().strftime("%-I:%M %p ")))

        self.weather_temp.set_text(f"{round(self.weather_data.temperature, 1)} °F")
        self.weather_img.set_from_pixbuf(self.weather_data.status_image)

        self.cal_time.set_text(str(list(self.cal_data.events.keys())))
        self.cal_title.set_text(str(list(self.cal_data.events.keys())))

        return True
