import googlemaps
import re
import RPi.GPIO as gpio
import time
import Tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Directions")
window.geometry("300x300")
window.configure(background='gray')


 


img1 = ImageTk.PhotoImage(Image.open("uturn.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("straight.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("right.jpeg"))
img4 = ImageTk.PhotoImage(Image.open("left.jpeg"))








client = googlemaps.Client("AIzaSyAdis3Ww-4VVS-K8fq1CEF-VmD-JsQiBsA")
#print(client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][0]['html_instructions'])
print(re.findall('<b>[\w,-]+</b>', client.directions("Pune", 
"Mumbai")[0]['legs'][0]['steps'][0]['html_instructions'])[0].replace('<b>', "").replace('</b>', ''))
turn=client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][1]['maneuver']
print(turn)
turn_distance=client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][0]['distance']['text']

if "right" in turn and "uturn" not in turn:
    
    panel = tk.Label(window, image = img3)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    window.mainloop()
    tk.update()
    if turn_distance <= 20:
        pass
        #put in the gpio pins to turn on the indicator

elif "left" in turn and "uturn" not in turn:
    
    panel = tk.Label(window, image = img4)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    tk.update()
    window.mainloop()
    if turn_distance <= 20:
        pass
        #put in the gpio pins to turn on the indicator

elif turn == "uturn-left":
    
    panel = tk.Label(window, image = img1)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    tk.update()
    window.mainloop()
    if turn_distance <= 20:
        pass
        #put in the gpio pins to turn on the indicator
        
        
else:
    
    panel = tk.Label(window, image = img2)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    print('Go straight')
    window.mainloop()
    tk.update()
        
        