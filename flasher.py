import googlemaps
import re
import RPi.GPIO as gpio
import time
import random
import Tkinter as tk
from PIL import ImageTk, Image



#This creates the main window of an application
window = tk.Tk()
window.title("Directions")
window.geometry("300x300")
window.configure(background='red')

client = googlemaps.Client("AIzaSyAdis3Ww-4VVS-K8fq1CEF-VmD-JsQiBsA")
#canvas = Canvas(root, width = 300, height = 300)  

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open("uturn.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("straight.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("right.jpeg"))
img4 = ImageTk.PhotoImage(Image.open("left.jpeg"))
#canvas.create_image(20, 20, anchor=NW, image=img)
i=1
#tk.update()
while(True):
    turn=(client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][i]['maneuver'])
    print(client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][0]['distance']['text'])
    i=i+1
    if ( turn == "turn-left" ):
        print("H")
        #panel = tk.Label(window, image = img4)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window.update()
        
        
        time.sleep(1)
        
        

    if ( turn == "turn-right" ):
        print("He")
        panel = tk.Label(window, image = img3)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window.update()
        time.sleep(1)
        
    #tk.update()
    
    if ( turn == "uturn-right" ):
        print("Hel")
        panel = tk.Label(window, image = img1)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window.update()
        time.sleep(1)
        
        #tk.update()
        
    if ( turn == "uturn-right" ):
        print("Hell")
        panel = tk.Label(window, image = img2)
       
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window.update()
        time.sleep(1)
        
    

    
