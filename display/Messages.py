from gi import require_version
require_version('Gtk', '3.0')
from collections import deque
from datetime import datetime
from gi.repository import Gtk, Gdk, Pango
import Images as IMG


class MessageData:
    def __init__(self):
        self.messages = deque(["a", "", "a", "", "a", "", "a", "", "a", ""])

    def update(self, topic, payload):
        try:
            topic = topic.split("/")
            if topic[1] != "messages":
                return

            data = json.loads(payload)
            self.messages.popleft()
            self.messages.append('{} {}'.format(data["message"], datetime.now().strftime("%-I:%M:%S %p ")))
        except Exception as e:
            print("Something happened", e)


class Messages(Gtk.VBox):
    def __init__(self, message_data):
        Gtk.VBox.__init__(self)
        self.message_data = message_data

        self.mes_0 = Gtk.Label()
        self.mes_1 = Gtk.Label()
        self.mes_2 = Gtk.Label()
        self.mes_3 = Gtk.Label()
        self.mes_4 = Gtk.Label()
        self.mes_5 = Gtk.Label()
        self.mes_6 = Gtk.Label()
        self.mes_7 = Gtk.Label()
        self.mes_8 = Gtk.Label()
        self.mes_9 = Gtk.Label()

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

        messagedesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        self.mes_0.override_font(messagedesc)
        self.mes_0.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_1.override_font(messagedesc)
        self.mes_1.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_2.override_font(messagedesc)
        self.mes_2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_3.override_font(messagedesc)
        self.mes_3.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_4.override_font(messagedesc)
        self.mes_4.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_5.override_font(messagedesc)
        self.mes_5.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_6.override_font(messagedesc)
        self.mes_6.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_7.override_font(messagedesc)
        self.mes_7.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_8.override_font(messagedesc)
        self.mes_8.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.mes_9.override_font(messagedesc)
        self.mes_9.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        self.update_screen()

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(self.mes_0, True, False, 0)
        center.pack_start(self.mes_1, True, False, 0)
        center.pack_start(self.mes_2, True, False, 0)
        center.pack_start(self.mes_3, True, False, 0)
        center.pack_start(self.mes_4, True, False, 0)
        center.pack_start(self.mes_5, True, False, 0)
        center.pack_start(self.mes_6, True, False, 0)
        center.pack_start(self.mes_7, True, False, 0)
        center.pack_start(self.mes_8, True, False, 0)
        center.pack_start(self.mes_9, True, False, 0)
        self.add(center)

    def update_screen(self):
        self.mes_0.set_text(self.message_data.messages[0])
        self.mes_1.set_text(self.message_data.messages[1])
        self.mes_2.set_text(self.message_data.messages[2])
        self.mes_3.set_text(self.message_data.messages[3])
        self.mes_4.set_text(self.message_data.messages[4])
        self.mes_5.set_text(self.message_data.messages[5])
        self.mes_6.set_text(self.message_data.messages[6])
        self.mes_7.set_text(self.message_data.messages[7])
        self.mes_8.set_text(self.message_data.messages[8])
        self.mes_9.set_text(self.message_data.messages[9])

        return True
