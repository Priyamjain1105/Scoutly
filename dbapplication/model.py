from app import db
from datetime import datetime

"""
class Person(db.Model):
    __tablename__ = 'person'
    pid = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    age =  db.Column(db.Integer)
    job =  db.Column(db.String(255))

    def __repr__(self):
        return f'Person with name {self.name} and age {self.age}'"""
    
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    skills = db.Column(db.String(300))
    experience = db.Column(db.Text)
    education = db.Column(db.Text)
    about_me = db.Column(db.Text)
 
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education,
            "about_me": self.about_me
        }


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    job_title = db.Column(db.String(200))
    job_desc = db.Column(db.Text)
    location = db.Column(db.String(100))
    salary = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "contact_email": self.contact_email,
            "job_title": self.job_title,
            "job_desc": self.job_desc,
            "location": self.location,
            "salary": self.salary
        }