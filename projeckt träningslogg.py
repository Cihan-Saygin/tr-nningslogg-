import json

FILENAME = "training_log.json"

def load_log():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_log(log):
    with open(FILENAME, "w") as f:
        json.dump(log, f, indent=4)

def add_session(log):
    session_data = {
        "Date": input("Date (YYYY-MM-DD): "),
        "Type": input("Type of training: "),
        "Duration": input("Duration (minutes): ")
    }
    log.append(session_data)
    save_log(log)
    print("Träningspass sparat!\n")

def show_log(log):
    if log:
        print("\nTräningslogg:")
        for session_data in log:
            print(f"{session_data['Date']} - {session_data['Type']} - {session_data['Duration']} min")
        print()
    else:
        print("Ingen träningsdata registrerad.\n")

def main_menu():
    log = load_log()

    while True:
        print("1. Lägg till träningspass\n2. Visa träningslogg\n3. Avsluta")
        choice = input("Välj ett alternativ: ")

        if choice == "1":
            add_session(log)
        elif choice == "2":
            show_log(log)
        elif choice == "3":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.\n")

main_menu()
