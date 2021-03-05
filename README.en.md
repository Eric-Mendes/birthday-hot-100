# birthday-hot-100 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Billboard_logo.svg/1280px-Billboard_logo.svg.png" align="right" width=100 />

|<img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/1200px-Flag_of_Brazil.svg.png" width=25>|[Ler isto em português](https://github.com/Eric-Mendes/birthday-hot-100 "README.md em português")|
|---|:--|

## Find out how was Billboard's Hot 100 chart on the day you were born!
This is a web-scraping project that saves Billboard's Hot 100 for a specified date on a .csv file

## Running
To run this project - besides installing all the stuff on the imports - you need to install [gecko-driver](https://github.com/mozilla/geckodriver/releases "Go to the download page") and specify its path here:
```
browser = webdriver.Firefox(executable_path="/PATH_TO_GECKO_DRIVER/")
```
You also need to define a path to save the csv file generated:
```
path_to_save = '/.../BILLBOARD_HOT_100/billboard_hot_100_week_{day}-{month}-{year}.csv'.format(day=birthday_day, month=birthday_month, year=birthday_year)
```
## For the future
1. I intend to integrate this script with [Spotify's Web API](https://developer.spotify.com/documentation/web-api/ "See the Docs") to be able to save a personalized playlist with the songs from that specific Hot 100.
2. I need help from web devs to make this a functioning website.

## Improvements
I don't understand a lot about docker (yet). If you dockerize this project to minimize install dependencies this will be of great help. Talk to me on [LinkedIn](https://www.linkedin.com/in/eric-velasco-de-paula-mendes/).
