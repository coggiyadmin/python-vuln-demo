from starlette.responses import RedirectResponse
from starlette.requests import Request
async def redirect_view(request: Request):
    nxt = request.query_params.get("next", "")
    return RedirectResponse(nxt)  # SINK CWE-601 Starlette redirect
