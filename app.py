from flask import Flask,render_template,request,redirect,url_for,session,flash
from werkzeug.security import generate_password_hash,check_password_hash
from models import User,Notes

app=Flask(__name__)
app.secret_key="notes@123"

@app.route("/",methods=['GET','POST'])
def regi():
	if request.method=='POST':
			name=request.form['name']
			pas=request.form['pass']
			session['name']=name
			session['pass']=pas
			user=User(name,pas)
			user.register()
			return redirect("/login")
	return render_template("register.html")
	
@app.route("/login",methods=['GET','POST'])
def logi():
			if request.method=='POST':
				item1=request.form['name']
				item2=request.form['pass']
				user=User(item1,item2)
				if user.login():
					session["name"]=item1
					return redirect("/notes")
				else:
					flash("Invalid name or password")
			return render_template("login.html")
				
@app.route("/notes")
def note():
		if "name" in session:
				name=session["name"]
				return render_template("notes.html")
		else:
			return redirect("/")
@app.route("/home", methods=['GET','POST'])

def home():
	if request.method == 'POST':
		notes= request.form['notes']
		username = session['name']
		note = Notes(username, notes)
		note.save_notes()
		return redirect("/final")
	return render_template("home.html")
@app.route("/final")
def final():
	Note=Notes("","")
	row=Note.return_notes()
	return render_template("final.html",notes=row)
					
				
			
app.run(debug=True)