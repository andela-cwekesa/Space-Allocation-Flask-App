from __init__ import db, app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/allocator'

class Employee(db.Model):
	__tablename__ = "employees"
	id = db.Column(db.Integer, primary_key = True)
	firstName = db.Column(db.String(200))
	otherNames = db.Column(db.String(100))
	designation = db.Column(db.String(100))
	assignRoom = db.Column(db.String(100))

	def __init__(self, firstName,otherNames, designation,assignRoom):
		self.firstName = firstName
		self.otherNames = otherNames
		self.designation = designation
		self.assignRoom = assignRoom