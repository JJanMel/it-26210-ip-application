import tkinter as tk
import requests

#Create the window that will display the application
sample = tk.Tk()
sample.title('IP Getter')
sample.geometry("250x100")

#Function to set the text of the input box
def setTextInput(text):
    textExample.delete(0,"end")
    textExample.insert(0, text)

#Adds the input box into the GUI
textExample = tk.Entry(sample)
textExample.pack()

#Button for the application to begin its process
button = tk.Button(sample, text='Get IP', width=10, command = lambda:setTextInput(requests.get('https://api.ipify.org').text))
button.place(x= 90, y = 30)

#Inititalize the GUI
sample.mainloop()


