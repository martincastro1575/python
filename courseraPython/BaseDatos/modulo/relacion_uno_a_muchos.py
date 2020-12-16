from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    books = relationship("Book", order_by="Book.id", back_populates="author")

    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    isbn = Column(String)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return "{}".format(self.title)

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

j_rowling = Author(firstname='Joanne', lastname='Rowling')

j_rowling.books = [
    Book(
        isbn='9788498387087',
        title='Harry Potter y la Piedra Filosofal',
        description='La vida de Harry Potter cambia para siempre el ...'),
    Book(
        isbn='9788498382679',
        title='Harry Potter y la camara secreta',
        description='Tras derrotar una vez mas a lord Voldemort, ...')
        ]

print("Imprimiendo todos los libros")
print(j_rowling.books)

print("Imprimiendo un titulo del libro")
print(j_rowling.books[1].title)

session.add(j_rowling)
session.commit()
j_rowling = session.query(Author).filter_by(firstname='Joanne').one()

print("Despues de agregar la sesion")
print(j_rowling.books)

print("Ejemplos de Consulta en objetos relacionados")
# Devuelve el autor y libro para este isbn. Los imprimimos en pantalla.
for an_author, a_book in session.query(Author, Book).filter(Author.id==Book.author_id).filter(Book.isbn=='9788498387087').all():
    print(an_author)
    print(a_book)

print("Devuelve el autor del libro con este isbn.")
print(session.query(Author).join(Book).filter(Book.isbn=='9788498387087').all())

print("Devuelve los autores de los libros poniendo la condición explícitamente.")
print(session.query(Author).join(Book, Author.id==Book.author_id).all())
print("Devuelve los autores de los libros especificando la relación de izquierda a derecha.")
print(session.query(Author).join(Author.books).all())
print("Devuelve los autores de los libros para una relación específica.")
print(session.query(Author).join(Book, Author.books).all())
print("Devuelve los autores de los libros utilizando un string")
print(session.query(Author).join('books').all())
print("Devuelve el nombre del autor del libro utilizando un filtro exists.Es decir, si existe algún libro del autor")
stmt = exists().where(Book.author_id==Author.id)
for name, in session.query(Author.firstname).filter(stmt):
    print(name)

print("Devuelve el nombre del autor del libro utilizando un filtro any. Es decir, si el autor tiene algún libro")
for name, in session.query(Author.firstname).filter(Author.books.any()):
    print(name)

print("Devuelve el nombre del autor del libro utilizando un filtro like")
print("parecido a any solo que se le puede definir una condición,")
print("en este caso que el apellido del autor contenga la subcadena de texto Row.")
for name, in session.query(Author.firstname).filter(Author.books.any(Author.lastname.like('%Row%'))):
    print(name)

print("Devuelve los libros donde el autor no se llame Joanne")
print(session.query(Book).filter(~Book.author.has(Author.firstname=='Joanne')).all())

