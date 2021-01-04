import tkinter as tk
import requests

#Formatting API retrieved data into a useable form
def format_responce(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_string  = 'City: %s \nConditions: %s \nTemperature (C): %s' % (name, description, temperature)
    except:
        final_string = 'There was a problem retrieving data'
    return final_string

#Retrieving weather data from the API
def get_weather(city):
    weather_key = 'e95e0b75fb742ef0d5b705efb2d7a6cc'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key,
              'q': city,
              'units':'Metric'}
    responce = requests.get(url,params=params)
    weather = responce.json()


    label['text']=format_responce(weather)


#Setting up GUI root/base 
root = tk.Tk()
root.title('Weather App')
canvas = tk.Canvas(root,height=700, width=800)
canvas.pack()

#Adding GUI elements and stylings
background_label = tk.Label(root)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='light blue',bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75,anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text='Get Weather',font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

lower_frame = tk.Frame(root, bg='light blue',bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75,anchor='n')

label = tk.Label(lower_frame, text='This is a label',font=('Modern', 24))
label.place(relwidth=1,relheight=1)


root.mainloop()

