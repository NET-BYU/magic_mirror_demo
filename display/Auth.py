from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk
import Images as IMG


class Auth(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()

        # self.update()

        center.pack_start(logo_image, True, False, 0)
        self.add(center)

    def update(self):
        pass
