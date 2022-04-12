#! /usr/bin/python3

# To run the script, you need to run the following command:
# "python3 <script.py>"

from tkinter import *
import tkinter as rsa
import smtplib
from tkinter import filedialog
from email.message import EmailMessage
from PIL import Image, ImageTk
from tkinter import messagebox
import bluetooth
from bluetooth import *




project = rsa.Tk()
# Program title
project.title("IoT Scanner by ASA")
# Program icon
#project.iconbitmap("icon.ico")

# Canvas
canvas = rsa.Canvas(project, width=600, height=200)
canvas.grid(columnspan=3, rowspan=3)

# Frame
frame = LabelFrame(project, text="Welcome to our project", padx=5, pady=5)
frame.grid(column=1, row=1, padx=10, pady=10)

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = rsa.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Credit
Credit = rsa.Label(frame, text="IoT Scanner by Adam, Simon, Arpit", font="Raleway",
                   fg="#ed1b2d", height=2, width=35)
Credit .grid(column=1, row=1)

# The message
Message = rsa.Label(project, text="This program will scan for active bluetooth devices", font="Raleway",
                    fg="#ed1b2d", height=2, width=43)
Message.grid(column=1, row=2)

# New Window Opener:
New_Window = Toplevel()
# Program title for the new window
New_Window.title("IoT Scanner by ASA")
# Program icon for the new window
# New_Window.iconbitmap("icon.ico")


# Bluetooth Scanner
nearby_devices = discover_devices(lookup_names = True)
def fileSave():
    file = open ('scan_results.txt', 'w')
    for name, addr in nearby_devices:
        file.write(" %s - %s" % (addr, name) + '\n')
    file.close()
    

# Button 2 (Save Butoon)
Second_Button = rsa.Button(project, text="Click here to save the results", command=fileSave, font="Raleway",
                           bg="#ed1b2d", fg="white", padx=20, pady=10)
Second_Button.grid(column=1, row=4)

# Button function
def ScanButton():
    Click = rsa.Text(New_Window, bg="lightgray", fg="#ed1b2d")
    Click.insert(1.0, nearby_devices)
    Click.tag_configure("center", justify="center")
    Click.tag_add("center", 1.0, "end")
    Click.grid(column=2, row=0)

# Button 1 (Scan Butoon)
First_Button = rsa.Button(project, text="Click here to scan", command=ScanButton, font="Raleway",
                   bg="#ed1b2d", fg="white", padx=20, pady=10)
First_Button.grid(column=1, row=3)

# The message
Message = rsa.Label(project, text="After saving your results, you need to close this program (Exit Program)",
                    font="Raleway", fg="#ed1b2d", height=2, width=75)
Message.grid(column=1, row=5)

# The message
Message = rsa.Label(project, text="A new window will popup so you can send the results to an email address.",
                    font="Raleway", fg="#ed1b2d", height=2, width=75)
Message.grid(column=1, row=6)

Message = rsa.Label(project, text="The results have been saved to a text file called 'scan_results.txt'",
                    font="Raleway", fg="#ed1b2d", height=2, width=75)
Message.grid(column=1, row=7)

# Exit the program
button_quit = Button(project, text="Exit Program", command=project.destroy, font="Raleway",
                     bg="#ed1b2d", fg="white", padx=20, pady=10)
button_quit.grid(column=1, row=8)

# End Canvas
canvas = rsa.Canvas(project, width=600, height=75)
canvas.grid(columnspan=2)

# The Loop (Code won't work without it)
project.mainloop()










# Email

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

        filename = attachments[0]
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
Label(iotEmail, text="Welcome to our email app", font=('Calibri',15)).grid(row=0, sticky=N)
Label(iotEmail, text="Please use the form below to send an email", font=('Calibri',11)).grid(row=1, sticky=W, padx=5 ,pady=10)

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
usernameEntry = Entry(iotEmail, textvariable = temp_username)
usernameEntry.grid(row=2,column=0)
passwordEntry = Entry(iotEmail, show="*", textvariable = temp_password)
passwordEntry.grid(row=3,column=0)
receiverEntry  = Entry(iotEmail, textvariable = temp_receiver)
receiverEntry.grid(row=4,column=0)
subjectEntry  = Entry(iotEmail, textvariable = temp_subject)
subjectEntry.grid(row=5,column=0)
bodyEntry     = Entry(iotEmail, textvariable = temp_body)
bodyEntry.grid(row=6,column=0)

#Buttons
Button(iotEmail, text = "Send", command = send).grid(row=7,   sticky=W,  pady=15, padx=5)
Button(iotEmail, text = "Reset", command = reset).grid(row=7,  sticky=W,  padx=65, pady=40)
Button(iotEmail, text = "Attachments", command = attachFile).grid(row=7,  sticky=W,  padx=130, pady=40)

iotEmail.mainloop()