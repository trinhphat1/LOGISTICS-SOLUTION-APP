from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

def CUSTOMER_DEMAND():
    # Create the main window
    root = Tk()
    root.title("Customer Demand")

    # Open the image
    img = Image.open("D:\\1.png")

    # Resize the image (optional)
    img = img.resize((500, 500))

    # Convert the image
    photo = ImageTk.PhotoImage(img)

    # Create a label and set its position using place()
    label = Label(root, image=photo)
    label.place(x=0, y=0)  # Adjust x and y values for desired position
        # Open the image
    img1 = Image.open("D:\\2.png")

    # Resize the image (optional)
    img1 = img1.resize((500, 500))

    # Convert the image
    photo1 = ImageTk.PhotoImage(img1)

    # Create a label and set its position using place()
    label1 = Label(root, image=photo1)
    label1.place(x=510, y=0)  # Adjust x and y values for desired position
            # Open the image
    img2 = Image.open("D:\\3.png")

    # Resize the image (optional)
    img2 = img2.resize((500, 500))

    # Convert the image
    photo2 = ImageTk.PhotoImage(img2)

    # Create a label and set its position using place()
    label2 = Label(root, image=photo2)
    label2.place(x=1020, y=0)  # Adjust x and y values for desired position
                # Open the image
    img3 = Image.open("D:\\4.png")

    # Resize the image (optional)
    img3 = img3.resize((800, 250))

    # Convert the image
    photo3 = ImageTk.PhotoImage(img3)

    # Create a label and set its position using place()
    label3 = Label(root, image=photo3)
    label3.place(x=0, y=500)  # Adjust x and y values for desired position
                    # Open the image
    img4 = Image.open("D:\\5.png")

    # Resize the image (optional)
    img4 = img4.resize((700, 250))

    # Convert the image
    photo4 = ImageTk.PhotoImage(img4)

    # Create a label and set its position using place()
    label4 = Label(root, image=photo4)
    label4.place(x=850, y=500)  # Adjust x and y values for desired position


    # Start the event loop
    root.mainloop()

# Call the function to display the image
CUSTOMER_DEMAND()