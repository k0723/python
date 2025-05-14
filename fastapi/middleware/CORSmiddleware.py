from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import HTTPException

class CORSmiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        allowed_origins = [
            "http://localhost:8000",
            # 다른 허용하는 출처 추가 가능
        ]
        origin = request.headers.get('origin')
        if origin in [None, 'null', 'none']:
            # 차단이 먼저인 기존 로직과 다르게, 허용하는 경우
            response = await call_next(request)
            return response
        # 'http://localhost:8000'에서 온 요청만 허용
        if origin not in allowed_origins:
            return JSONResponse(
                status_code=403,
                content={"detail": "허용되지 않는 출처입니다."}
            )
        response = await call_next(request)
        return response