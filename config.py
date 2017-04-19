class Development:
	'SQLALCHEMY_DATABASE_URI' = 'postgresql://localhost/allocator'
	app.config['PGSQL_DATABASE_USER'] = 'collins'
	app.config['PGSQL_DATABASE_PASSWORD'] = 'root'
	app.config['PGSQL_DATABASE_DB'] = 'allocator'
	app.config['PGSQL_DATABASE_HOST'] = 'localhost'

class Testing:

		