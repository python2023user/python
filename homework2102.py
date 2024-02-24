from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float, MetaData, Table
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///cars.db', echo=False)
Base = declarative_base()
metadata = MetaData()
metadata.reflect(bind=engine)

# Automatically delete an existing table to clear the data.
if 'cars' in metadata.tables:
    table = Table('cars', metadata, autoload=True, autoload_with=engine)
    table.drop(engine)

# 1. Извличане на информация – направете таблицата с хранителни
# продукти “Cars" с 10 автомобила, които имат марка и цена в лева. Напишете
# SQL заявка, която извлича марките и цените на всички автомобили със
# стойност на цената над 50 000 лева

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    car = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f"<Car(car='{self.car}', price={self.price}, id={self.id})>"

Base.metadata.create_all(engine)
print("-> 1. Създаване на таблица с име cars и 10 стойности към нея.")

Session = sessionmaker(bind=engine)
session = Session()

car1 = Car(car='Audi A6', price=80000)
car2 = Car(car='Audi A8', price=120000)
car3 = Car(car='Shkoda Octavia', price=12000)
car4 = Car(car='Audi A7', price=113000)
car5 = Car(car='BMW 5 Gran Turismo', price=25000)
car6 = Car(car='Mercedes-Benz GLE', price=125000)
car7 = Car(car='Citroen C3', price=15000)
car8 = Car(car='Toyota Avensis', price=35000)
car9 = Car(car='Dodge Charger', price=65000)
car10 = Car(car='BMW X6', price=70000.00)

session.add_all([car1, car2, car3, car4, car5, car6, car7, car8, car9, car10])
session.commit()

cars = session.query(Car).all()
print("Всички коли в таблицата:")
for c in cars:
    print(f"{c.id}. Марка: {c.car} - {c.price:.2f} лв.")

cars = session.query(Car).filter(Car.price > 50000).all()
print("-> 1. Всички коли над 50 000 лв.:")
for c in cars:
    print(f"Марка: {c.car} - {c.price:.2f} лв.")

# 2. Изтриване на запис: Изтрийте всички автомобили от таблицата
# " Cars", които са с цена под 30 000 лева.

session.query(Car).filter(Car.price < 30000).delete()
print("-> 2. Изтриване на всички коли с цена под 30 000 лв.")
session.commit()
cars = session.query(Car).all()
print("-> 2. Всички коли в таблицата след изтриване:")
for c in cars:
    print(f"Марка: {c.car} - {c.price:.2f} лв.")

# 3. Добавяне на нов запис - Въведете нов автомобил в таблицата
# “Cars" със зададена марка и цена.

new_car = Car(car='Toyota Yaris', price=9000)
session.add(new_car)
print(f"-> 3. Добавена е нова марка '{new_car.car}' с цена {new_car.price} лв.")
cars = session.query(Car).all()
print("-> 3. Всички коли в таблицата след добавянето:")
for c in cars:
    print(f"Марка: {c.car} - {c.price:.2f} лв.")

# 4. Филтриране и сортиране - извлечете марките и цените на
# продуктите от таблицата "Cars", подредени в намаляващ ред
# по цената и филтрирани, така че да бъдат включени само тези
# с цена над 100 000 лева.

cars = session.query(Car).filter(Car.price > 100000).order_by(Car.price.desc()).all()
print("-> 4. Всички коли по-скъпи от 100 000 лв. подредени в намаляващ ред:")
for c in cars:
    print(f"Марка: {c.car} - {c.price:.2f} лв.")

## 
    
session.close()