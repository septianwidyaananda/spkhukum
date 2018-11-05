from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db_spkhukum import DBConnect
from listComp_spkhukum import listcomp

conn = DBConnect()
root = Tk()
root.geometry('600x285')
root.title('Manajemen List Kasus Kejaksaan Tinggi Surabaya')
root.configure(background='#AEB6BF')

style = Style()
style.theme_use('classic')
for elem in ['TLabel', 'TButton', 'TRadioutton']:
	style.configure(elem, background='#AEB6BF')

labels = ['Nama Lengkap:', 'Jenis Kelamin:', 'Kasus:']
for i in range(3):
	Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

BuList = Button(root, text='Daftar List')
BuList.grid(row=4, column=1)
BuSubmit = Button(root, text='Kirim')
BuSubmit.grid(row=4, column=2)

fullnama = Entry(root, width=40, font=('Arial', 14))
fullnama.grid(row=0, column=1, columnspan=2)
Spanjeniskelamin = StringVar()
Radiobutton(root, text='Laki-laki', value='Laki-laki', variable=Spanjeniskelamin).grid(row=1, column=1)
Radiobutton(root, text='Perempuan', value='Perempuan', variable=Spanjeniskelamin).grid(row=1, column=2)
kasus = Text(root, width=35, height=5, font=('Arial', 14))
kasus.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

def SaveData():
	msg = conn.Add(fullnama.get(), Spanjeniskelamin.get(), kasus.get(1.0, 'end'))
	fullnama.delete(0, 'end')
	kasus.delete(1.0, 'end')
	showinfo(title='Tambah', message=msg)

def ShowList():
	listrequest = listComp()


BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

root.mainloop()