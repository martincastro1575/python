from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Text
from sqlalchemy import ForeignKey
import sqlite3
import csv

Base = declarative_base()


class Curso(Base):
    __tablename__ = 'curso'
    
    Id_cur = Column(Integer, Sequence('Id_cur'), primary_key=True)
    nombre_cur = Column(String)
    
    
    curso_hor = relationship('Horario', back_populates='curso')
    alumnos = relationship('Alumno', back_populates='curso')
    
    def __repr__(self):
        return "{} {}".format(self.Id_cur, self.nombre_cur) 

class Alumno(Base):
    __tablename__ = 'alumno'
    
    Id_al = Column(Integer, Sequence('Id_al'), primary_key=True)
    nombre_alu = Column(String)
    apellido_alu = Column(String)
    edad_alu = Column(Integer)
    cur_id = Column(Integer, ForeignKey('curso.Id_cur'))

    
    curso = relationship('Curso', back_populates="alumnos")
    
    def __repr__(self):
        return "{} {} {} {}".format(self.Id_al, self.nombre_alu, self.apellido_alu, self.edad_alu) 


class Profesor(Base):
    __tablename__ = 'profesor'

    Id_pro = Column(Integer, Sequence('Id_pro'), primary_key=True)
    nombre_prof = Column(String)
    apellido_prof = Column(String)

    profe_horas = relationship('Horario', back_populates='profesor')

    def __repr__(self):
        return "{} {} {}".format(self.Id_pro, self.nombre_prof, self.apellido_prof) 


class Horario(Base):
    __tablename__ = 'horario'
    
    Id_hor = Column(Integer, Sequence('Id_hor'), primary_key=True)
    nombre_dia = Column(String)
    hora_d = Column(String)
    hora_h = Column(String)


    cur_id = Column(Integer, ForeignKey('curso.Id_cur'))
    prof_id = Column(Integer, ForeignKey('profesor.Id_pro'))

    curso = relationship('Curso', back_populates='curso_hor')
    profesor = relationship('Profesor', back_populates='profe_horas')
 
  
    def __repr__(self):
        return "{} {} {} {}".format(self.Id_hor, self.nombre_dia, self.hora_d, self.hora_h) 


class QueryAlumnosCurso(object):
        
        def __init__(self, path):
            self.path = path
            
        def exportar(self, curso):
            alumnos = curso.alumnos
            with open(self.path, 'w') as a_file:
                writer = csv.writer(a_file)
                for al in alumnos:
                    writer.writerow([str(al)])




class QueryHorarioCurso(object):

    def __init__(self, path):
        self.path = path

    def exportar(self, curso):
        horario = curso.curso_hor
        with open(self.path, 'w') as a_file:
            writer = csv.writer(a_file)
            for hora in horario:
                 writer.writerow([str(hora)])

class QueryHorarioProfe(object):

    def __init__(self, path):
        self.path = path

    def exportar(self, profe):
        horarios = profe.profe_horas
        with open(self.path, 'w') as a_file:
           writer = csv.writer(a_file)
           for hora in horarios:
               writer.writerow([str(hora)])


def main(*args, **kwargs):

    engine = create_engine("sqlite://")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    neville = Alumno(nombre_alu="Neville", apellido_alu="Longbottom", edad_alu=17)
    harry = Alumno(nombre_alu="Harry", apellido_alu="Potter", edad_alu=18)
    luna = Alumno(nombre_alu="Luna", apellido_alu="Lovegood", edad_alu=19)
    cecilio = Alumno(nombre_alu="Cecilio", apellido_alu="Odol", edad_alu=19)

    curso_py = Curso(nombre_cur="Python")
    curso_py.alumnos.append(harry)
    curso_py.alumnos.append(neville)

    curso_py2 = Curso(nombre_cur="Advanced Python")
    curso_py2.alumnos.append(luna)
    curso_py2.alumnos.append(cecilio)

    curso_py3 = Curso(nombre_cur="Python Expert")
    curso_magia1 = Curso(nombre_cur="Magia 1")
    curso_magia1.alumnos.append(harry)
    curso_magia1.alumnos.append(luna)

    curso_magia2 = Curso(nombre_cur="Magia Avanzada")
    curso_magia3 = Curso(nombre_cur="Magia Experto")
    curso_magia3.alumnos.append(neville)
    curso_magia3.alumnos.append(cecilio)

    profe_roberto = Profesor(nombre_prof="Roberto", apellido_prof="Code")
    profe_severus = Profesor(nombre_prof="Severus", apellido_prof="Snape")
    profe_mine = Profesor(nombre_prof="Minerva", apellido_prof="McGonagall")

    lprimera = Horario(nombre_dia='Lunes', hora_d="03 AM", hora_h="05 AM")
    lprimera.curso = curso_py
    lprimera.profesor = profe_roberto
    lsegunda = Horario(nombre_dia='Lunes',hora_d="05 AM", hora_h="07 AM")
    lsegunda.curso = curso_py2
    lsegunda.profesor = profe_severus
    ltercera = Horario(nombre_dia='Lunes',hora_d="07 AM", hora_h="09 AM")
    ltercera.curso = curso_py3
    ltercera.profesor = profe_mine

    mprimera = Horario(nombre_dia='Martes', hora_d="03 AM", hora_h="05 AM")
    mprimera.curso = curso_magia1
    mprimera.profesor = profe_mine
    msegunda = Horario(nombre_dia='Martes',hora_d="05 AM", hora_h="07 AM")
    msegunda.curso = curso_magia2
    msegunda.profesor = profe_roberto
    mtercera = Horario(nombre_dia='Martes',hora_d="07 AM", hora_h="09 AM")
    mtercera.curso = curso_magia3
    mtercera.profesor = profe_severus

    session.add_all((curso_py, curso_py2, curso_py3, curso_magia1, curso_magia2, curso_magia3))

    session.add_all((neville,harry, luna, cecilio))

    session.add_all((profe_mine, profe_roberto, profe_severus))

    session.add_all((lprimera,lsegunda, ltercera, mprimera, msegunda, mtercera))

    session.commit()


    QueryAlumnosCurso('./query_AluCurso').exportar(curso_magia1)
 
    QueryHorarioCurso('./query_HoraCurso').exportar(curso_py)

    QueryHorarioProfe('./query_HoraProfe').exportar(profe_severus)




if __name__ == "__main__":
    main()