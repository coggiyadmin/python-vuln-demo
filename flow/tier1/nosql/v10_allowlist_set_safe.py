# v10 allowlist-set
SAFE_IDS = {1, 2, 3}
def lookup(doc_id: int):
    if doc_id in SAFE_IDS:
        return {'id': doc_id}
