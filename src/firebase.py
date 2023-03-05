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
    if email == "" or password == "":
        return False

    for user in users_ref.get():
        if email == user.get("email") and password == user.get("password"):
            return user.id
    return False

def register(email, password):
    if email == "" or password == "":
        return False

    for user in users_ref.get():
            if email == user.get('email'):
                return False
    
    new_user = users_ref.add({"email": email, "password": password, "pet": {"endurance": 100, "health": 100, "name": "pet name", "strength": 100, "neededxp": 100, "currentxp": 0, "currentlevel": 1}, "stats": {"mindfulness": 0, "running": 0, "weights": 0}})
    return new_user[1].id

def add_xp(user_id, xp):
    user = get_user_by_id(user_id).to_dict()
    user["pet"]["currentxp"] += xp
    if user["pet"]["currentxp"] > user["pet"]["neededxp"]:
        user["pet"]["currentlevel"] += 1
        user["pet"]["currentxp"] = user["pet"]["currentxp"] % user["pet"]["neededxp"]
        user["pet"]["neededxp"] *= 1.2

        user["pet"]["health"] *= 1.2
        user["pet"]["endurance"] *= 1.2
        user["pet"]["strength"] *= 1.2
    users_ref.document(user_id).set(user)

def add_strength(user_id, strength):
    user = get_user_by_id(user_id).to_dict()
    user["pet"]["strength"] += strength
    users_ref.document(user_id).set(user)

def add_endurance(user_id, endurance):
    user = get_user_by_id(user_id).to_dict()
    user["pet"]["endurance"] += endurance
    users_ref.document(user_id).set(user)

def add_health(user_id, mindfulness):
    user = get_user_by_id(user_id).to_dict()
    user["pet"]["health"] += mindfulness
    users_ref.document(user_id).set(user)