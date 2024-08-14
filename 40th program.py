#40. Create a claWeatherAppss  that uses tkinter to create a weather information GUI.

import tkinter as tk 
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")
        self.title_label = tk.Label(master, text="Weather Information", font=("Arial", 16))
        self.weather_label = tk.Label(master, text="Weather: Unknown", font=("Arial", 14))
        self.weather_label.pack(pady=20)
        self.fetch_button = tk.Button(master, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack(pady=10)

    def fetch_weather(self):
        simulated_weather = "Sunny, 25°C"
        self.weather_label.config(text=f"Weather: {simulated_weather}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()