from flask import Flask, request
import motor.motor_asyncio
app = Flask(__name__)
client = motor.motor_asyncio.AsyncIOMotorClient()
@app.route("/m")
async def m():
    name = request.args.get("name", "")
    await client.app.users.find({"$where": "this.n == '" + name + "'"}).to_list(10)  # SINK CWE-943 motor $where
