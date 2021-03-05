import pandas as pd
import datetime
from selenium import webdriver

"""
Billboard's hot 100 is weekly
"""

y = int(input("Type your birthday's year"))
m = int(input("Type your birthday's month (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 or 12)"))
d = int(input("Type your birthday's day"))

birthday = datetime.datetime(y, m, d)
weekday = int(birthday.strftime('%w'))

that_saturday = birthday + datetime.timedelta(days=(6 - weekday))
birthday_day = that_saturday.strftime('%d')
birthday_month = that_saturday.strftime('%m')
birthday_year = that_saturday.strftime('%Y')

data = []

# enter the website
browser = webdriver.Firefox(executable_path="/PATH_TO_GECKO_DRIVER/")
browser.get("https://www.billboard.com/charts/hot-100/{}-{}-{}".format(birthday_year, birthday_month, birthday_day))

# get the hot 100
for i in range(100):
    song_title = browser.find_elements_by_xpath("//span[@class='chart-element__information__song text--truncate color-"
                                                "-primary']")[i].text
    artist = browser.find_elements_by_xpath("//span[@class='chart-element__information__artist text--truncate color-"
                                            "-secondary']")[i].text
    last_week = browser.find_elements_by_xpath("//div[@class='chart-element__meta text--center color--secondary text-"
                                               "-last']")[i].text
    peak = browser.find_elements_by_xpath("//div[@class='chart-element__meta text--center color--secondary text-"
                                          "-peak']")[i].text
    weeks_on_chart = browser.find_elements_by_xpath("//div[@class='chart-element__meta text--center color--secondary "
                                                    "text--week']")[i].text

    data.append([str(song_title), str(artist), last_week, peak, weeks_on_chart])

    print("{}.".format(i+1))
    print("Song: {title}\nArtist: {name}\n".format(title=song_title, name=artist))


df = pd.DataFrame(data, index=[i for i in range(1, len(data)+1)],
                  columns=['SONG', 'ARTIST', 'LAST WEEK', 'PEAK', 'WEEKS ON CHART'])

df.head()
path_to_save = '/.../BILLBOARD_HOT_100/billboard_hot_100_week_{day}-{month}-{year}.csv'.\
    format(day=birthday_day, month=birthday_month, year=birthday_year)
df.to_csv(r'{}'.format(path_to_save),
          index=False)
