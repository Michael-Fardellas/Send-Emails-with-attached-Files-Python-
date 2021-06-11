import smtplib
import tkinter as tk
from tkinter import filedialog
# from email.message import EmailMessage
from tkinter import messagebox

attachments = []


def attachFile(event = None):
    location = searchby_entry.get()
    filename = filedialog.askopenfilename(initialdir= location ,title='Please select a file')
    attachments.append(filename)
    newlabel = tk.Label(root, text = "{} file(s) attached succesfully".format(len(attachments)), font = ("Helvetica", 12, "bold"), fg = "green")
    newlabel.place(relx = 0.3, rely = 0.95)


def send_message(event = None):
    try:
        msg      = EmailMessage()
        username = username_entry.get()
        password = password_entry.get()
        to       = email_receipient_entry.get()
        subject  = "Automated Email"
        body     = Message_TXT.get("1.0",'end-1c')
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
            print("idk")
            return
        else:
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            print("Success")
            newlabel = tk.Label(root, text = "The email has been sent succesfully", font = ("Helvetica", 12, "bold"), fg = "green")
            newlabel.place(relx = 0.3, rely = 0.95)
            #newlabel.config(text="Email has been sent successfully", fg="green")
    except Exception as e:
        tk.messagebox.showerror(title="Error occured while sending the email ", message=e)
    
HEIGHT = 500
WIDTH = 600

    
root = tk.Tk()

root.resizable(False, False)
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


username_label = tk.Label(root, text = "Email: ", font = ("Helvetica", 14, "bold"))
username_label.place(relx = 0.07, rely = 0.15, relwidth = 0.2)


password_label = tk.Label(root, text = "Password: ", font = ("Helvetica", 14, "bold"))
password_label.place(relx = 0.07, rely = 0.3, relwidth = 0.2)


username_entry = tk.Entry(root)
username_entry.place(relx = 0.28,rely=0.16, relwidth = 0.17)


password_entry = tk.Entry(root, show = "*")
password_entry.place(relx = 0.28,rely=0.31, relwidth = 0.17)


email_receipient_label = tk.Label(root, text = "Email Receipient:", font = ("Helvetica", 14, "bold"))
email_receipient_label.place(relx = 0.07, rely = 0.44)

email_receipient_entry = tk.Entry(root)
email_receipient_entry.place(relx = 0.07, rely = 0.54, relwidth = 0.3)

Message_Label = tk.Label(root, text = "Message :", font = ("Helvetica", 16, "bold"))
Message_Label.place(relx = 0.07, rely = 0.62)

Message_TXT = tk.Text(root)
Message_TXT.place(relx =  0.07, rely = 0.68, relwidth = 0.4, relheight = 0.25)


searchby_lbl = tk.Label(root, text = "Search files from: ", font = ("Helvetica", 15, "bold"))
searchby_lbl.place(relx = 0.6, rely = 0.07)

searchby_entry = tk.Entry(root)
searchby_entry.place(relx = 0.6, rely = 0.17, relwidth = 0.3)

searchbutton = tk.Button(root, text = "🔎", command = lambda: attachFile(), borderwidth = 0, font = ("Helvetica", 16))
searchbutton.place(relx = 0.55, rely = 0.156)

finalbutton = tk.Button(root, text = "SEND \n EMAIL", command = lambda : send_message(), borderwidth = 7, font = ("Helvetica", 20))
finalbutton.place(relx = 0.6, rely = 0.56)

#canvas.create_image(338, 93, image= what)

root.bind('<Return>', send_message)

root.bind("<Return>", attachFile)

root.mainloop()