import os

from fastapi.middleware.cors import CorsMiddleware


class CorsConfig:

    @classmethod
    def middlewareConfig(self, app):
        origins = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
        app.add_middleware(
            CorsMiddleware,
            allow_origins=origins,
            allow_credentials = True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
