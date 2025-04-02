import jwt
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class MyOIDCBackend(OIDCAuthenticationBackend):
    def get_userinfo(self, access_token, id_token, payload):
        print("ACCESS TOKEN (raw):", access_token[:100], "...")
        print("ID TOKEN (raw):", id_token[:100], "...")
        print("PAYLOAD:", payload)

        # Access token 디코드 (서명 검증은 생략)
        try:
            decoded_access = jwt.decode(id_token, options={"verify_signature": False})
            print(" ID TOKEN DECODED:", decoded_access)
        except Exception as e:
            print("ID TOKEN DECODE ERROR:", e)

        return super().get_userinfo(access_token, id_token, payload)
