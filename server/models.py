from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer, nullable=False, default=0)
    department = db.Column(db.String, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return (f'<Employee {self.id}, {self.name}, {self.salary}, '
                f'{self.department}, {self.hire_date}>')
