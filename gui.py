#!/bin/python3
from tkinter import *

from tkinter import filedialog

import tkinter as asa

from PIL import Image, ImageTk

from tkinter import messagebox

from tkhtmlview import HTMLLabel

import bluetooth

from bluetooth import *

import sqlite3

from IoT_Scan import devices, stop

from IoT import scan, read, clear

from shodan_search import v

from email.message import EmailMessage

import smtplib


project = asa.Tk()
# Program title
project.title("IoT Scanner by ASA")


# Canvas
canvas = asa.Canvas(project, width=200, height=100)
canvas.grid(columnspan=3, rowspan=3)

# Frame
frame = LabelFrame(project, text="Welcome to our project", padx=5, pady=5)
frame.grid(column=1, row=1, padx=10, pady=10)

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = asa.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Credit (Frame)
Credit = asa.Label(frame, text="IoT Scanner by Adam, Simon, Arpit", font="Raleway",
                   fg="#ed1b2d", height=2, width=35)
Credit .grid(column=1, row=1)

# Message 1
Message = asa.Label(project, text="This program will scan for active IoT devices", font="Raleway",
                    fg="#ed1b2d", height=2, width=43)
Message.grid(column=1, row=2)

# New Window Opener:
New_Window = Toplevel()
# Program title for the new window
New_Window.title("IoT Scanner by ASA")


# Bluetooth Scanner
nearby_devices = discover_devices(lookup_names = True)

print ("found %d devices" % len(nearby_devices))
for name, addr in nearby_devices:
    myFile = " %s - %s" % (addr, name)
    print (myFile)
    

track = 0
myFile2 = []


for i in range (1, stop):
    
    cdev = ('Device:', devices[i]['ip'], devices[i]['mac'], devices[i]['dev_name'])

    myFile2.append(cdev)

f =  "\n".join(str(i) for i in myFile2)
f2 = f.replace('(','').replace(')','').replace(',','').replace('\'','')
cve =  "\n".join(str(i) for i in v)
f3 = f2 + cve
def ScanButton():
    Click = asa.Text(New_Window, bg="lightgray", fg="#ed1b2d")
    Click.insert(1.0, f3)
    Click.tag_configure("center", justify="center")
    Click.tag_add("center", 1.0, "end")
    Click.grid(column=2, row=0)
    # Button 5 (Close Butoon)
    btn = Button(New_Window, text="Close Window", command=New_Window.destroy, font="Raleway",
                     bg="#ed1b2d", fg="white", padx=20, pady=10).grid(column=2, row=2)


# Button 1 
First_Button = asa.Button(project, text="Click here to see the results", command=ScanButton, font="Raleway",
                   bg="#ed1b2d", fg="white", padx=20, pady=10)
First_Button.grid(column=1, row=3)


# Message 2
Message = asa.Label(project, text="The results have been saved into a text file called 'results.txt'",
                    font="Raleway", fg="#ed1b2d", height=2, width=75)
Message.grid(column=1, row=4)

# Message 3
Message = asa.Label(project, text="After closing the program, our email app will run so you can send the results to an email address.",
                    font="Raleway", fg="#ed1b2d", height=2, width=100)
Message.grid(column=1, row=5)

# Message 4
Message = asa.Label(project, text="You can close this program now (Exit Program)",
                    font="Raleway", fg="#ed1b2d", height=2, width=75)
Message.grid(column=1, row=6)

# Exit the program
button_quit = Button(project, text="Exit Program", command=project.destroy, font="Raleway",
                     bg="#ed1b2d", fg="white", padx=20, pady=10)
button_quit.grid(column=1, row=7)

# End Canvas
canvas = asa.Canvas(project, width=200, height=75)
canvas.grid(columnspan=2)

# Mainloop
project.mainloop()





# Email App

#Global variables
attachments = []

#Main Screen Init
iotEmail       = Tk()
iotEmail.title('Email App by ASA')

#Functions
def attachFile():
    filename = filedialog.askopenfilename(initialdir='c:/',title='Please select a file')
    attachments.append(filename)
    notif.config(fg='green', text = 'Attached ' + str(len(attachments)) + ' files')
    
def send():
    try:
        msg      = EmailMessage()
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        body     = temp_body.get()
        msg['subject'] = subject
        msg['from'] = username
        msg['to'] = to
        msg.set_content(body)

        for filename in attachments:
            filetype = filename.split('.')
            filetype = filetype[1]
            if filetype == "jpg" or filetype == "JPG" or filetype == "png" or filetype == "PNG":
                import imghdr
                with open(filename, 'rb') as f:
                    file_data = f.read()
                    image_type = imghdr.what(filename)
                msg.add_attachment(file_data, maintype='image', subtype=image_type, filename=f.name)

            else:
                with open(filename, 'rb') as f:
                    file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f.name)
        
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")


def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')

#Labels
Label(iotEmail, text="Welcome to our email app", font=('Calibri',16)).grid(row=0, sticky=N)
Label(iotEmail, text="Please use the form below to send an email",
      font=('Calibri',11)).grid(row=1, sticky=N, padx=5 ,pady=10)

Label(iotEmail, text="Email", font=('Calibri', 11)).grid(row=2,sticky=W, padx=5)
Label(iotEmail, text="Password", font=('Calibri', 11)).grid(row=3,sticky=W, padx=5)
Label(iotEmail, text="To", font=('Calibri', 11)).grid(row=4,sticky=W, padx=5)
Label(iotEmail, text="Subject", font=('Calibri', 11)).grid(row=5,sticky=W, padx=5)
Label(iotEmail, text="Body", font=('Calibri', 11)).grid(row=6,sticky=W, padx=5)
notif = Label(iotEmail, text="", font=('Calibri', 11),fg="red")
notif.grid(row=7,sticky=S)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
temp_body     = StringVar()

#Entries
#The sender's email box
usernameEntry = Entry(iotEmail, textvariable = temp_username)
usernameEntry.grid(row=2,column=0, sticky=N)
#The sender's password box
passwordEntry = Entry(iotEmail, show="*", textvariable = temp_password)
passwordEntry.grid(row=3,column=0, sticky=N)
#The receiver box
receiverEntry  = Entry(iotEmail, textvariable = temp_receiver)
receiverEntry.grid(row=4,column=0, sticky=N)
#The subject box
subjectEntry  = Entry(iotEmail, textvariable = temp_subject)
subjectEntry.grid(row=5,column=0, sticky=N)
#The body box
bodyEntry     = Entry(iotEmail, textvariable = temp_body)
bodyEntry.grid(row=6,column=0, sticky=N)

#Buttons
Button(iotEmail, text = "Attach", command = attachFile).grid(row=8, sticky=W,  padx=5, pady=5)
Button(iotEmail, text = "Send", command = send).grid(row=8, sticky=N, pady=5, padx=5)
Button(iotEmail, text = "Reset", command = reset).grid(row=8, sticky=E, padx=15, pady=5)
Button(iotEmail, text = "Close", command = iotEmail.destroy).grid(row=10, sticky=N,  padx=130, pady=5)


#Instructions
Instructions = Toplevel()

w1 = Label(Instructions, text="Instructions", font=('Calibri',20)).grid(row=0, sticky=N, pady=5, padx=5)

w2 = Label(Instructions, text=" In order to use the email app, \
you need to allow 'less secure apps' in your Google account (Use this email as a sender)",
           font=('Calibri',14)).grid(row=1, sticky=N, pady=5, padx=5)

w3 = Label(Instructions, text=" login to your Google account and go to: ",
           font=('Calibri',14)).grid(row=2, sticky=N, pady=5, padx=5)

w4 = Label(Instructions, text="https://myaccount.google.com/lesssecureapps",
           font=('Calibri',14)).grid(row=4, sticky=N, pady=5, padx=5)

w5 = Label(Instructions, text="OR right click your Google account picture > Manage your Google account \n \
Security > Less secure app access > Turn ON",font=('Calibri',14)).grid(row=5, sticky=N, pady=5, padx=5)

w6 = Label(Instructions, text="OR click the link BELOW",
           font=('Calibri',14)).grid(row=6, sticky=N, pady=5, padx=5)

w7 = Label(Instructions, text="Now go to the Email App", font=('Calibri',14)).grid(row=7, sticky=N, pady=5, padx=5)

w8 = Label(Instructions, text="1. Attach the file 'results.txt'", font=('Calibri',14)).grid(row=8, sticky=N, pady=5, padx=5)

w9 = Label(Instructions, text="2. Fill the form with your info", font=('Calibri',14)).grid(row=9, sticky=N, pady=5, padx=5)

w10 = Label(Instructions, text="3. Click 'Send'", font=('Calibri',14)).grid(row=10, sticky=N)

w11 = Label(Instructions, text="\n", font=('Calibri',14)).grid(row=11, sticky=N)

w12 = Label(Instructions, text="Click the LINK below to access your Google Account", font=('Calibri',16)).grid(row=12, sticky=N)

html_label=HTMLLabel(Instructions,
                     html='<a href="https://myaccount.google.com/lesssecureapps"> LINK',
                     font=('Calibri',1)).grid(row=13, sticky=N)

Button(Instructions, text = "Close Instructions",
       command = Instructions.destroy).grid(row=14, sticky=N,  padx=130, pady=5)

#Mainloop
iotEmail.mainloop()