n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class WeatherData:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
data=[]
for i in range(n):
    data.append(WeatherData(date[i],day[i],weather[i]))
early_rain=0
for i in range(n):
    if weather[i]=="Rain":
        early_rain=i
        break

for i in range(n):
    if data[i].weather=="Rain" and data[i].date<data[early_rain].date:
        early_rain=i

print(data[early_rain].date,data[early_rain].day,data[early_rain].weather)