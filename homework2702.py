from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

engine = create_engine('sqlite:///dynamic_table.db', echo=False)
metadata = MetaData()
metadata.reflect(bind=engine)

for tname in metadata.tables:
    table = Table(tname, metadata, autoload=True, autoload_with=engine)
    table.drop(engine)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def create_dynamic_table():
    table_name = input("Enter table name: ")
    columns = []
    while True:
        col_name = input("Enter column name (or type 'done' to finish): ")
        if col_name.lower() == 'done':
            break
        col_type = input("Enter column type (Integer, String, Float): ")
        if col_type == 'Integer':
            columns.append((col_name, Integer))
        elif col_type == 'String':
            columns.append((col_name, String))
        elif col_type == 'Float':
            columns.append((col_name, Float))
        else:
            print("Invalid type. Please enter Integer, String, or Float.")

    attrs = {'__tablename__': table_name, 'id': Column(Integer, primary_key=True)}
    for col_name, col_type in columns:
        attrs[col_name] = Column(col_type)
    attrs['__repr__'] = lambda self: f"<{table_name}(id={self.id})>"
    DynamicTable = type(table_name, (Base,), attrs)

    Base.metadata.create_all(engine)
    return DynamicTable
DynamicTable = create_dynamic_table()
def insert_row(DynamicTable):
    print("Inserting a new row.")
    new_row = DynamicTable()
    for column in DynamicTable.__table__.columns:
        if column.name != 'id' and column.name != 'password':
            value = input(f"Enter value for {column.name}: ")
            setattr(new_row, column.name, value)
        elif column.name == 'password':
            value = input(f"Enter value for {column.name}: ")
            enc_pass = fernet.encrypt(value.encode())
            setattr(new_row, column.name, enc_pass)
    session.add(new_row)
    session.commit()
    print("Row inserted successfully.")

def update_row(DynamicTable):
    row_id = int(input("Enter the id of the row to update: "))
    row = session.query(DynamicTable).get(row_id)
    if row:
        for column in DynamicTable.__table__.columns:
            if column.name != 'id':
                new_value = input(f"Enter new value for {column.name} (leave blank to keep current): ")
                if new_value:
                    setattr(row, column.name, new_value)
        session.commit()
        print("Row updated successfully.")
    else:
        print("Row not found.")

def update_bycol(DynamicTable):
    row_id = input("Enter the column name to update: ")
    row_value = input("Enter current value: ")
    row_new_value = input("Enter new value: ")
    detect_value = session.query(DynamicTable).filter_by(**{row_id: row_value}).all()
    if detect_value:
        for column in DynamicTable.__table__.columns:
            if column.name == row_id:
                if row_new_value:
                    setattr(*detect_value, column.name, row_new_value)
                    print("Value changed to", row_new_value)
                else:
                    print("No new value detect")
                    menu()
    else:
        print(f"Row not found.")
        menu()
    menu()   

def delete_row(DynamicTable):
    row_id = int(input("Enter the id of the row to delete: "))
    row = session.query(DynamicTable).get(row_id)
    if row:
        session.delete(row)
        session.commit()
        print("Row deleted successfully.")
    else:
        print("Row not found.")

def delete_by_value(DynamicTable):
    row_id = input("Enter the column name to update: ")
    row_value = input("Enter current value: ")
    detect_value = session.query(DynamicTable).filter_by(**{row_id: row_value}).all()
    if detect_value:
        for dv in detect_value:
            session.delete(dv)
            session.commit()
        print("Succesfully deleted values")
    else:
        print("No values for delete")

def search(DynamicTable):
    row_id = input("Enter column name: ")
    row_value = input("Enter value: ")
    print(f"Loading results for column '{row_id}' and value '{row_value}'")
    detect_value = session.query(DynamicTable).filter_by(**{row_id: row_value}).all()
    for instance in detect_value:
        line = []
        for column in DynamicTable.__table__.columns:
            line.append(f"{column.key}: {getattr(instance, column.key)}")
        print(*line)
    if line == []:
        print("No results")

def list_row(DynamicTable):
    print("Loading list...")
    for instance in session.query(DynamicTable).all():
        line = []
        for column in DynamicTable.__table__.columns:
            line.append(f"{column.key}: {getattr(instance, column.key)}")
        print(*line)

def menu():
    while True:
        print("\n1. Insert row\n2. Update row\n3. Delete row\n4. List\n5. Search by value\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            insert_row(DynamicTable)
        elif choice == '2':
            print("\n1. Update by index\n2. Update by column\n3. Back")
            while True:
                choice = input("Enter your choice: ")
                if choice == '1':
                    update_row(DynamicTable)
                elif choice == '2':
                    update_bycol(DynamicTable)
                elif choice == '3':
                    break
        elif choice == '3':
            print("\n1. Delete by index\n2. Delete by value\n3. Back")
            while True:
                choice = input("Enter your choice: ")
                if choice == '1':
                    delete_row(DynamicTable)
                elif choice == '2':
                    delete_by_value(DynamicTable)
                elif choice == '3':
                    break
            
        elif choice == '4':
            list_row(DynamicTable)
        elif choice == '5':
            search(DynamicTable)
            
        elif choice == '6':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
