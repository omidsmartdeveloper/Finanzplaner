# Finanzplaner

Finanzplaner - Python Anwendung
Projektbeschreibung

Der Finanzplaner ist eine einfache Python-Anwendung, die es Nutzern ermöglicht:

Einnahmen und Ausgaben zu erfassen.
Die Daten in einer JSON-Datei zu speichern.
Die Einnahmen und Ausgaben in einem übersichtlichen Balkendiagramm zu visualisieren.

Die Anwendung wurde mit Python und den Modulen tkinter, json und matplotlib umgesetzt.
Installation
Voraussetzungen:

Python 3.x installiert
Die folgenden Python-Module:
                 
tkinter(Standardmodul, keine separate Installation nötig)
matplotlib (installierbar mit  pip install matplotlib)

Klone das Repository oder lade die Dateien herunter.
Stelle sicher, dass alle Abhängigkeiten installiert sind:

    pip install matplotlib

Starte die Anwendung:

    python finanzplaner.py

Funktionen

Einnahmen hinzufügen:
Erfassen Sie Einnahmen mit dem entsprechenden Betrag und speichern Sie diese.

Ausgaben hinzufügen:
Erfassen Sie Ausgaben mit dem entsprechenden Betrag und speichern Sie diese.

Diagramm anzeigen:
Visualisieren Sie die Gesamtsummen der Einnahmen und Ausgaben in einem Balkendiagramm.

Dateistruktur

finanzplaner.py: Der Hauptprogrammcode.
finanzen.json: Die Datei, in der alle Einnahmen und Ausgaben gespeichert werden (wird automatisch erstellt, falls sie nicht existiert).

Bedienung

Öffnen Sie das Programm.
Geben Sie die Einnahmen oder Ausgaben in das entsprechende Textfeld ein und klicken Sie auf den jeweiligen Button, um die Daten zu speichern. Um eine Übersicht zu erhalten, klicken Sie auf den Button "Diagramm anzeigen".

Beispielbilder
Beispiel für die GUI:

Beispiel für das Diagramm:

Bekannte Probleme

Falls eine fehlerhafte Eingabe (z. B. Buchstaben statt Zahlen) gemacht wird, stürzt das Programm ab. Dieses Problem könnte durch eine Eingabeprüfung gelöst werden.

Weiterentwicklung

Hinzufügen einer Kategorie für Einnahmen und Ausgaben.
Exportieren der Daten in eine Excel- oder CSV-Datei.
Einfügen von Fehlerüberprüfungen für Eingaben.

Autoren

    Omid 
    Kontakt: omid.kabirzad@gmail.com
