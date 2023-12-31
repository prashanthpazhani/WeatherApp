from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

root = Tk()
root.title("Weather App")
root.geometry("450x750")
root['background'] = 'white'

# Dates 
dt = datetime.datetime.now() 
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15)) 
date.place(x=5, y=130) 
month = Label(root, text=dt.strftime('%d %B'), bg='white', font=("bold", 15)) 
month.place(x=100, y=130) 

# Time 
hour = Label(root, text=dt.strftime('%I: %M %p'), 
             bg='white', font=("bold", 15)) 
hour.place(x=10, y=160) 

# City Search
city = StringVar()
city_entry = Entry(root, textvariable=city, bg='white', font=("bold", 15))
city_entry.grid(row=0,column=0)


# Makes sure to put a night image if it is past 5pm or before 8 am. Else put sun image
if int(dt.strftime('%I')) <=8 and int(dt.strftime('%I')) >= 5:
    new = ImageTk.PhotoImage(Image.open('moon.png')) 
    panel = Label(root, image=new) 
    panel.place(x=225, y=375)
else:
    new = ImageTk.PhotoImage(Image.open('sun.png')) 
    panel = Label(root, image=new) 
    panel.place(x=225, y=375)

def load_city():
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                              + city_entry.get() + "&units=imperial&appid="+"5c0d19863ae26172c0cc19160b8a0163")
    api = json.loads(api_request.content) 

    # Temperatures
    x = api['main']
    current_temperature = x['temp']
    humidity = x['humidity']
    tempmin = x['temp_min']
    tempmax = x['temp_max']

    # Coordinates
    y = api['coord']
    longtitude = y['lon']
    latitude = y['lat']

    # Country
    z = api['sys']
    country = z['country']
    city = api['name']

    label_city.configure(text=city)
    label_country.configure(text=country)
    label_temp.configure(text=current_temperature)
    humidity_data.configure(text=humidity)
    min.configure(text=tempmin)
    max.configure(text=tempmax)
    
# Search Button
search_bar = Button(root, text= "Search", command=load_city, bg='white', font=("bold", 15))
search_bar.grid(row=0,column=1)

    # Country  Names and Coordinates
label_city = Label(root, text = "...", bg='white', font=("bold", 15))
label_city.place(x=10, y=63)

label_country = Label(root, text = "...", bg='white', font=("bold", 15))
label_country.place(x=10, y=100)

#label_lon = Label(root, text = "...", bg='white', font=("bold", 15))
#label_lon.place(x=10, y=63)

#abel_lat = Label(root, text = "...", bg='white', font=("bold", 15))
#label_lat.place(x=10, y=63)

# Current Temperature
label_temp = Label(root, text = "...", bg='white', font=("bold", 50))
label_temp.place(x=10, y=375)

#label_city = Label(root, text = "...", bg='white', font=("bold", 15))
#label_city.place(x=10, y=63)

# Other temperature details
label_humidity = Label(root, text = "Humidity: ", bg='white', font=("bold", 15))
label_humidity.place(x=0, y=500)
humidity_data = Label(root, text = "...", bg='white', font=("bold", 15))
humidity_data.place(x=100, y=500)


label_min = Label(root, text = "Min. Temp: ", bg='white', font=("bold", 15))
label_min.place(x=0, y=525)

min = Label(root, text = "...", bg='white', font=("bold", 15))
min.place(x=105, y=525)

label_max = Label(root, text = "Max. Temp: ", bg='white', font=("bold", 15))
label_max.place(x=0, y=550)

max = Label(root, text = "...", bg='white', font=("bold", 15))
max.place(x=105, y=550)


# Note 
note = Label(root, text = "All temperatures in degree Faherenheit", bg='white', font=("bold", 8))
note.place(x=80, y=620)

root.mainloop()
