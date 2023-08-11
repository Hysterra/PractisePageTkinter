import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=450,height=300)


def click_button():
    #print("button clicked")
    user_input = my_entry.get() #my entrye ne girilicekse onu str olarak bize getiriyor
    print(user_input)
#label
my_label = tkinter.Label(text="this is a label",font=("Arial",30,"normal"))
#my_label.config(bg="black",fg="white")
#my_label.pack(side="bottom") ##boş kaldığında ortada konumlandırmak için bir fonksiyon
my_label.place(x=0,y=0)
my_label.grid(row=0, column=0)

#button
my_button = tkinter.Button(text="this is a button",command=click_button)
#my_button.pack()#boş kaldığında ortalamaya çalışır
#my_button.pack(side="bottom")
#my_button.place(x=225-89/2,y=150-13) #ortalamış olduk.
my_button.grid(row=1, column=1)



'''
#buradaki kodlar ile oluşturduğumuz butonun boyutlarını elde ettik çünkü place ile ortalamak için gerekli
my_button.update()
my_button.winfo_width() #89
my_button.winfo_height()#26
print(my_button.winfo_height())
print(my_button.winfo_width())
'''


#entry
my_entry = tkinter.Entry(width=50)
#my_entry.pack()
#my_entry.place(x=225-150, y=170)
my_entry.grid(row=2,column=2)


# özgürlük sıralaması :  place>grid>pack


#çalışma sayfası

window.mainloop()