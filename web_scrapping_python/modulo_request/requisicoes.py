import requests

response = requests.get('https://www.google.com')

print(f"\nStatus code: {response.status_code}")

print(f"\nHeader: {response.headers}")

print(f"\nContent: {response.content}")
