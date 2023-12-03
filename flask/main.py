from flask import Flask, request
from monzo import get_balance

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/callback')
def callback():
    # Retrieve the 'code' parameter from the callback URL
    code = request.args.get('code')

    if code:
        # Process the received code (e.g., exchange it for an access token)
        # Here you can implement logic to exchange the code for an access token

        # You can now use the 'code' to make a POST request to exchange it for an access token

        # Example: Make a POST request to the Monzo token endpoint to exchange the code for an access token
        # Include necessary data like client_id, client_secret, redirect_uri, code, etc.
        # Make sure to handle this securely, such as storing sensitive data.

        # Once you obtain the access token, you can use it to make requests to the Monzo API

        # ... (Code to exchange 'code' for access token)
        get_balance(code)

        return f"Code received successfully. It is {code}. You can proceed to obtain the access token."
    else:
        return "No code received."

if __name__ == '__main__':
    app.run(debug=True)
