import msal
import requests
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration
CLIENT_ID = os.getenv('CLIENT_ID')
TENANT_ID = os.getenv('TENANT_ID')
AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPE = ['User.Read', 'Calendars.Read']
ENDPOINT = 'https://graph.microsoft.com/v1.0/me/events'

# Initialize the MSAL public client
app = msal.PublicClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
)

# Acquire a token interactively
result = app.acquire_token_interactive(scopes=SCOPE)

if 'access_token' in result:
    # Make a request to the Graph API
    headers = {
        'Authorization': 'Bearer ' + result['access_token']
    }
    response = requests.get(ENDPOINT, headers=headers)

    if response.status_code == 200:
        events = response.json().get('value', [])
    else:
        print(f"Error fetching events: {response.status_code}")
        events = []
else:
    print("Error acquiring token.")
    events = []

# Create the Tkinter UI
root = tk.Tk()
root.title("Calendar Events")

tree = ttk.Treeview(root, columns=('Subject', 'Start', 'End'), show='headings')
tree.heading('Subject', text='Subject')
tree.heading('Start', text='Start')
tree.heading('End', text='End')

for event in events:
    tree.insert('', tk.END, values=(event['subject'], event['start']['dateTime'], event['end']['dateTime']))

tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()