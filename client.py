import requests

def send_request():
    url = 'https://simpleserver-bice.vercel.app/'
    response = requests.get(url)
    print(response.json())

if __name__ == '__main__':
    send_request()