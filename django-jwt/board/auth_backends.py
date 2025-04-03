import jwt
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# token 출력용 코드
class MyOIDCBackend(OIDCAuthenticationBackend):
    def get_userinfo(self, access_token, id_token, payload):
        # Access token 디코딩
        try:
            decoded_access = jwt.decode(access_token, options={"verify_signature": False})
            print(" ACCESS TOKEN DECODED:", decoded_access)
        except Exception as e:
            print("ACCESS TOKEN DECODE ERROR:", e)

        # payload만 리턴하면 /userinfo를 호출하지 않음
        return payload
    
        # /userinfo를 호출할 때 사용  
        # return super().get_userinfo(access_token, id_token, payload)
