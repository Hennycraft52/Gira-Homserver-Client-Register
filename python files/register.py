import tkinter as tk
from tkinter import messagebox
import requests
import base64
import pyperclip

def send_request():
    ip = ip_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    client_identifier = client_entry.get()

    url = f"https://{ip}/api/v2/clients"

    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }

    data = {"client": client_identifier}

    config = {
        "timeout": 10,
        "verify": False,
    }

    try:
        response = requests.post(url, headers=headers, json=data, **config)
        if response.status_code == 200:
            token = response.json().get('token', 'Token not found')
            token_entry.config(state=tk.NORMAL)  # Aktiviere das Feld
            token_entry.delete(0, tk.END)  # Lösche vorherigen Token
            token_entry.insert(tk.END, token)  # Zeige den Token im GUI an
            token_entry.config(state=tk.DISABLED)  # Deaktiviere das Feld wieder
            messagebox.showinfo("Erfolgreiche Anfrage", "Erfolgreiche Anfrage!\nToken wurde empfangen und im Feld angezeigt.")
        else:
            messagebox.showerror("Fehler bei der Anfrage", f"Fehler bei der Anfrage. Statuscode: {response.status_code}\nAntwort:\n{response.text}")
    except requests.RequestException as e:
        messagebox.showerror("Fehler", f"Fehler bei der Anfrage: {str(e)}")

def copy_token():
    token = token_entry.get()
    if token:
        pyperclip.copy(token)
        messagebox.showinfo("Token kopiert", "Token wurde in die Zwischenablage kopiert.")
    else:
        messagebox.showwarning("Kein Token", "Es gibt keinen Token zum Kopieren.")

# GUI erstellen
root = tk.Tk()
root.title("Gira-Client-Register")



# Labels
ip_label = tk.Label(root, text="IP:")
username_label = tk.Label(root, text="Benutzername:")
password_label = tk.Label(root, text="Passwort:")
client_label = tk.Label(root, text="Client Identifier:")
token_label = tk.Label(root, text="Token:")

# Entry-Felder
ip_entry = tk.Entry(root, width=30)
username_entry = tk.Entry(root, width=30)
password_entry = tk.Entry(root, width=30, show='*')  # show='*' for password masking
client_entry = tk.Entry(root, width=30)
token_entry = tk.Entry(root, width=30, state=tk.DISABLED)  # Das Token-Feld ist schreibgeschützt

# Button zum Senden der Anfrage
send_button = tk.Button(root, text="Anfrage senden", command=send_request)

# Copy Token Button
copy_button = tk.Button(root, text="Copy Token", command=copy_token)

# Layout
ip_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
client_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
token_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

ip_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
client_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
token_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

send_button.grid(row=5, column=0, columnspan=2, pady=10)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)

# GUI starten
root.mainloop()
