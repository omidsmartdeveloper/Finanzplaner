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
    category = entry_income_category.get()
    data = load_data()
    data["einnahmen"].append({"amount": amount, "category": category})
    save_data(data)
    label_status.config(text="Einnahme hinzugefügt!", fg="green")

# Ausgaben hinzufügen
def add_expense():
    amount = float(entry_expense.get())
    category = entry_expense_category.get()
    data = load_data()
    data["ausgaben"].append({"amount": amount, "category": category})
    save_data(data)
    label_status.config(text="Ausgabe hinzugefügt!", fg="red")

# Diagramm anzeigen
def show_chart():
    data = load_data()
    income = sum(item["amount"] for item in data["einnahmen"])
    expense = sum(item["amount"] for item in data["ausgaben"])

    plt.bar(["Einnahmen", "Ausgaben"], [income, expense], color=["green", "red"])
    plt.title("Einnahmen vs. Ausgaben")
    plt.ylabel("Betrag (€)")
    plt.show()

# GUI erstellen
root = tk.Tk()
root.title("Finanzplaner")

# Statusanzeige
label_status = tk.Label(root, text="")
label_status.pack(pady=5)

# Eingabefelder für Einnahmen
tk.Label(root, text="Einnahme Betrag (€):").pack()
entry_income = tk.Entry(root)
entry_income.pack()

tk.Label(root, text="Einnahme Kategorie:").pack()
entry_income_category = tk.Entry(root)
entry_income_category.pack()

tk.Button(root, text="Einnahme hinzufügen", command=add_income).pack(pady=10)

# Eingabefelder für Ausgaben
tk.Label(root, text="Ausgabe Betrag (€):").pack()
entry_expense = tk.Entry(root)
entry_expense.pack()

tk.Label(root, text="Ausgabe Kategorie:").pack()
entry_expense_category = tk.Entry(root)
entry_expense_category.pack()

tk.Button(root, text="Ausgabe hinzufügen", command=add_expense).pack(pady=10)

# Button zum Diagramm anzeigen
tk.Button(root, text="Diagramm anzeigen", command=show_chart).pack(pady=20)

root.mainloop()








