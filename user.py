
import json
import os
import hashlib
import secrets


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.score = 0
        self.attempted_quizzes = []

    def attempt_quiz(self, quiz_title, score):
        self.score = score

        self.attempted_quizzes.append({
            "quiz_title": quiz_title,
            "score": score
        })

    def display_user(self):
        print("User ID:", self.user_id)
        print("Username:", self.username)
        print("Score:", self.score)
        print("Attempted Quizzes:", self.attempted_quizzes)


# Registration function
def register_user():
    file_path = os.path.join(
        os.path.dirname(__file__), "data", "users.json"
    )

    with open(file_path, "r") as file:
        users = json.load(file)

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            return

    salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    ).hex()

    new_user = {
        "user_id": len(users) + 1,
        "username": username,
        "salt": salt,
        "password_hash": password_hash
    }

    users.append(new_user)

    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)

    print("Registration successful!")


# Login function
def login_user():
    file_path = os.path.join(
        os.path.dirname(__file__), "data", "users.json"
    )

    with open(file_path, "r") as file:
        users = json.load(file)

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username:

            password_hash = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode(),
                user["salt"].encode(),
                100000
            ).hex()

            if password_hash == user["password_hash"]:
                print("Login successful!")
                print("Welcome", username)
                return user

            print("Incorrect password!")
            return None

    print("Username not found!")
    return None
