import jwt

data = {
  "some": "payload",
  "user_id": "12122121",
  "access_token": "dhadhashdhasd3123",
  "user_package": "lite"
}
key = "secret"



encoded_jwt = jwt.encode(data, key , algorithm="HS256")
print(encoded_jwt)

decoded_jwt = jwt.decode(encoded_jwt, key , algorithms=["HS256"])

print(decoded_jwt)
