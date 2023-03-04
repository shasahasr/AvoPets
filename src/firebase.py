import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyA4w-h8doZxkAHnWHujzuLh_ITFkVZc2ow",
    'authDomain': "avopets-abb9b.firebaseapp.com",
    'databaseURL': "https://avopets-abb9b-default-rtdb.firebaseio.com",
    'projectId': "avopets-abb9b",
    'storageBucket': "avopets-abb9b.appspot.com",
    'messagingSenderId': "54079669236",
    'appId': "1:54079669236:web:563b79f20978b9f470afa1",
    'measurementId': "G-R7QWE9FVVF"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#Login function

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']
       # print(email)
    except:
        print("Invalid email or password")
    return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

#Main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()
