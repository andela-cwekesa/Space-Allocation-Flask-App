from ..models.models import Employee;
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g

@app.route('/addEmployee', methods = ['GET', 'POST'])

def addEmployee():
	if(request.method == 'POST'):
		employee = Employee(request.form['firstName'], request.form['otherNames'],request.form['designation'], request.form['assignRoom'])
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('addEmployee'))
        return render_template('addUser.html')
