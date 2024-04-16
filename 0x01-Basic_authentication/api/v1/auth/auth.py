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

    def authorization_header(self, request=None) -> str:
        """authorization header method"""
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current user methid"""
        return None
