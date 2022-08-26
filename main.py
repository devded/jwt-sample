import uuid
import secrets
import jwt
import json
import time

class SignUp:
  def __init__(self):
    self.user_id = self._generate_user_id()
    self.access_token = self._generate_access_token()
    self.refresh_token = self._generate_refresh_token()
    self.expired_at = self._generate_expired_at()
    self.jwt_token = self._generate_jwt_token()
    

  def save(self):
    # print(self.user_id)
    # print(self.access_token)
    # print(self.refresh_token)
    # print(self.expired_at)
    print(self.jwt_token)


  def _generate_user_id(self):
    self.user_id = str(uuid.uuid4())
    return self.user_id


  def _generate_access_token(self):
    self.access_token = secrets.token_hex(20)
    return self.access_token

  def _generate_refresh_token(self):
    self.refresh_token = secrets.token_hex(30)
    return self.refresh_token

  def _generate_jwt_token(self):
    data = {
        "user_id": self.user_id,
        "access_token": self.access_token,
        "refresh_token": self.refresh_token,
        "expired_at": self.expired_at
      }
    key = "secret"
    return jwt.encode(data, key , algorithm="HS256")

  def _generate_expired_at(self):
    self.expired_at = int(time.time())
    return self.expired_at



SignUp().save()


def decoded_jwt(encoded_jwt):
  key="secret"
  decoded_jwt = jwt.decode(encoded_jwt, key , algorithms=["HS256"])
  print(decoded_jwt)


print(decoded_jwt("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiZGY1MGExZjEtM2VjYi00OTg0LWE4OWMtNjlhODg5MmE5MzRlIiwiYWNjZXNzX3Rva2VuIjoiYTY2ODIwYjE0YmE3NmQ5NDQ5YmUxZjJhZTJjM2RjZmQ2M2M1ZTY3YiIsInJlZnJlc2hfdG9rZW4iOiJhMTkyZTM2ZDNlMjY4YzY0MWJkM2E4OGQxMzg2NmYwYzA4OWQxNDFkY2VkMmFjM2ViNzdkY2Y2ZmRlMjkifQ.YAxqFc0JMmaKb0GDsXzGttIhek3dfihLkMsZHX3x1MY"))

