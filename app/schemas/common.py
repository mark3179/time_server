from datetime import datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class RequestMeta(BaseModel):
    trace_id: str | None = Field(default=None, description="客户端链路追踪ID")
    client_timestamp: int | None = Field(default=None, description="客户端发送时的时间戳（毫秒）")


class ApiRequest(BaseModel, Generic[T]):
    data: T | None = Field(default=None, description="请求业务数据")
    meta: RequestMeta | None = Field(default=None, description="请求元信息")


class ResponseMeta(BaseModel):
    request_id: str = Field(description="服务端生成的请求ID")
    timestamp: datetime = Field(description="服务端响应时间")
    path: str = Field(description="请求路径")


class ApiResponse(BaseModel, Generic[T]):
    code: int = Field(default=0, description="业务状态码，0表示成功")
    message: str = Field(default="success", description="状态信息")
    data: T | None = Field(default=None, description="业务数据")
    meta: ResponseMeta
