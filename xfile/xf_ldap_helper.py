"""Cross-file taint — SINK side (LDAP injection). Imported by xf_ldap_controller.py."""
import ldap

conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


def search(user: str):
    # SINK: `user` arrives tainted across the file boundary → LDAP injection (CWE-90)
    return conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")
