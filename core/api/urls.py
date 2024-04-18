from django.http import HttpRequest
from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from ninja import NinjaAPI

from core.api.schemas import PingResponseSchema

from core.api.v1.urls import router as v1_router

api = NinjaAPI()


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(status=True)


api.add_router('v1/', v1_router)

urlpatterns = [
    path("", api.urls),
]
