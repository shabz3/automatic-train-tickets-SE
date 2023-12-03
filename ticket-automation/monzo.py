import requests
import os
from telegram import send_message


# Replace with your actual client credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")
state_string = os.environ.get("STATE_STRING")

def monzo_auth():
    # Set up authorization URL to grant access
    auth_url = f'https://auth.monzo.com/?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&state={state_string}'

    send_message(auth_url)

def get_balance(authentication_code):
    # Retrieve the code from the redirect_uri

    # Exchange the code for an access token
    token_url = 'https://api.monzo.com/oauth2/token'

    token_params = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': authentication_code
    }

    response = requests.post(token_url, data=token_params)

    if response.status_code == 200:
        access_token = response.json().get('access_token')
        # Now you have the access_token to make API requests
        # Example API request to get account balance
        headers = {'Authorization': f'Bearer {access_token}'}
        balance_url = 'https://api.monzo.com/balance'
        balance_response = requests.get(balance_url, headers=headers)
        if balance_response.status_code == 200:
            balance_data = balance_response.json()
            print('Account Balance:', balance_data)
        else:
            print('Failed to fetch balance:', balance_response.text)
    else:
        print('Failed to retrieve access token:', response.text)


monzo_auth()