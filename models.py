import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash

class User:
	def __init__(self,name,password):
		self.name=name
		self.password=password
	def register(self):
			hashed=generate_password_hash(self.password)
			con=sqlite3.connect("tobiiii.db")
			cur=con.cursor()
			cur.execute('''CREATE TABLE IF NOT EXISTS tobii(name TEXT , pass  TEXT)''')
			cur.execute('''INSERT INTO tobii VALUES(?,?)''',(self.name,hashed))
			con.commit()
	def login(self):
			con=sqlite3.connect("tobiiii.db")
			cur=con.cursor()
			cur.execute('''SELECT * FROM tobii WHERE name=?''',(self.name,))
			row=cur.fetchone()
			if row and check_password_hash(row[1],self.password):
				return True
			return False
class Notes():
	def __init__(self,username,text):
		self.username=username
		self.text=text
	def save_notes(self):
				con=sqlite3.connect("tobiiii.db")
				cur=con.cursor()
				cur.execute('''CREATE TABLE IF NOT EXISTS notes(name TEXT , note TEXT)''')
				cur.execute('''INSERT INTO notes VALUES(?,?)''',(self.username,self.text))
				con.commit()
	def return_notes(self):
				con=sqlite3.connect("tobiiii.db")
				cur=con.cursor()
				cur.execute('''SELECT * FROM notes''')
				row=cur.fetchall()
				return row