from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500, description="用户提问内容")


class AskResponseData(BaseModel):
    query: str = Field(description="原始问题")
    current_time: str = Field(description="当前本地时间")
