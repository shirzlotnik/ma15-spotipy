from json import load
from os import getenv
from typing import Dict, Optional
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

users = {}
login_manager = LoginManager()
