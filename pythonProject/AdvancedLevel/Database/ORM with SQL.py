from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base model
Base = declarative_base()


# Define the ORM model (SQL table)
class User(Base):
    __tablename__ = 'users'  # This maps to the 'users' table in the database

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Email = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User(name={self.Name}, email={self.Email})>"

# Connection string for SQL Server using pyodbc
server = '192.168.0.30'  # e.g., 'localhost\\SQLEXPRESS' or your SQL Server IP
database = 'Anupama'
username = 'User11'
password = 'CDev011@gfh'

# SQLAlchemy connection string using pymssql driver
connection_string = f"mssql+pymssql://{username}:{password}@{server}:1433/{database}"

# Create a SQLAlchemy engine
engine = create_engine(connection_string, echo=True)

# Create the 'users' table (if it doesn't exist already)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example of creating and inserting a new User
new_user = User(Name="John Doe", Email="johndoe@example.com")
session.add(new_user)
session.commit()

# Query to fetch all users
Users = session.query(User).all()
for user in Users:
    print(user)

# Close the session
session.close()


