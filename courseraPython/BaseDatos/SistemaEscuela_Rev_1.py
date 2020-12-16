# -*- coding: utf-8 -*-

"""
Created on Sun Nov  1 20:20:16 2020

@author: Cabeto
"""

"""
Definimos las tablas a trabajar a partir de clases y las relaciones entre
estas (uno a muchos). Se crea la sesiÃ³n y se insertan datos para verificar
el correcto funcionamiento del cÃ³digo.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

#CreaciÃ³n de tablas (clases) y sus respectivas relaciones

class Course(Base):
    __tablename__ = 'course'
    
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    course_name = Column(String)
    
    students = relationship("Student", order_by="Student.id", 
                        back_populates="course")
    schedules = relationship("Schedule", order_by="Schedule.id", 
                        back_populates="course_schedule")
    
    def __repr__(self):
        return "{}".format(self.course_name)


class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))
    
    course = relationship("Course", back_populates="students")
    
    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)
    
    
class Schedule(Base):
    __tablename__ = 'schedule'
    
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    day_of_the_week = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    
    course_schedule = relationship("Course", back_populates="schedules")
    teacher_schedule = relationship("Teacher", back_populates="t_schedules")
    
    def __repr__(self):
        return "{} {} {}".format(self.day_of_the_week, self.start_time, self.end_time)
    
    
class Teacher(Base):
    __tablename__ = 'teacher'
    
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    
    t_schedules = relationship("Schedule", order_by="Schedule.id", 
                        back_populates="teacher_schedule")
    
    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)
    
engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

#Ingreso de datos en sesiÃ³n

stud_1 = Student(firstname='George', lastname='Smith', course_id=1)
stud_2 = Student(firstname='Elise', lastname='Franklin', course_id=1)
stud_3 = Student(firstname='Laura', lastname='Bond', course_id=2)
stud_4 = Student(firstname='Peter', lastname='Roosevelt', course_id=3)

stud_1.course = Course(course_name='Biologia')
stud_3.course = Course(course_name='Matematicas')
stud_4.course = Course(course_name = 'Geografia')

sched_1 = Schedule(day_of_the_week='Lunes', start_time="8 am -", 
                   end_time="11 am", course_id=1, teacher_id=1)
sched_2 = Schedule(day_of_the_week='Sabado', start_time="9 am -", 
                   end_time="12 am", course_id=1, teacher_id=2)
sched_3 = Schedule(day_of_the_week='Martes', start_time="8 am -", 
                   end_time="11 am", course_id=2, teacher_id=1)
sched_4 = Schedule(day_of_the_week='Viernes', start_time="1 pm -", 
                   end_time="4 pm", course_id=3, teacher_id=1)
sched_5 = Schedule(day_of_the_week='Viernes', start_time="7 am -", 
                   end_time="10 am", course_id=2, teacher_id=2)

teach_1 = Teacher(firstname="John", lastname="Ronald")
teach_2 = Teacher(firstname="Elvis", lastname="Lopez")

#Guardado de datos en sesiÃ³n

session.add(stud_1)
session.add(stud_2)
session.add(stud_3)
session.add(stud_4)
session.add(teach_1)
session.add(teach_2)
session.add(sched_1)
session.add(sched_2)
session.add(sched_3)
session.add(sched_4)
session.add(sched_5)

session.commit()

#consulta de datos guardados en sesiÃ³n

print("\nImprime los estudiantes que se encuentran en cierto curso \n")
for student in session.query(Student).filter_by(course_id=1):
    print(student)
#for student in session.query(Student).filter_by(course_id=2):
    #print(student)
#for student in session.query(Student).filter_by(course_id=3):
    #print(student)

print("\nImprime el horario de un profesor especÃ­fico \n")
for teacher in session.query(Schedule).filter_by(teacher_id=1):
    print(teacher)
#for teacher in session.query(Schedule).filter_by(teacher_id=2):
    #print(teacher)

print("\nImprime el horario de un curso especÃ­fico \n")
for course in session.query(Schedule).filter_by(course_id=1):
    print(course)
#for course in session.query(Schedule).filter_by(course_id=2):
    #print(course)
#for course in session.query(Schedule).filter_by(course_id=3):
    #print(course)

print("\nImprime todos los cursos registrados \n")
for course in session.query(Course):
    print(course)
