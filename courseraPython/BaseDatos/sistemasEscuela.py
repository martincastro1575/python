from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Time
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists
from sqlalchemy import Table, Text 
import datetime
import csv

Base = declarative_base()


class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, Sequence('alumno_id_seq'), primary_key = True)
    firstname = Column(String)
    lastname = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship("Curso", back_populates='alumno')

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, Sequence('curso_id_seq'), primary_key = True)
    nombre = Column(String)
    alumno = relationship('Alumno', back_populates='curso')
    horario_curso = relationship('Horario', back_populates='curso')
    def __repr__(self):
        return f"{self.nombre}"

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, Sequence('profesor_id_seq'), primary_key = True)
    firstname = Column(String)
    lastname = Column(String)
    
    horario_profe = relationship("Horario", back_populates='profesor')
   

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, Sequence('horario_id_seq'), primary_key = True)
    dia_semana = Column(String)  
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    curso_id = Column(Integer,ForeignKey('curso.id'))
    profesor_id = Column(Integer, ForeignKey('profesor.id'))

    curso = relationship('Curso', back_populates='horario_curso')
    profesor = relationship('Profesor', back_populates='horario_profe')    

    def __repr__(self):
        return f"{self.dia_semana} {self.hora_inicio} {self.hora_fin}"

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Creando Cursos
curso1 = Curso(nombre='Primero')
curso2 = Curso(nombre='Segundo')

#Creando alumnos y asignando los aun curso
alum1 = Alumno(firstname="Maria", lastname="Perez", curso = curso1)
alum2 = Alumno(firstname="Esther", lastname="Cardona", curso = curso2)
alum3 = Alumno(firstname="Sol", lastname="Perez", curso = curso1)


#Creando profesores
profe1 = Profesor(firstname = 'Albus', lastname = 'Dumblodore')

#Creando Horarios
horario1 = Horario(dia_semana='Lunes', hora_inicio=datetime.time(7,00), hora_fin=datetime.time(11,00), curso=curso1, profesor = profe1 )
horario2 = Horario(dia_semana='Martes', hora_inicio=datetime.time(8,00), hora_fin=datetime.time(14,00), curso=curso2, profesor = profe1)
horario3 = Horario(dia_semana='Jueves', hora_inicio=datetime.time(14,00), hora_fin=datetime.time(17,00), curso=curso1, profesor = profe1)

#creando las sesiones
session.add(curso1)
session.add(curso2)

session.add(alum1)
session.add(alum2)
session.add(alum3)

session.add(profe1)

session.add(horario1)
session.add(horario2)
session.add(horario3)

session.commit()

alum_list = []
for alum in curso1.alumno:
    alum_list.append(alum)

print("Alumnos del curso 1", alum_list)
print("Exportando listado de alumnos......")   

#Listado de curso1 x Alumno
with open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/alumnoscurso.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    list_curso1 = alum_list
    writer.writerow(list_curso1)

print("=====================================================\n")
profe_list = []
for profe in profe1.horario_profe:
    datos= "Horario:  " + str(profe) + " - " + "Profesor: " + profe1.firstname
    profe_list.append(datos)

print("Horario Profe: ", profe_list)
print("Exportando listado de Horario Profe......")   

#Listado de profe horario
with open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/profesorhorario.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    list_profe1_horario = profe_list
    writer.writerow(list_profe1_horario)

print("=====================================================\n")

#Listado de curso por horario
list_curso_horario = "Dia: " + horario1.dia_semana + " - Inicia: " + str(horario1.hora_inicio) + " - Termina: " + str(horario1.hora_fin) + " - Curso: " + str(horario1.curso)
print("Horario Curso: ", list_curso_horario)
print("Exportando Listado de horario Curso....")

with open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/cursohorario.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    list_horario = list_curso_horario
    writer.writerow(list_horario)

print("=====================================================\n")