#!/usr/bin/env python3
"""module"""
from flask import Blueprint, abort

blueprint = Blueprint('index', __name__)


@blueprint.route('/api/v1/unauthorized')
def unauthorized_endpoint():
    """unauthorized endpoint method"""
    abort(401)
    
def register_views(app):
    """register views method"""
    app.register_blueprint(blueprint)
