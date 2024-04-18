#!/usr/bin/env python3
"""
module for authentication
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """
    base class for authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        docs
        """
        if not path or not excluded_paths:
            return True

        path_with_slash = path if path.endswith('/') else path + '/'

        if path_with_slash in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header method
        """
        if not request:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current active user.
        """
        return None
