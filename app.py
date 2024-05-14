#Khai báo thư viện
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import ttk
import re
import requests
#Tạo background và giao diện app
root =Tk()
root.title("LOGISTICS SOLUTION APP")
root.geometry("1280x720")
root.iconbitmap("D:\\log.jpg")
load_img=Image.open("D:\\log2.jpg")
render_img=ImageTk.PhotoImage(load_img)
background_img=Label(root,image=render_img)
background_img.place(x=0,y=0)
root.resizable(False,False)


# Tạo khung chứa 
frame_tele = tk.Frame(root, bg='#00BFFF')
frame_tele.place(x=0,y=105)

frame_email = tk.Frame(root, bg='#00BFFF')
frame_email.place(x=0,y=135)

frame_ADDRESS = tk.Frame(root, bg='#00BFFF')
frame_ADDRESS.place(x=0,y=165)

frame_CUS = tk.Frame(root)
frame_CUS.place(x=0,y=15)
# Tạo nhãn  
label_telephone = tk.Label(frame_tele, text="", font=("Times New Roman", 16))
label_telephone.pack()


label_email = tk.Label(frame_email, text="", font=("Times New Roman", 16))
label_email.pack()

label_ADDRESS = tk.Label(frame_ADDRESS, text="", font=("Times New Roman", 16))
label_ADDRESS.pack()
#Danh mục thông tin

TELEPHONE ="TRINH HOANG PHAT 0378395033"
email ="phattrinh.31231021847@st.ueh.edu.vn"
ADDRESS=" 279 Đ. Nguyễn Tri Phương, Phường 5, Quận 10, Thành phố Hồ Chí Minh"
#Tạo các hàm

def dropdown_option_selected(selected_option):
    print("Selected option:", selected_option)

def TELEPHONE_NUMBER():
    label_telephone.config(text= TELEPHONE)

def EMAIL():
    label_email.config(text= email)

def ADDRESS1():
    label_ADDRESS.config(text= ADDRESS)


# Create a label to display information

toolbar_frame = tk.Frame(root, bg="#483d8b",borderwidth=6)
toolbar_frame.pack(fill="x")

label = tk.Label(toolbar_frame, text="UEH LOGISTICS SOLUTION",font=("Freestyle Script", 24),bg='#483d8b',fg='White',)
label.pack(side="right", padx=5, pady=0)

class RealTimeCurrenctyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
    def convert(self, from_currency, to_currency, amount):
        #init_amount = amount
        if from_currency != 'USD':
            amount = amount /self.currencies[from_currency]
        # limit the precision to 4 decimal
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class App(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        self.geometry ("500x200")

        #Label
        self.intro_label = Label(self, text = 'WELCOME TO UEH LOGISTICS SOLUTION', fg = 'red', relief=tk.RAISED, borderwidth=3)
        self.intro_label.config(font = ('Comic Sans MS', 15, 'bold'))
        self.intro_label.place(x = 40, y = 5)

        self.date_label = Label(self, text= f"1 USD = {self.currency_converter.convert('USD', 'VND', 1)} VND \n Date: \
            {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        self.date_label.config(font = ('Comic Sans MS', 11, 'bold'))
        self.date_label.place(x = 140, y = 50)

        #Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)

        #dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")

        font = ('Comic Sans MS', 12, 'bold')
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        #placing
        self.from_currency_dropdown.place(x = 30, y = 120)
        self.amount_field.place(x = 36, y = 150)
        self.to_currency_dropdown.place(x = 340, y = 120)
        self.converted_amount_field_label.place(x = 346, y = 150)

        #Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command=self.perform)
        self.convert_button.config(font = ('Comic Sans MS', 10, 'bold'))
        self.convert_button.place(x = 225, y = 135)
    
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)
        self.converted_amount_field_label.config(text=str(converted_amount))
    
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1) and result is not None)

if __name__ == "__main__":
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrenctyConverter(url)
    def EXCHANGE_RATE():
        App(converter)

# Create and add buttons to the toolbar
button1 = tk.Button(toolbar_frame, text="TELEPHONE NUMBER",command=TELEPHONE_NUMBER)
button1.pack(side=tk.LEFT, padx=30, pady=5)

button2 = tk.Button(toolbar_frame, text="EMAIL",command=EMAIL)
button2.pack(side=tk.LEFT, padx=30, pady=5)

button3 = tk.Button(toolbar_frame, text="ADRESS",command=ADDRESS1)
button3.pack(side=tk.LEFT, padx=25, pady=5)

button4 = tk.Button(toolbar_frame, text="PRODUCT AND TRANSPORTATION", command=EMAIL)
button4.pack(side=tk.LEFT, padx=25, pady=5)

button5 = tk.Button(toolbar_frame, text="CUSTOMER DEMAND", command=CUSTOMER_DEMAND)
button5.pack(side=tk.LEFT, padx=25, pady=5)

button6 = tk.Button(toolbar_frame, text="EXCHANGE RATE", command=EXCHANGE_RATE)
button6.pack(side=tk.LEFT, padx=25, pady=5)

mainloop()