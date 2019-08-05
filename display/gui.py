from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject
from Auth import Auth
from Calendar import Calendar
from Help import Help
from Home import Home
from Info import Info
from Messages import Messages
from Mirror import Mirror
from Quote import QuoteData, Quote
from TimeDate import TimeDate
from WeatherData import WeatherData, Weather
import threading
import subscriber
import Images as IMG


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Magic Mirror")

        self.state_list = ["HOME", "WEATHER", "TIME", "MESSAGES", "QUOTE", "CALENDAR", "HELP", "INFO", "MIRROR"]
        self.state = "WEATHER"

        # Data classes which update from subscriber
        weather_data = WeatherData()
        quote_data = QuoteData()

        # Screen objects that are cycled in the window
        # self.home_screen = Home()
        self.auth_screen = Auth()
        self.weather_screen = Weather(weather_data)
        self.time_screen = TimeDate()
        self.message_screen = Messages()
        self.quote_screen = Quote(quote_data)
        # self.calendar_screen = Calendar()
        self.help_screen = Help()
        self.info_screen = Info()
        self.mirror_screen = Mirror()

        # Starts the MQTT subscriber
        data_thread = threading.Thread(target=subscriber.run, args=([weather_data, quote_data],))
        data_thread.start()

        # Updates the value on the screens in separate threads
        GObject.timeout_add(1000, self.weather_screen.update_weather)
        GObject.timeout_add(1000, self.time_screen.update_clock)
        GObject.timeout_add(1000, self.quote_screen.update)

        self.app_stack = Gtk.Stack()
        self.app_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.app_stack.set_transition_duration(500)

        self.app_stack.add_named(self.weather_screen, "Weather")
        self.app_stack.add_named(self.time_screen, "Time")
        self.app_stack.add_named(self.message_screen, "Message")
        self.app_stack.add_named(self.quote_screen, "Quote")
        self.app_stack.add_named(self.help_screen, "Help")
        self.app_stack.add_named(self.info_screen, "Info")
        self.app_stack.add_named(self.mirror_screen, "Mirror")

        # Meant to add the default screen
        self.add(self.app_stack)

        self.fullscreen()
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(255, 255, 255))
        self.set_default_size(500, 500)
        self.set_icon(IMG.iconpix)

    def do_key_press_event(self, event):
        Gtk.Window.do_key_press_event(self, event)
        if event.keyval == Gdk.KEY_Escape:
            self.unfullscreen()
        elif event.keyval == Gdk.KEY_F11:
            self.fullscreen()
        elif event.keyval == Gdk.KEY_h and self.state is not self.state_list[0]:
            self.state = "HOME"
            self.app_stack.set_visible_child_name("Home")
        elif event.keyval == Gdk.KEY_w and self.state is not self.state_list[1]:
            self.state = "WEATHER"
            self.app_stack.set_visible_child_full("Weather", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_t and self.state is not self.state_list[2]:
            self.state = "TIME"
            self.app_stack.set_visible_child_full("Time", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_m and self.state is not self.state_list[3]:
            self.state = "MESSAGES"
            self.app_stack.set_visible_child_full("Message", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_q and self.state is not self.state_list[4]:
            self.state = "QUOTE"
            self.app_stack.set_visible_child_full("Quote", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_c and self.state is not self.state_list[5]:
            self.state = "CALENDAR"
            self.app_stack.set_visible_child_full("Calendar", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_F1 and self.state is not self.state_list[6]:
            self.state = "HELP"
            self.app_stack.set_visible_child_full("Help", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_i and self.state is not self.state_list[7]:
            self.state = "INFO"
            self.app_stack.set_visible_child_full("Info", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_n and self.state is not self.state_list[8]:
            self.state = "MIRROR"
            self.app_stack.set_visible_child_full("Mirror", Gtk.StackTransitionType.CROSSFADE)
        elif event.keyval == Gdk.KEY_Left:
            if self.state_list.index(self.state) != 1:
                self.state = self.state_list[self.state_list.index(str(self.state)) - 1]
                if self.state is "WEATHER":
                    self.app_stack.set_visible_child_full("Weather", Gtk.StackTransitionType.SLIDE_RIGHT)
                elif self.state is "TIME":
                    self.app_stack.set_visible_child_full("Time", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "MESSAGES":
                    self.app_stack.set_visible_child_full("Message", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "QUOTE":
                    self.app_stack.set_visible_child_full("Quote", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "CALENDAR":
                    self.app_stack.set_visible_child_full("Calendar", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "HELP":
                    self.app_stack.set_visible_child_full("Help", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "INFO":
                    self.app_stack.set_visible_child_full("Info", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state == "MIRROR":
                    self.app_stack.set_visible_child_full("Mirror", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
            elif self.state_list.index(self.state) == 1:
                self.state = self.state_list[len(self.state_list) - 1]
                self.app_stack.set_visible_child_name("Mirror")
        elif event.keyval == Gdk.KEY_Right:
            if self.state_list.index(self.state) != len(self.state_list) - 1:
                self.state = self.state_list[self.state_list.index(str(self.state)) + 1]
                if self.state == "WEATHER":
                    self.app_stack.set_visible_child_full("Weather", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "TIME":
                    self.app_stack.set_visible_child_full("Time", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "MESSAGES":
                    self.app_stack.set_visible_child_full("Message", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "QUOTE":
                    self.app_stack.set_visible_child_full("Quote", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "CALENDAR":
                    self.app_stack.set_visible_child_full("Calendar", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "HELP":
                    self.app_stack.set_visible_child_full("Help", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "INFO":
                    self.app_stack.set_visible_child_full("Info", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
                elif self.state is "MIRROR":
                    self.app_stack.set_visible_child_full("Mirror", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
            elif self.state_list.index(self.state) == len(self.state_list) - 1:
                self.state = self.state_list[1]
                self.app_stack.set_visible_child_full("Weather", Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        elif (event.keyval == Gdk.KEY_Up) and (self.state is "CALENDAR"):
            print("derpaflerp")


def main():
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    cursor = Gdk.Cursor.new(Gdk.CursorType.BLANK_CURSOR)
    window.get_window().set_cursor(cursor)
    Gtk.main()


if __name__ == '__main__':
    main()
