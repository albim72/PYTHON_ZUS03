from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Dict
import bcrypt


# --- Model użytkownika z hashem hasła ---
class User(BaseModel):
    email: EmailStr
    password_hash: str


# --- Prosta "baza danych" w pamięci ---
user_db: Dict[str, User] = {}


# --- Rejestracja użytkownika ---
def register():
    print("\n== Rejestracja ==")
    try:
        email = input("Email: ")
        password = input("Hasło (min. 6 znaków): ")

        if len(password) < 6:
            raise ValueError("Hasło musi mieć co najmniej 6 znaków.")

        if email in user_db:
            print("❌ Użytkownik już istnieje!")
            return

        # Haszujemy hasło
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        user = User(email=email, password_hash=password_hash)
        user_db[email] = user
        print("✅ Rejestracja zakończona sukcesem!")

    except ValidationError as e:
        print("❌ Błąd walidacji:")
        print(e)
    except ValueError as ve:
        print(f"❌ {ve}")


# --- Logowanie użytkownika ---
def login():
    print("\n== Logowanie ==")
    email = input("Email: ")
    password = input("Hasło: ")

    user = user_db.get(email)

    if user and bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        print(f"✅ Zalogowano jako {user.email}")
    else:
        print("❌ Nieprawidłowy email lub hasło!")


# --- Główne menu ---
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
