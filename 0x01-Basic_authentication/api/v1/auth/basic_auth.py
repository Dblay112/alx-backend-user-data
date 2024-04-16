#!/usr/bin/env python3
"""
Basic Auth module.
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """Basic authentication class."""

    def __init__(self) -> None:
        """Initialization of BasicAuth class"""
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """Extract_base64_authorization_header method"""
        if not authorization_header \
                or not isinstance(authorization_header, str) \
                or authorization_header[:6] != 'Basic ':
            return None
        return " ".join(authorization_header.split(' ')[1:])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        basic user object.
        """
        if user_email is None or not isinstance(user_email, str) \
            or user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user.
        """
        authorization_header = self.authorization_header(request)

        base64_authorization_header = self.extract_base64_authorization_header(
            authorization_header)

        decoded_base64_authorization_header = self.decode_base64_authorization_header(
            base64_authorization_header)

        user_email, user_pwd = self.extract_user_credentials(
            decoded_base64_authorization_header)

        return self.user_object_from_credentials(user_email, user_pwd)
        return user
