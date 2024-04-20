#!/usr/bin/env python3
"""
Session Based Authentication Module
"""
from uuid import uuid4
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
  """ session authentication class that inherits Auth"""
  user_id_by_session_id = {}
  def __init__(self) -> None:
    """class initialization"""
    super().__init__()

  def create_session(self, user_id: str = None) -> str:
    """an instance method that creates a session for user id"""
    if not user_id or not isinstanceof(user_id, str):
      return None
    session_id = str(uuid.uuid4())
    self.user_id_by_session_id[session_id] = user_id
    return session_id
