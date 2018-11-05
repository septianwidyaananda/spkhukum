import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('information.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists Comp(ID integer primary key autoincrement, Name varchar(255), JenisKelamin varchar(255), Comment text)')
		self._db.commit()
	def Add(self, nama, jeniskelamin, kasus):
		self._db.execute('insert into Comp (Nama, Jenis Kelamin, Kasus) values (?,?,?)',(nama,jeniskelamin,kasus))
		self._db.commit()
		return 'Selamat Anda Berhasil Input Data'
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor
