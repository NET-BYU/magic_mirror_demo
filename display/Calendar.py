from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

import Images as IMG
import json


class EventData:
    def __init__(self):
        self.events = {}
        self.updated = False

    def update(self, topic, payload):
        try:
            topic = topic.split("/")
            if topic[1] != "event":
                return

            new_events = json.loads(payload)
            self.events = {event['Title']: event for event in new_events}
            self.updated = True

        except Exception as e:
            print("Something happened", e)


class Event(Gtk.VBox):
    def __init__(self, event_data):
        Gtk.VBox.__init__(self)
        self.event_data = event_data

        self.title = self.event_data["Title"]
        self.time = self.event_data["Time"]
        self.location = self.event_data["Location"]

        self.title_label = Gtk.Label()
        self.time_label = Gtk.Label()
        self.location_label = Gtk.Label()

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        titledesc = Pango.FontDescription("AnjaliOldLipi Bold 35")
        self.title_label.override_font(titledesc)
        self.title_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        datedesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        self.time_label.override_font(datedesc)
        self.time_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        locdesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        self.location_label.override_font(locdesc)
        self.location_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        self.title_label.set_text(self.title)
        self.location_label.set_text(self.location)
        self.time_label.set_text(self.time)

        center.pack_start(self.title_label, True, False, 0)
        center.pack_start(self.location_label, True, False, 0)
        center.pack_start(self.time_label, True, False, 0)

        self.add(center)

    def update_event_data(self, event_data):
        self.title = event_data["Title"]
        self.time = event_data["Time"]
        self.location = event_data["Location"]

    def update_event(self):
        self.title_label.set_text(self.title)
        self.location_label.set_text(self.location)
        self.time_label.set_text(self.time)

        return True


class Calendar(Gtk.VBox):
    def __init__(self, calendar_data):
        Gtk.VBox.__init__(self)

        self.calendar_data = calendar_data

        self.event_stack = Gtk.Stack()

        self.state = []

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

        self.update_events()

        event_space.pack_start(self.event_stack, True, False, 0)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(up_image, True, False, 0)
        center.pack_start(event_space, True, False, 0)
        center.pack_start(down_image, True, False, 0)
        self.add(center)

    def update_events(self):
        if self.calendar_data.updated == False:
            return True

        print("Contents Before:")
        for event in self.event_stack:
            print(event.position)
        print("Cal Data", self.calendar_data.events)

        # Remove old events from stack
        removed_events = []
        for event_object in self.event_stack:
            event_title = event_object.title
            print("Title:", event_title)
            if event_title not in self.calendar_data.events:
                removed_events.append(event_object)
        for event_object in removed_events:
            self.event_stack.remove(event_object)
            print("Removed event", event_object.title)

        # Adds new events to stack
        for event_title, event in self.calendar_data.events.items():
            event_object = self.event_stack.get_child_by_name(event_title)
            if event_object is None:
                print("New Object Added", event_title)
                self.event_stack.add_named(Event(event), event_title)

        # Handles Updated Events
        for event_title, event in self.calendar_data.events.items():
            event_object = self.event_stack.get_child_by_name(event_title)
            event_object.update_event_data(event)
            event_object.update_event()

        # Redraw stack
        self.event_stack.show_all()
        self.calendar_data.updated = False

        print("Contents After:")
        for event in self.event_stack:
            print(len(self.event_stack.get_children()))

        return True
