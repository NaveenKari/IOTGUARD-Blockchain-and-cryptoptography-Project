import requests

def Mine():
    # Replace the URL with the address of your Flask app
    url = 'http://127.0.0.1:5000/mine_block'

    # Send a GET request to mine a block
    response = requests.get(url)
    # Print the response from the server
    

Mine()