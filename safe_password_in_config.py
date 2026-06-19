"""SAFE mirror — password_in_config.py; credentials read from the environment, none
hardcoded. Expect 0 security findings."""
import os

DB_HOST = "db.internal"
DB_USER = "app"
DB_PASSWORD = os.environ["DB_PASSWORD"]     # injected at runtime, not in source
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
DEBUG = False
