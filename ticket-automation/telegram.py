import requests

def send_message(auth_url):
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = ''

    # Replace 'YOUR_CHAT_ID' with the chat ID where you want to send the message
    chat_id = ''

    # Create the message text containing the authentication URL
    message_text = f'Click the link to authenticate: {auth_url}'

    # URL for sending messages via the Telegram Bot API
    telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    # Parameters for sending a message to the specified chat ID
    params = {
        'chat_id': chat_id,
        'text': message_text
    }

    # Send the message to the Telegram chat
    response = requests.get(telegram_api_url, params=params)

    # Check the response status
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message. Status code:', response.status_code)
