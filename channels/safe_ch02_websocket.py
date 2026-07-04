"""TN — WebSocket payload HTML-escaped."""
import html
def on_message(ws, message):
    return "<p>" + html.escape(message) + "</p>"
