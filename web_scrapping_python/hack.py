import hashlib
import requests

password = "1"

# result = hashlib.md5(password.encode())

# print(result.hexdigest())

# c4ca4238a0b923820dcc509a6f75849b
# c81e728d9d4c2f636f067f89cc14862c

def get():
    return requests.get("http://83.136.253.251:31885/download.php?contract=MjA%3D")

response = get()

print(response.text)