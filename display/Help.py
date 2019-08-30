from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import Images as IMG


class Help(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.helppix)

        title = Gtk.Label()
        description = Gtk.Label()
        helptext = Gtk.Label()

        title.set_text("Help")
        description.set_text("BYU's Magic Mirror is an IoT project that depends on the following processes located at "
                             "immerse-iot.byu.edu:\n"
                             "- Quote API [client_location] which refreshes every 10m or upon request\n"
                             "- Message API [client_location] which refreshes every time a message is sent or upon "
                             "request\n"
                             "- Weather API [client_location] which refreshes every 10m or upon request\n"
                             "- Calendar API [client_location] which refreshes every day or upon request\n"
                             "all pushing messages via MQTT publishers and clients to postman.cloudmqtt.com\n")
        helptext.set_text("[h]\t\t or House returns user to Home Screen\n"
                          "[t]\t\t or Clock shows user time and date\n"
                          "[q]\t\t or Quotation Mark shows a random quote\n"
                          # "[m]\t\t or <equivalent gesture> shows the message queue\n"
                          "[w]\t\t or Sun and Cloud shows the weather\n"
                          "[c]\t\t or Calendar shows the calendar events\n"
                          "[F1]\t\t or Question Mark shows this help screen\n"
                          "[i]\t\t or Info Circle shows the About screen\n"
                          "[n]\t\t shows a blank screen for mirror purposes\n"
                          "[Left]\t\t cycles through app screens forwards\n"
                          "[Right]\t\t cycles through app screens backwards\n"
                          "[Up]\t\t cycles through calendar events\n"
                          "[Down]\t\t cycles through calendar events\n"
                          " \n"
                          "For any other technical/development aspect of this project, please refer to the wiki at\n "
                          "http://immerse.byu.edu/InteractiveDisplays/dokuwiki/doku.php?id=demo_info:iot:start\n")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        descriptdesc = Pango.FontDescription("Ubuntu Mono Italic 18")
        description.override_font(descriptdesc)
        description.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        description.set_line_wrap(True)

        helpdesc = Pango.FontDescription("Ubuntu Mono 18")
        helptext.override_font(helpdesc)
        helptext.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        # help.set_line_wrap(True)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(description, True, False, 0)
        center.pack_start(helptext, True, False, 0)
        self.add(center)
