"""Framework-idiom benign (WS-5.2) — ORM access that LOOKS risky but is safe.
SQLAlchemy + Django ORM bind parameters automatically. ZERO findings expected.
"""
from flask import request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("postgresql://localhost/app")


def find_user_sqlalchemy(name: str):
    with Session(engine) as s:
        # ORM expression language — `name` is bound, not interpolated.
        return s.execute(text("SELECT * FROM users WHERE name = :n"), {"n": name}).all()


def find_user_django(name):
    from django.contrib.auth.models import User
    # Django ORM parameterizes the lookup; no raw SQL.
    return User.objects.filter(username=name).values()
