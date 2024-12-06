import tkinter as tk
import json
import matplotlib.pyplot as plt

# Daten laden oder initialisieren
def load_data():
    try:
        with open("finanzen.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"einnahmen": [], "ausgaben": []}

# Daten speichern
def save_data(data):
    with open("finanzen.json", "w") as file:
        json.dump(data, file)

# Einnahmen hinzufügen
def add_income():
    amount = float(entry_income.get())
    data = load_data()
    data["einnahmen"].append(amount)
    save_data(data)

# Ausgaben hinzufügen
def add_expense():
    amount = float(entry_expense.get())
    data = load_data()
    data["ausgaben"].append(amount)
    save_data(data)

# Diagramm anzeigen
def show_chart():
    data = load_data()
    income = sum(data["einnahmen"])
    expense = sum(data["ausgaben"])

    plt.bar(["Einnahmen", "Ausgaben"], [income, expense], color=["green", "red"])
    plt.title("Einnahmen vs. Ausgaben")
    plt.show()

# GUI erstellen
root = tk.Tk()
root.title("Finanzplaner")

# Eingabefelder für Einnahmen
tk.Label(root, text="Einnahme Betrag").pack(pady=5)
entry_income = tk.Entry(root)
entry_income.pack(pady=5)
tk.Button(root, text="Einnahme hinzufügen", command=add_income).pack(pady=10)

# Eingabefelder für Ausgaben
tk.Label(root, text="Ausgabe Betrag").pack(pady=5)
entry_expense = tk.Entry(root)
entry_expense.pack(pady=5)
tk.Button(root, text="Ausgabe hinzufügen", command=add_expense).pack(pady=10)

# Button zum Diagramm anzeigen
tk.Button(root, text="Diagramm anzeigen", command=show_chart).pack(pady=20)

root.mainloop()








