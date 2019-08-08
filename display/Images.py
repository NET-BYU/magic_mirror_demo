from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import GdkPixbuf


# System Icons
icon = "./src/general/icon.png"
helpimg = "./src/apps/help.svg"
homeimg = "./src/apps/home.svg"
infoimg = "./src/apps/info.svg"
messagesimg = "./src/apps/messages.svg"
quoteimg = "./src/apps/quote.svg"
timeimg = "./src/apps/time.svg"
calendarimg = "./src/apps/calendar.svg"
logoimg = "./src/general/BYU.svg"

# Weather Icons
severe_img = "./src/weather/alert-severe.svg"
broken_clouds_img = "./src/weather/broken-clouds.svg"
clear_day_img = "./src/weather/clear-day.svg"
clear_night_img = "./src/weather/clear-night.svg"
clouds_day_img = "./src/weather/clouds-day.svg"
clouds_night_img = "./src/weather/clouds-night.svg"
mist_img = "./src/weather/mist.svg"
rain_img = "./src/weather/rain.svg"
showers_img = "./src/weather/showers.svg"
snow_img = "./src/weather/snow.svg"
thunderstorm_img = "./src/weather/thunderstorm.svg"

# Directions
up_img = "./src/direction/up.svg"
down_img = "./src/direction/down.svg"

# Home Status Bar
message = "./src/homescreen/message.svg"

# System Images
iconpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(icon, -1, 250, True)
helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 250, True)
homepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(homeimg, -1, 128, True)
infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 250, True)
messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 250, True)
quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 250, True)
timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 250, True)
calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 250, True)
logopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(logoimg, -1, 425, True)

# Weather Images
severepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(severe_img, -1, 250, True)
brokencloudspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(broken_clouds_img, -1, 250, True)
cleardaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_day_img, -1, 250, True)
clearnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_night_img, -1, 250, True)
cloudsdaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_day_img, -1, 250, True)
cloudsnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_night_img, -1, 250, True)
mistpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(mist_img, -1, 250, True)
rainpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(rain_img, -1, 250, True)
showerspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(showers_img, -1, 250, True)
snowpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(snow_img, -1, 250, True)
thunderstormpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(thunderstorm_img, -1, 250, True)
sunrisepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_day_img, -1, 50, True)
sunsetpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_night_img, -1, 50, True)

# Navegator Bar
home_helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 128, True)
home_infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 128, True)
home_messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 128, True)
home_quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 128, True)
home_timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 128, True)
home_calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 128, True)

# Direction arrows
uppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(up_img, -1, 50, True)
downpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(down_img, -1, 50, True)

# Home Screen Status Bar
status_message_sing_pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(message, -1, 50, True)
status_message_plu_pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 50, True)
status_severepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(severe_img, -1, 50, True)
status_brokencloudspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(broken_clouds_img, -1, 50, True)
status_cleardaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_day_img, -1, 50, True)
status_clearnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_night_img, -1, 50, True)
status_cloudsdaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_day_img, -1, 50, True)
status_cloudsnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_night_img, -1, 50, True)
status_mistpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(mist_img, -1, 50, True)
status_rainpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(rain_img, -1, 50, True)
status_showerspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(showers_img, -1, 50, True)
status_snowpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(snow_img, -1, 50, True)
status_thunderstormpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(thunderstorm_img, -1, 50, True)
