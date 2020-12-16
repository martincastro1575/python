from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased


Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, Sequence('author_id_seq'), primary_key = True)
    firstname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)

engine = create_engine('sqlite:///:memory:')

#Author.__table__
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
author = Author(firstname='Martin', lastname='Castro')
session.add(author)

session.add_all([
Author(firstname='John Ronald Reuel', lastname='Tolkien'),
Author(firstname='Jose', lastname='Hernandez')])

session.commit()


# Devuelve los autores ordenados por id. Imprimimos el nombre y el apellido de cada uno.
print("Query #1")
for instance in session.query(Author).order_by(Author.id):
    print(instance.firstname, instance.lastname)

# Devuelve el nombre y el apellido de cada autor y los imprimimos en pantalla.
print("Query #2")
for firstname, lastname in session.query(Author.firstname, Author.lastname):
    print(firstname, lastname)

# Devuelve el autor y el primer nombre del mismo. Imprimimos cada uno de estos datos.
print("Query #3")
for row in session.query(Author, Author.firstname).all():
    print(row.Author, row.firstname)

# Devuelve los autores, pero le asignamos una etiqueta al campo primer nombre.
# Luego imprimimos el valor de esa etiqueta.
print("Query #4")
for row in session.query(Author.firstname.label('firstname_label')).all():
    print(row.firstname_label)

# Devuelve el autor y el primer nombre del mismo. La diferencia con la Query 3 es que
# definimos un alias de la tabla. Imprimimos el autor.
print("Query #5")
author_alias = aliased(Author, name='author_alias')
for row in session.query(author_alias, author_alias.firstname).all():
    print(row.author_alias)

# Buscamos todos los autores, pero nos quedamos con los de las posiciones 2 y 3.
9# La notación es como el slicing de las listas en Python.
print("Query #6")
for an_author in session.query(Author).order_by(Author.id)[1:3]:
    print(an_author)

# Filtramos los autores por los que tienen como nombre Joanne y nos quedamos con el
# nombre del mismo.
print("Query #7")
for name, in session.query(Author.firstname).filter_by(firstname='Martin'):
    print(name)

# Igual a la consulta anterior, solo que filtramos por apellido del autor
print("Query #8")
for name, in session.query(Author.firstname).filter(Author.lastname=='Castro'):
    print(name)

# Filtramos autor por nombre y apellido
print("Query #9")
for an_author in session.query(Author).filter(Author.firstname=='Martin').filter(Author.lastname=='Castro'):
    print(an_author)

# Nos quedamos con la cantidad de autores que tienen como primer nombre Joanne
print("Query #10")
print(session.query(Author).filter(Author.firstname=='Martin').count())




# our_author = session.query(Author).filter_by(firstname='Martin').first()
# print(author is our_author)

# author = Author(firstname='Martin', lastname='Castro')
# author.firstname
# author.lastname
# author.id