from tkinter import *
from tkinter.ttk import *
from db_spkhukum import DBConnect
import sqlite3


class listcomp:
    def __init__(self):
        self._dbconnect = DBConnect()
        self._dbconnect.row_factory = sqlite3.Row
        self._root = Tk()
        self._root.title('Daftar List Kasus Kejaksaan Tinggi Surabaya')
        tv = Treeview(self._root)
        tv.pack()
        tv.heading('#0', text='Nomor')
        tv.configure(column=('#Nama', '#Jenis Kelamin', '#Kasus'))
        tv.heading('#Nama', text='Nama')
        tv.heading('#Jenis Kelamin', text='Jenis Kelamin')
        tv.heading('#Kasus', text='Kasus')
        cursor = self._dbconnect.ListRequest()
        for row in cursor:
            tv.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
            tv.set('#{}'.format(row['ID']), '#Nama', row['Nama'])
            tv.set('#{}'.format(row['ID']), '#Jenis Kelamin', row['Jenis Kelamin'])
            tv.set('#{}'.format(row['ID']), '#Kasus', row['Kasus'])

