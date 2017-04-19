from app import db, app
from app.models import Employee
from flask import session, request, flash, url_for, redirect, render_template, abort ,g, escape

@app.route('/')
def hello_world():
	return render_template('addUser.html')

@app.route('/addEmployee', methods = ['GET', 'POST'])
def addEmployee():
	success = None
	error = None
	if request.method == 'POST':
		if not request.form['firstName'] or not request.form['otherNames'] or not request.form['designation'] or not request.form['assignRoom']:
			error = 'Empty fields not allowed'
			return render_template('addUser.html', error = error)
		else:
			employee = Employee(request.form['firstName'], request.form['otherNames'],request.form['designation'], request.form['assignRoom'])
			if employee:
				success = 'You have successfully added a' + ' ' + request.form['designation']
			db.session.add(employee)
			db.session.commit()
			return render_template('addUser.html', success = success)
	else:
		return render_template('addUser.html')


if __name__ == '__main__':
   app.run(debug = True, port=5002)

# @app.route('/')
# def hello_world():
# 	return 'Hello World'

# if __name__ == '__main__':
#    app.run()