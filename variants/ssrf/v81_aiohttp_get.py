from aiohttp import web, ClientSession
async def fetch(request):
    url = request.query.get("url", "")  # SOURCE
    async with ClientSession() as s:
        async with s.get(url) as resp:  # SINK CWE-918 aiohttp client
            return web.Response(text=await resp.text())
