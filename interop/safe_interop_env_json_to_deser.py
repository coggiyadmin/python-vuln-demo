"""SAFE — constant pickle bytes only."""
import pickle

def load():
    pickle.loads(pickle.dumps({"ok": True}))
