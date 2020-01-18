from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents objects loaded into the
# database session object. 
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="Jazzmeus1970@gmail.com")
session.add(User1)
session.commit()

# Menu for Michael Kitchen
restaurant1 = Restaurant(name="=Michael's Kitchen", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="hot dogs",
                     description="bun with hotdog"
                     "served with ketchup your choice of condements.",
                     price="$2.99", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Michael's hamburgers",
                     description=" beef pattie served with a tasty bun."
                     "add a soup your choice.",
                     price="$5.50",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Michael's Pizza",
                     description="Michael's delicious hand spun pizaa"
                     "Your choice of toppings.",
                     price="$5.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for Joe's Famous place
restaurant2 = Restaurant(name="Joe's Famous place")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Joes famous chilli dogs",
                     description="Home made chilli a touch of spice.",
                     price="$7.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Joes famous Hamton lobster",
                     description="lobster served with either soup, salad, or bowl"
                     "layered with vegetables and a tangy sauce.",
                     price="$25",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Joes hand spun origianl",
                     description="Joes hand spun home made pizza"
                     "made with Mama's secret sauce.",
                     price="$15", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


print "Added menu items!"
