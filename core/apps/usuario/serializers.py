import typing

from django.contrib.auth.models import User
from marshmallow import Schema, fields, types
from typing_extensions import Required


class UsuarioSerializer(Schema):
    nome = fields.Str(required=True, allow_none=False, allow_blank=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True, allow_none=False, allow_blank=False)
    password2 = fields.Str(required=True, allow_none=False, allow_blank=False)

    def validate(
        self,
        data: typing.Union[
            typing.Mapping[str, typing.Any],
            typing.Iterable[typing.Mapping[str, typing.Any]],
        ],
        *,
        many: typing.Optional[bool] = None,
        partial: typing.Optional[typing.Union[bool, types.StrSequenceOrSet]] = None
    ) -> typing.Dict[str, typing.List[str]]:
        result = super().validate(data, many=many, partial=partial)

        user_email_validate = User.objects.filter(email=data.get("email")).exists()
        
        user_name_validate = User.objects.filter(username=data.get("nome")).exists()

        if user_email_validate or user_name_validate:
            result.update({"errors": [{"email": "E-mail already registered"}]})
            return result
        elif not data.get("password") == data.get("password2"):
            result.update({"errors": [{"password": "passwords do not match"}]})
            return result
        else:
            return result


class LoginSerializer(Schema):
    email = fields.Email(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False, allow_blank=False)

    def validate(
        self,
        data: typing.Union[
            typing.Mapping[str, typing.Any],
            typing.Iterable[typing.Mapping[str, typing.Any]],
        ],
        *,
        many: typing.Optional[bool] = None,
        partial: typing.Optional[typing.Union[bool, types.StrSequenceOrSet]] = None
    ) -> typing.Dict[str, typing.List[str]]:

        result = super().validate(data, many=many, partial=partial)

        user = User.objects.filter(
            email=data.get("email")
        )

        if not user.exists():
            result.update({"errors": [{"email": "E-mail not registered"}]})
            return result
        else:
            return result
