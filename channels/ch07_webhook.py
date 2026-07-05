"""CH-07 webhook — payload field -> shell."""
import os
def on_webhook(event):
    name = event['repository']['name']  # SOURCE webhook body
    os.system('git clone /srv/' + name)  # SINK CWE-78
