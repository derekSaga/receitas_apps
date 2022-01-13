import typing

from django.contrib.auth.models import User
from marshmallow import Schema, fields


class UsuarioSerializer(Schema):
    nome = fields.Str(required=True, allow_none=False, allow_blank=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True, allow_none=False, allow_blank=False)
    password2 = fields.Str(required=True, allow_none=False, allow_blank=False)

    def validate(
        self, data, many=None, partial=None
    ) -> typing.Dict[str, typing.List[str]]:
        result = super().validate(data, many=many, partial=partial)

        if User.objects.filter(email=data.get("email")):
            return result.update({"errors": [{"email": "E-mail already registered"}]})
        elif not data.get("password") == data.get("password2"):
            result.update({"errors": [{"password": "passwords do not match"}]})
            return result
        else:
            return result
