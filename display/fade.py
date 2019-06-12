import gtk
import gobject
import cairo
import sys

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Fade In")
        self.resize(300, 350)
        self.set_position(gtk.WIN_POS_CENTER)

        ## alpha is starting transparency
        self.alpha = 0
        ## delta is amount to increase alpha
        self.delta = 0.01

        self.connect("destroy", gtk.main_quit)

        self.darea = gtk.DrawingArea()
        self.darea.connect("expose-event", self.expose)
        self.add(self.darea)

        try:
            self.surface = cairo.ImageSurface.create_from_png("/usr/share/icons/gnome/256x256/emotes/face-angel.png")
        except Exception as e:
            print(e.message)
            sys.exit(1)

        self.show_all()

    def fadeImage(self):
        self.darea.queue_draw()

    def expose(self, widget, event):

        cr = widget.window.cairo_create()

        cr.set_source_surface(self.surface, 10, 10)
        cr.paint_with_alpha(self.alpha)

        self.alpha += self.delta

        if self.alpha >= 1: return False
        else: gobject.timeout_add(50,self.fadeImage)

PyApp()
gtk.main()
