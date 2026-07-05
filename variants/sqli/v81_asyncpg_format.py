from aiohttp import web
import asyncpg
async def get_user(request):
    name = request.query.get("name", "")  # SOURCE
    conn = await asyncpg.connect()
    return web.json_response(await conn.fetch(
        "SELECT * FROM users WHERE name = '%s'" % name))  # SINK CWE-89 asyncpg %-format
