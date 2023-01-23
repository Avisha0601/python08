from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.title("Encapsulation")
root.geometry("800x600")
root.config(bg="orange2")
#HEADING--
label_heading = Label(root, text="Juice Center",bg="aqua", font=("Sylfaen",18,"bold","italic"))
label_heading.place(relx=0.05,rely=0.1, anchor= W)
#LOGO IMAGE--
juice = ImageTk.PhotoImage(Image.open ("logo.png"))
juice_image=Label(root, image=juice, bg="orange2")
juice_image.place(relx=0.2, rely=0.4,anchor=CENTER)
#LOAD IMAGES--
apple = ImageTk.PhotoImage(Image.open ("apple_img.png"))
mango = ImageTk.PhotoImage(Image.open ("mango_img.png"))
orange = ImageTk.PhotoImage(Image.open ("orange.png"))
#FRUIT IMAGES--
fruit_image=Label(root, bg="orange2")
fruit_image.place(relx=0.8, rely=0.8,anchor=CENTER)
#LABEL SELECT FRUIT--
label_name = Label(root, text="Please select your fruit ",bg="grey", font=("Bahnschrift Light",15))
label_name.place(relx=0.96,rely=0.2, anchor= E)
#DROPDOWN--
fruit_list = ["Apple","Mango","Orange"]
fruit_dropdown = ttk.Combobox(root,state = "readonly", values=fruit_list, justify="right") 
fruit_dropdown.place(relx=0.95, rely=0.25, anchor= E)
#LABEL ENTRY QUANTITY-
label_quantity = Label(root, text="Enter any quantity you want ",bg="grey", font=("Bahnschrift Light",15))
label_quantity.place(relx=0.96,rely=0.35, anchor= E)
#ENTRY ELEMENT--
input_quantity = Entry(root)
input_quantity.place(relx=0.95,rely=0.4, anchor= E)
#TOTAL COST LABEL--
label_show_amount = Label(root, bg="lightgreen", font=("Bahnschrift Light",12))
label_show_amount.place(relx=0.95,rely=0.7, anchor= E)
#QUANTITY LABEL--
label_show_quantity = Label(root, bg="white", font=("Bahnschrift Light",12))
label_show_quantity.place(relx=0.95,rely=0.8, anchor= E)
class Juice:
    def _init_(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self._cost = 250
        
    def _calculateCost(self):
        total_cost = self.quantity * self._cost
        label_show_amount['text'] = "You have to pay: "+str(total_cost)+" USD"
        if(self.fruit == "Apple"):
            calorie = (self.quantity * 52)/100
            fruit_image['image'] = apple
        elif(self.fruit == "Mango"):
            calorie = (self.quantity * 60)/100
            fruit_image['image'] = mango
        elif(self.fruit == "Orange"):
            calorie = (self.quantity * 47)/100
            fruit_image['image'] = orange
        label_show_quantity['text'] = "x"+str(self.quantity)+" = "+str(calorie)
    def qetCost(self):
        self._calculateCost()
    
    def orderJuice():
        fruit = fruit_dropdown.get()
        quantity = input_quantity.get()
        obj1 = Juice(fruit,quantity)
        obj1.ggetCost()
btn = Button(root, text="TOTAL", bg="red3", fg="white", padx=10, pady=1, font("Arial",11,"bold"), relief=FLAT, command=orderJuice)
btn.place(relx=0.95,rely=0.5, anchor= E)
root.mainloop()