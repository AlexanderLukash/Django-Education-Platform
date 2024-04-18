from pydantic import BaseModel


class PingResponseSchema(BaseModel):
    status: bool
