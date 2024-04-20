#!/usr/bin/env python3
"""
Session Based Authentication Module
"""
from uuid import uuid4
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
  """ session authentication class that inherits Auth"""
  def __init__(self) -> None:
    """class initialization"""
    super().__init__()
