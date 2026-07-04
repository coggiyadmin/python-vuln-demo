from starlette.responses import RedirectResponse
from starlette.requests import Request
async def oauth_redirect(request: Request):
    return RedirectResponse(request.query_params.get("next", ""))  # SINK CWE-601 Starlette
