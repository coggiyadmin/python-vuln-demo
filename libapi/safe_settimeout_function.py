"""TN — schedule callable, not string. cognium-dev #124."""
import threading

def schedule(fn, delay_ms: int) -> None:
    threading.Timer(delay_ms / 1000.0, fn).start()
