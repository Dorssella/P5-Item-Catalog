from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, BookDB, User

engine = create_engine('postgresql://bookDB:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
DBconnection = DBSession()

# Create dummy user
User1 = User(name="admin", email="sagar.choudhary96@gmail.com")
DBconnection.add(User1)
DBconnection.commit()

# Dummy books data
book1 = BookDB(bookName = "The Year of Taking Chances", authorName = "Lucy Diamond", coverUrl = "https://books.google.com/books/content/images/frontcover/F9uIBAAAQBAJ?fife=w300-rw",
                description = "hello", category = "Romance", user_id = 1)

DBconnection.add(book1)
DBconnection.commit()

book2 = BookDB(bookName = "Summoner: The Inquisition: Book 2", authorName = "Taran Matharu", coverUrl = "https://books.google.com/books/content/images/frontcover/sQAfCgAAQBAJ?fife=w300-rw",
                description = "hello", category = "Fantasy", user_id = 1)

DBconnection.add(book2)
DBconnection.commit()

book3 = BookDB(bookName = "That's The Way We Met", authorName = "Sudeep Nagarkar", coverUrl = "https://books.google.com/books/content/images/frontcover/xE15t_pAG34C?fife=w300-rw",
                description = "hello", category = "Fiction", user_id = 1)

DBconnection.add(book3)
DBconnection.commit()

book4 = BookDB(bookName = "The Creep", authorName = "John Arcudi", coverUrl = "https://books.google.com/books/content/images/frontcover/fEI4qWTBoZMC?fife=w300-rw",
                description = "hello", category = "Mystery", user_id = 1)

DBconnection.add(book4)
DBconnection.commit()

book5 = BookDB(bookName = "Now That You're Rich: Let's fall in Love!", authorName = "Durjoy Datta", coverUrl = "https://books.google.com/books/content/images/frontcover/CDQnAgAAQBAJ?fife=w300-rw",
                description = "hello", category = "Romance", user_id = 1)

DBconnection.add(book5)
DBconnection.commit()


print "added Books!"
