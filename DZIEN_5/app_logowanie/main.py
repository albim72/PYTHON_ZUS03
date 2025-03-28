from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Dict
import getpass


# --- Model użytkownika ---
class User(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)


# --- Prosta "baza danych" w pamięci ---
user_db: Dict[str, User] = {}


# --- Rejestracja ---
def register():
    print("\n== Rejestracja ==")
    try:
        email = input("Email: ")
        password = getpass.getpass("Hasło (min. 6 znaków): ")
        user = User(email=email, password=password)
        if email in user_db:
            print("❌ Użytkownik już istnieje!")
        else:
            user_db[email] = user
            print("✅ Rejestracja zakończona sukcesem!")
    except ValidationError as e:
        print("❌ Błąd walidacji:")
        print(e)


# --- Logowanie ---
def login():
    print("\n== Logowanie ==")
    email = input("Email: ")
    password = getpass.getpass("Hasło: ")

    user = user_db.get(email)
    if user and user.password == password:
        print(f"✅ Zalogowano jako {user.email}")
    else:
        print("❌ Nieprawidłowy email lub hasło!")


# --- Główna pętla programu ---
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Rejestracja")
        print("2. Logowanie")
        print("3. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()
