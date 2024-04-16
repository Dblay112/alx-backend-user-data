#!/usr/bin/env python3
"""
Module for aunthentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Base authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth method"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        path = path.rstrip("/")
        excluded_paths = [p.rstrip("/") for p in excluded_paths]
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False
        return True


    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """
        method to decode the value of a Base64 string base64_authorization_header
        """
        try:
            base64_bytes = base64_authorization_header.encode("utf-8")

            string_bytes_base64 = base64.b64decode(base64_bytes)

            return string_bytes_base64.decode("utf-8")

        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        method that returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str) or \
           ':' not in decoded_base64_authorization_header:
            return None, None

        pos = decoded_base64_authorization_header.find(':')

        email = decoded_base64_authorization_header[:pos]
        password = decoded_base64_authorization_header[pos + 1:]

        return email, password

    def authorization_header(self, request=None) -> str:
        """authorization header method"""
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current user methid"""
        return None
