from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk


class Mirror(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
