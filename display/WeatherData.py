from gi import require_version

require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from datetime import datetime
from time import time
import Images as IMG
import json

icon_map = {
    "01d": IMG.cleardaypix,
    "01n": IMG.clearnightpix,
    "02d": IMG.cloudsdaypix,
    "02n": IMG.cloudsnightpix,
    "03d": IMG.brokencloudspix,
    "03n": IMG.brokencloudspix,
    "04d": IMG.brokencloudspix,
    "04n": IMG.brokencloudspix,
    "09d": IMG.showerspix,
    "09n": IMG.showerspix,
    "10d": IMG.rainpix,
    "10n": IMG.rainpix,
    "11d": IMG.thunderstormpix,
    "11n": IMG.thunderstormpix,
    "13d": IMG.snowpix,
    "13n": IMG.snowpix,
    "50d": IMG.mistpix,
    "50n": IMG.mistpix,
}

home_icon_map = {
    "01d": IMG.status_cleardaypix,
    "01n": IMG.status_clearnightpix,
    "02d": IMG.status_cloudsdaypix,
    "02n": IMG.status_cloudsnightpix,
    "03d": IMG.status_brokencloudspix,
    "03n": IMG.status_brokencloudspix,
    "04d": IMG.status_brokencloudspix,
    "04n": IMG.status_brokencloudspix,
    "09d": IMG.status_showerspix,
    "09n": IMG.status_showerspix,
    "10d": IMG.status_rainpix,
    "10n": IMG.status_rainpix,
    "11d": IMG.status_thunderstormpix,
    "11n": IMG.status_thunderstormpix,
    "13d": IMG.status_snowpix,
    "13n": IMG.status_snowpix,
    "50d": IMG.status_mistpix,
    "50n": IMG.status_mistpix,
}


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset


def time_field_get(time_event):
    certain_time = time_event.split(':')
    hour = ""
    minute_day = ""
    minute = ""
    time_of_day = ""
    for item in range(len(certain_time)):
        if item == 0:
            hour = certain_time[item]
        elif item == 1:
            minute_day = certain_time[item]
    minute_day = minute_day.split()
    for item in range(len(minute_day)):
        if item == 0:
            minute = minute_day[item]
        elif item == 1:
            time_of_day = minute_day[item]
    if time_of_day == "PM":
        hour = int(hour) + 12

    return hour, minute


class WeatherData:
    def __init__(self):
        self.count = 0
        self.temperature = 0
        self.condition = "COND"
        self.sunrise = "RISE"
        self.sunset = "SET"
        self.cloudiness = "CLOUD"
        self.wind = "WIND"
        self.humidity = "HUMID"
        self.image = IMG.logopix
        self.status_image = IMG.logopix
        self.gid = "GID"
        self.time_of_day = "DAY"

    def update(self, topic, payload):
        try:
            topic = topic.split('/')
            if topic[1] != "Weather":
                return
            if topic[2] != "Update":
                return

            data = json.loads(payload)
            icon = data["icon"]
            self.temperature = data["temp"]
            self.humidity = data["humidity"]

            self.sunrise = data["sunrise"]
            self.sunset = data["sunset"]

            sunrise = datetime_from_utc_to_local(datetime.utcfromtimestamp(self.sunrise))
            self.sunrise = sunrise.strftime("%-I:%M %p ")

            sunset = datetime_from_utc_to_local(datetime.utcfromtimestamp(self.sunset))
            self.sunset = sunset.strftime("%-I:%M %p ")

            self.cloudiness = data["cloud_cover"]
            self.wind = data["wind_speed"]
            self.condition = data["description"].title()
            self.image = icon_map.get(icon, IMG.logopix)
            self.status_image = home_icon_map.get(icon, IMG.logopix)

        except Exception as e:
            print("Something happened", e)


class Weather(Gtk.Layout):
    __gtype_name__ = 'Weather'

    def __init__(self, weather_data):
        Gtk.Layout.__init__(self)
        self.set_border_width(20)

        self.weather_data = weather_data

        self.temperature = self.weather_data.temperature
        self.condition = self.weather_data.condition
        self.sunrise = self.weather_data.sunrise
        self.sunset = self.weather_data.sunset
        self.cloudiness = self.weather_data.cloudiness
        self.wind = self.weather_data.wind
        self.humidity = self.weather_data.humidity
        self.image = self.weather_data.image

        self.humidity_label = Gtk.Label()
        self.wind_label = Gtk.Label()
        self.cloudiness_label = Gtk.Label()
        self.sunset_label = Gtk.Label()
        self.sunrise_label = Gtk.Label()
        self.condition_label = Gtk.Label()
        self.temperature_label = Gtk.Label()

        self.status_image = Gtk.Image()

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        sunbox = Gtk.HBox()
        cloudbox = Gtk.HBox()

        self.status_image.set_from_pixbuf(self.image)

        sunrise_image = Gtk.Image()
        sunset_image = Gtk.Image()
        sunrise_image.set_from_pixbuf(IMG.sunrisepix)
        sunset_image.set_from_pixbuf(IMG.sunsetpix)

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 150")
        self.temperature_label.override_font(tempdesc)
        self.temperature_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        conditiondesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        self.condition_label.override_font(conditiondesc)
        self.condition_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        labeldesc = Pango.FontDescription("AnjaliOldLipi Bold 23")

        self.sunrise_label.override_font(labeldesc)
        self.sunrise_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.sunset_label.override_font(labeldesc)
        self.sunset_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.cloudiness_label.override_font(labeldesc)
        self.cloudiness_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.wind_label.override_font(labeldesc)
        self.wind_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.humidity_label.override_font(labeldesc)
        self.humidity_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        # self.temperature_label.set_text(self.temperature.split('.')[0] + "°F")
        # self.condition_label.set_text(self.condition)
        # self.sunrise_label.set_text(self.sunrise)
        # self.sunset_label.set_text(self.sunset)
        # self.cloudiness_label.set_text("Cloudiness: " + self.cloudiness + '%')
        # self.wind_label.set_text("Wind Speed: " + self.wind + ' mph')
        # self.humidity_label.set_text("Humidity: " + self.humidity + '%')

        self.update_weather()

        sunbox.pack_start(sunrise_image, True, False, 0)
        sunbox.pack_start(self.sunrise_label, True, True, 0)
        sunbox.pack_start(sunset_image, True, True, 0)
        sunbox.pack_start(self.sunset_label, True, True, 0)
        sunbox.pack_start(self.humidity_label, True, True, 0)

        cloudbox.pack_start(self.cloudiness_label, True, False, 0)
        cloudbox.pack_start(self.wind_label, True, False, 0)

        center.pack_start(self.status_image, True, False, 0)
        center.pack_start(self.temperature_label, True, False, 0)
        center.pack_start(self.condition_label, True, False, 0)
        center.pack_start(cloudbox, True, False, 0)
        center.pack_start(sunbox, True, False, 0)
        self.put(center, ((Gdk.Screen.width() / 2) - 325), 100)
        # self.add(center)

    def update_weather(self):
        self.humidity_label.set_text(f"Humidity: {self.weather_data.humidity} %")
        self.wind_label.set_text(f"Wind Speed: {self.weather_data.wind} mph")
        self.cloudiness_label.set_text(f"Cloudiness: {self.weather_data.cloudiness} %")
        self.sunset_label.set_text(self.weather_data.sunset)
        self.sunrise_label.set_text(self.weather_data.sunrise)
        self.condition_label.set_text(self.weather_data.condition)
        self.temperature_label.set_text(f"{round(self.weather_data.temperature, 1)} °F")

        self.status_image.set_from_pixbuf(self.weather_data.image)

        return True
