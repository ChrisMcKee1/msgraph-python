# msgraph-python

This project is a Python application that displays a user's calendar events from Microsoft Graph using a Tkinter-based GUI. The application uses the Microsoft Authentication Library (MSAL) for Python to authenticate users and acquire tokens for accessing the Microsoft Graph API.

## Features

- Interactive user authentication using MSAL
- Fetch and display calendar events from Microsoft Graph
- Simple and user-friendly Tkinter GUI

## Prerequisites

- Python 3.6 or higher
- An Azure Tenant
- An Azure App Registration

## Setup

### 1. Azure App Registration

1. **Register an Application:**
   - Go to the [Azure portal](https://portal.azure.com/).
   - Navigate to `App registrations > New registration`.
   - Enter a name for your application.
   - Select `Accounts in this organizational directory only` for the supported account types.
   - Click `Register`.

2. **Configure Redirect URI:**
   - Under `Authentication`, click `Add a platform`.
   - Select `Mobile and desktop applications`.
   - Add `http://localhost` as the redirect URI.
   - Click `Configure`.

3. **API Permissions:**
   - Under `API permissions`, click `Add a permission`.
   - Select `Microsoft Graph`.
   - Select `Delegated permissions`.
   - Add the following permissions:
     - `User.Read`
     - `Calendars.Read`
     - Here is the link to the list event api [Event permissions](https://learn.microsoft.com/en-us/graph/api/calendar-list-events?view=graph-rest-1.0&tabs=http)
   - Click `Add permissions`.

4. **Client ID and Tenant ID:**
   - Note down the `Application (client) ID` and `Directory (tenant) ID` from the app registration overview page.

### 2. Environment Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/msgraph-python.git
   cd msgraph-python

2. Create a Virtual Environment

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a .env File:**
    - Create a `.env` file in the project root directory.
    - Add the following environment variables to the `.env` file:

      ```env
      CLIENT_ID=YOUR_CLIENT_ID
      TENANT_ID=YOUR_TENANT_ID
      ```

### 3. Run the Application

1. **Run the Application:**

    ```sh
    python calendar_app.py
    ```

2. **Sign in with your Microsoft account.**
    - The application will open a browser window for authentication.
    - Sign in with your Microsoft account and grant the required permissions.
    - The application will fetch and display your calendar events in a Tkinter window.

## Code Explanation

`calendar_app.py`

This script performs the following tasks:

1. Load Environment Variables:
    - Uses python-dotenv to load CLIENT_ID and TENANT_ID from a .env file.
1. Initialize MSAL Public Client:
    - Creates an instance of PublicClientApplication with the client ID and authority.
1. Acquire Token Interactively:
    - Prompts the user to sign in and acquire an access token using acquire_token_interactive.
1. Fetch Calendar Events:
    - Uses the access token to make an authenticated request to the Microsoft Graph API to fetch calendar events.
1. Display Events in Tkinter GUI:
    - Parses the JSON response and displays the calendar events in a Tkinter Treeview widget.

`requirements.txt`

This file lists the dependencies required for the project:

```env
msal
requests
python-dotenv
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
