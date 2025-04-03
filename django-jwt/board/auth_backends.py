import jwt
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# token 출력용 코드
class MyOIDCBackend(OIDCAuthenticationBackend):
    def get_userinfo(self, access_token, id_token, payload):
        print("ACCESS TOKEN (raw):", access_token[:100], "...")
        print("ID TOKEN (raw):", id_token[:100], "...")
        print("PAYLOAD:", payload) # id token의 payload

        # Access token 디코드 (서명 검증 생략)
        try:
            decoded_access = jwt.decode(access_token, options={"verify_signature": False})
            print(" ACCESS TOKEN DECODED:", decoded_access)
        except Exception as e:
            print("ACCESS TOKEN DECODE ERROR:", e)

        return super().get_userinfo(access_token, id_token, payload)
