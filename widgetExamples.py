from tkinter import *

# * her şeyi demek
# farklı bir window oluşturma stili. Aynı sonuç

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

# label
my_label = Label(text="my label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.pack()
my_label.config(padx=20, pady=20)


def button_clicked():
    print("Button clicked")
    print(my_entry.get())  # entry sıkıntı çıkartmıyor
    # print(my_text.get()) # text sıkıntı çıkarıyor. index istiyor
    print(my_text.get("1.0", END))  # input, line 1 den ve 0. karakterden başlasın, sona kadar gitsin demek


# button
my_button = Button(text="button", command=button_clicked)
my_button.config(padx=20, pady=20)
my_button.pack()

# entry
# single line
my_entry = Entry(width=20)
my_entry.pack()

# text
# multiline
my_text = Text(width=30, height=10)

my_text.focus() # input line text kısmından başlar öncelikli olarak
my_text.pack()

#scale
def scale_selected(value): #devamlı sayıları yazıyor
    print(value)

my_scale = Scale(from_=0, to=50,command= scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0,to=50, command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def checkButton_selected():
    print(check_state.get()) # 1 ve 0 vericek

check_state = IntVar() #check_state değişkeni seçildiğinde 1 olur seçilmediğinde 0. Çünkü IntVar() buna yarıyor direkt tkinter ile gelen bir özellik
my_checkbutton = Checkbutton(text="check",variable=check_state,command=checkButton_selected)
my_checkbutton.pack()

#radio button  //kod denendiğinde daha iyi anlaşılacaktır
def radio_selected():
    print((radio_checked_state.get()))

radio_checked_state = IntVar()
my_radioButton = Radiobutton(text="1. option", value=10, variable=radio_checked_state,command=radio_selected)
my_radioButton_2 = Radiobutton(text="2. option", value=20, variable=radio_checked_state,command=radio_selected)

my_radioButton.pack()
my_radioButton_2.pack()

#listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = Listbox()
name_list = ["Aykan","ABC","QWE","FGH","BNM"]

for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])

my_listbox.bind('<<ListboxSelect>>',listbox_selected) #jargonu bu
my_listbox.pack()


window.mainloop()

# burası ders notu niteliğinde bir sayfadır