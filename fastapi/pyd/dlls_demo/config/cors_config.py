import os

from corsheaders.middleware import CorsMiddleware


class CORSConfig:

    @classmethod
    def middleware(self,app):
        origins = os.getenv("CORS_ALLOWED_ORIGINS", "").split("")
        app.add_middleware(
            CorsMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
