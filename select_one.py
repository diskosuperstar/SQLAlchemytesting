from main import session
from models import User

Borna = session.query(User).filter_by(username = 'paul').first()

print(Borna)
