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