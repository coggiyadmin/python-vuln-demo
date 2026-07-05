import redis, subprocess
r = redis.Redis()
def handle(key):
    v = r.get(key).decode()  # SOURCE cache read (second-order)
    subprocess.call("echo " + v, shell=True)  # SINK
