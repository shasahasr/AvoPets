from firebase_admin import credentials, firestore, initialize_app

default_app = initialize_app(credentials.Certificate('key.json'))
db = firestore.client()
users_ref = db.collection('users')

def get_user_by_id(id):
    return users_ref.document(id).get()

def get_user_by_email(email):
    for user in users_ref.get():
        if email == user.get("email"):
            return user
    return None

def check_login(email, password):
    for user in users_ref.get():
        if email == user.get("email") and password == user.get("password"):
            return user.id
    return False

def register(email, password):
    for user in users_ref.get():
            if email == user.get('email'):
                return False
    
    new_user = users_ref.add({"email": email, "password": password, "pet": {"endurance": 100, "health": 100, "name": "pet name", "strength": 100}, "stats": {"mindfulness": 0, "running": 0, "weights": 0}})
    return new_user[1].id