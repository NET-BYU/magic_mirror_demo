from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import Images as IMG


class QuoteData():
    def __init__(self):
        self.text = "TEXT"
        self.author = "AUTHOR"

    def update(self, topic, payload):
        topic = str(topic).split('/')
        if topic[1] == "quote":
            print("Incoming from Quotes")
            if topic[2] == "text":
                self.text = str(payload.decode("utf-8"))
            elif topic[2] == "author":
                self.author = str(payload.decode("utf-8"))
                

class Quote(Gtk.VBox):
    def __init__(self, quote_data):
        Gtk.VBox.__init__(self)

        self.quote_data = quote_data
        self.text = Gtk.Label()
        self.author = Gtk.Label()
        self.count = 0

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.quotepix)


        # text.set_label(self.text)

        self.update()
        # text.set_text(self.quote_data.text)
        # author.set_text("~ " + self.quote_data.author + " ~")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        self.text.override_font(tempdesc)
        self.text.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.text.set_line_wrap(True)
        # text.set_justify(Gtk.Justification.CENTER)

        authordesc = Pango.FontDescription("AnjaliOldLipi Bold Italic 20")
        self.author.override_font(authordesc)
        self.author.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        # author.set_line_wrap(True)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(self.text, True, False, 0)
        center.pack_start(self.author, True, False, 0)
        self.add(center)

    def update(self):
        self.text.set_text(self.quote_data.text)
        self.author.set_text("~ " + self.quote_data.author + " ~" + str(self.count))
        self.count+=1
        return True
