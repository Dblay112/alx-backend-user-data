#!/usr/bin/env python3
"""
Basic Auth module.
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
  """base class for basic authentication
  inherits Auth class
  """
  pass  
