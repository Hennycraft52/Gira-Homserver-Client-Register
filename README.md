# Gira Client Register

Dieses Repository enthält ein Python-Skript, das eine grafische Benutzeroberfläche (GUI) für die Anmeldung von Gira-Clients bietet und die Anfrage an einen API-Endpunkt sendet, um einen Token zu erhalten.

## Voraussetzungen

- Python 3.x installiert
- Die notwendigen Python-Pakete installieren:

  ```bash
  pip install -r requirements.txt
Anwendung starten
Öffne die Befehlszeile (Command Prompt) oder das Terminal.

Wechsle zum Verzeichnis, in dem das Skript liegt.

Starte die Anwendung mit dem Befehl:

bash
Copy code
python register.py
Konvertierung in eine ausführbare Datei (Optional)
Du kannst das Skript in eine ausführbare Datei umwandeln, um es ohne Python-Installation auszuführen. Installiere dazu pyinstaller:

bash
Copy code
pip install pyinstaller
Dann konvertiere das Skript mit:

bash
Copy code
pyinstaller --onefile --noconsole --icon=icons\icon.ico register.py
Die ausführbare Datei wird im dist-Verzeichnis erstellt.

Benutzung
Gib die IP-Adresse, den Benutzernamen, das Passwort und den Client-Identifier ein.
Klicke auf "Anfrage senden".
Kopiere den generierten Token aus dem angezeigten Dialogfenster.
Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die LICENSE Datei für weitere Details.
