from tkinter import *
from tkinter import messagebox

format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}----Welcome to Weather App by Cities----{format_reset}")

greeting = "Welcome to Weather App by Cities"

cities = {
    "Amsterdam": {
        "Temperature": "8°C",
        "Conditions": "Cloudy",
        "Wind Speed": "13 MPH",
        "Humidity": "84%"
    },
    "Athens": {
        "Temperature": "18°C",
        "Conditions": "Sunny",
        "Wind Speed": "12 MPH",
        "Humidity": "43%"
    },
    "Budapest": {
        "Temperature": "13°C",
        "Conditions": "Sunny",
        "Wind Speed": "3 MPH",
        "Humidity": "48%"
    },
    "Berlin": {
        "Temperature": "6°C",
        "Conditions": "Cloudy",
        "Wind Speed": "4 MPH",
        "Humidity": "84%"
    },
    "Copenhagen": {
        "Temperature": "10°C",
        "Conditions": "Cloudy",
        "Wind Speed": "4 MPH",
        "Humidity": "84%"
    },
    "Paris": {
        "Temperature": "12°C",
        "Conditions": "Cloudy",
        "Wind Speed": "5 MPH",
        "Humidity": "89%"
    },
    "Prague": {
        "Temperature": "6°C",
        "Conditions": "Cloudy",
        "Wind Speed": "2 MPH",
        "Humidity": "93%"
    },
    "Rome": {
        "Temperature": "21°C",
        "Conditions": "Partly Cloudy",
        "Wind Speed": "4 MPH",
        "Humidity": "66%"
    },
    "Vienna": {
        "Temperature": "12°C",
        "Conditions": "Mostly Cloudy",
        "Wind Speed": "5 MPH",
        "Humidity": "56%"
    }, 
    "London": {
        "Temperature": "6°C",
        "Conditions": "Cloudy",
        "Wind Speed": "12 MPH",
        "Humidity": "79%"
    },
    "Madrid": {
        "Temperature": "19°C",
        "Conditions": "Mostly Sunny",
        "Wind Speed": "4 MPH",
        "Humidity": "60%"
    }
}

def view_weather_list():
    try:
        for city in cities:
            print(f"City: {city}")
            print("Temperature: ", cities[city]["Temperature"])
            print("Conditions: ", cities[city]["Conditions"])
            print("Wind Speed: ", cities[city]["Wind Speed"])
            print("Humidity: ", cities[city]["Humidity"])
            print()
    except ValueError:
        print("The list is empty")

"""
def check_weather():
    while True:
        try:
            city_name = input("City Name: ")

            if city_name not in cities:
                raise KeyError

            print("Temperature: ", cities[city_name]["Temperature"])
            print("Conditions: ", cities[city_name]["Conditions"])
            print("Wind Speed: ", cities[city_name]["Wind Speed"])
            print("Humidity: ", cities[city_name]["Humidity"])
            print()
            print("Thank you for using our Weather App!")
            break

        except KeyError:
            print("City not found, please try again!")
        except Exception as e:
            print(f"An error occured: {e}")

check_weather()

"""

def custom_messagebox(title, message, on_close = None):
    """
    dialog = Toplevel(window)
    dialog.title(title)
    dialog.geometry("400x200")
    dialog.resizable(True, True)
    message_label = Label(dialog, text=message, font=("Arial", 12), wraplength=350, justify=LEFT)
    message_label.pack(pady=10, padx=10)
    ok_button = Button(dialog, text="OK", font=("Arial", 10), command=lambda: close_dialog(dialog, on_close))
    ok_button.pack(pady=10)
    dialog.bind("<Return>", lambda event: close_dialog(dialog, on_close))
    dialog.transient(window)
    dialog.grab_set()
    window.wait_window(dialog)
    """
    dialog = Toplevel(window)
    dialog.title(title)
    dialog_width = 400
    dialog_height = 200
    dialogDim = str(dialog_width) + 'x' + str(dialog_height)
    message_label = Label(dialog, text=message, font=("Arial", 12), wraplength=350, justify=LEFT)
    message_label.pack(pady=10, padx=10)
    ok_button = Button(dialog, text="OK", font=("Arial", 10), command=lambda: close_dialog(dialog, on_close))
    ok_button.pack(pady=10)
    dialog.geometry(dialogDim)
    dialog.resizable(False, False)
    dialog.transient(window)
    movex = (screen_width / 2) - (dialog_width / 2)
    movey = (screen_height / 2) - (dialog_height / 2)
    dialog.geometry(f'{dialog_width}x{dialog_height}+{int(movex)}+{int(movey)}')
    dialog.bind("<Return>", lambda event: close_dialog(dialog, on_close))
    dialog.transient(window)
    dialog.grab_set()
    dialog.focus_set()
    dialog.lift()
    dialog.wait_window(dialog)

def close_dialog(dialog, on_close):
    dialog.destroy()
    if on_close:
        on_close()

def check_weather(city_name):
        city_name = city_name.capitalize()
        try:
            if city_name not in cities:
                raise KeyError
            
            city_weather = cities[city_name]
            weather_info = (
                f"Temperature: {city_weather['Temperature']}\n"
                f"Conditions: {city_weather['Conditions']}\n"
                f"Wind Speed: {city_weather['Wind Speed']}\n"
                f"Humidity: {city_weather['Humidity']}\n"
            )
            custom_messagebox(f"Weather for {city_name}", weather_info, on_close=lambda: custom_messagebox("Thank You", "Thank you for using our Weather App!"))

        except KeyError:
            custom_messagebox("City not found","City not found, please try again!", on_close = None)
        except Exception as e:
            custom_messagebox("Error",f"An error occured: {e}")


window = Tk()
window.title("Weather App")
window_width = 500
window_height = 200
windowDim = str(window_width) + 'x' + str(window_height)
window.geometry(windowDim)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
xcord = (screen_width / 2) - (window_width / 2)
ycord = (screen_height / 2) - (window_height / 2)
window.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
window.title("Enter City Name")
window.grab_set()
window.focus_set()
window.lift()
Label(window, text="Welcome to Weather App by Cities", font=("Arial", 12), fg = "navy").pack(pady=5)
Label(window, text="City Name: ", font=("Arial", 12)).pack(pady=5)
city_name_var = StringVar()
entry = Entry(window, textvariable=city_name_var, font=("Arial", 12))
entry.pack(pady=5)

def on_submit():
    check_weather(city_name_var.get())

Button(window, text='Check Weather', font=("Arial", 12), command=on_submit).pack(pady=10)
entry.bind("<Return>", lambda event: on_submit())

window.mainloop()


"""
def ask_city():
    dialog = Toplevel(window)
    dialog_width = 200
    dialog_height = 200
    dialogDim = str(dialog_width) + 'x' + str(dialog_height)
    dialog.title("Enter City Name")
    dialog.geometry(dialogDim)
    dialog.resizable(False, False)
    dialog.transient(window)
    movex = (screen_width / 2) - (dialog_width / 2)
    movey = (screen_height / 2) - (dialog_height / 2)
    dialog.geometry(f'{dialog_width}x{dialog_height}+{int(movex)}+{int(movey)}')
    dialog.grab_set()
    Label(dialog, text="City Name: ", font=("Arial", 12)).pack(pady=5)
    city_name_var = StringVar()
    entry = Entry(dialog, textvariable=city_name_var, font=("Arial", 12))
    entry.pack(pady=5)

    def on_submit():
        check_weather(city_name_var.get())
        dialog.destroy()

    Button(dialog, text='Check Weather', font=("Arial", 12), command=on_submit).pack(pady=10)
    entry.bind("<Return>", lambda event: on_submit())

ask_city()
"""

"""
Label(window, text = "City Name: ").pack(pady = 5)
city_name_var = StringVar()
Entry(window, textvariable = city_name_var).pack(pady = 5)
Button(window, text='Check Weather', command=lambda: check_weather(city_name_var.get())).pack(pady = 10)

window.mainloop()
"""