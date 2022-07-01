from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from backend.core.middlewares import ProcessTimeMiddleware, ActivityLoggerMiddleWare
from .core.config import settings
from .router import router


def get_application() -> FastAPI:
    _app = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    _app.add_middleware(ProcessTimeMiddleware)
    _app.add_middleware(
        PrometheusMiddleware,
        app_name=settings.PROJECT_NAME,
        group_paths=True,
        prefix="kommatipara",
        filter_unhandled_paths=True,
        skip_paths=[
            '/healthcheck/readiness',
            '/healthcheck/liveness',
            '/healthcheck/startup',
            '/metrics',
            '/docs',
            '/redoc',
            '/openapi.json',
        ],
    )
    _app.add_middleware(ActivityLoggerMiddleWare)
    _app.add_route("/metrics", handle_metrics)

    _app.include_router(router, prefix=settings.API_V1_STR)

    return _app


app = get_application()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=9000)
