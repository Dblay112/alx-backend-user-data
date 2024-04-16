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
