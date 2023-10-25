from models import User, Comment
from main import session

user1 = User(
    username='Borna',
    email_address="bornam@sql.org",
    comments=[
        Comment(text="Hello World"),
        Comment(text="SQLAlchemy testing")
    ]
)

paul = User(
    username='paul',
    email_address="paul@sql.org",
    comments=[
        Comment(text="Whats up?"),
        Comment(text="SQLAlchemy testing1")
    ]
)


cathy = User(
    username='cathy',
    email_address="cathy@sql.org"
)

session.add_all([user1,paul,cathy])

session.commit()