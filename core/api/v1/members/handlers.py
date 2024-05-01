from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.members.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.members.services.auth import BaseAuthService
from core.project.containers import get_container


router = Router(
    tags=['Members'],
)


@router.post('auth', response=ApiResponse[AuthOutSchema], operation_id='authorize')
def auth_handler(request: HttpRequest, schema: AuthInSchema) -> ApiResponse[AuthOutSchema]:
    container = get_container()
    service: BaseAuthService = container.resolve(BaseAuthService)

    service.authorize(phone=schema.phone)
    return ApiResponse(
        data=AuthOutSchema(
            message=f'Code is send to: {schema.phone}',
        ),
    )


@router.post('confirm', response=ApiResponse[TokenOutSchema], operation_id='confirmCode')
def get_token_handler(request: HttpRequest, schema: TokenInSchema) -> ApiResponse[TokenOutSchema]:
    container = get_container()
    service: BaseAuthService = container.resolve(BaseAuthService)

    try:
        token = service.confirm(code=schema.code, phone=schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message,
        ) from exception

    return ApiResponse(data=TokenOutSchema(token=token))
