"""CWE-260 — Password in Configuration File. A real credential sits in a tracked
config module. Real vuln; NO finding = FALSE NEGATIVE. (CWE-798 family.)"""

# application configuration
DB_HOST = "db.internal"
DB_USER = "app"
DB_PASSWORD = "Pr0d-DB-pass!2024"     # hardcoded credential in config → CWE-260
SMTP_PASSWORD = "smtp-s3cret-key"     # hardcoded credential in config → CWE-260
DEBUG = False
