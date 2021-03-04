from app import db
from tables import Person, House, ownership


# db.drop_all()
# db.create_all()


# DataIn = Person(name='Daniel', surname='Diaz Souto')
# MoreData = Person(name='Nadia', surname='Peruffo')
# ExtraData = Person(name='Diego', surname='Diaz Peruffo')

# db.session.add(DataIn)
# db.session.add(MoreData)
# db.session.add(ExtraData)

# db.session.commit()


# Hou = House(type='Detached', street='Hendon lane', market_price='200000.00', owner_id='2')
# Hou1= House(type='Flat', street='ballards lane', market_price='2000000.50', owner_id='1')

# db.session.add(Hou)
# db.session.add(Hou1)

# db.session.commit()

ls = Person.query.first()
ls.name='John'


db.session.commit()