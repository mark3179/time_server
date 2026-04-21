from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500, description="用户提问内容")


class AskResponseData(BaseModel):
    query: str = Field(description="原始问题")
    answer: str = Field(description="回答内容")
    created_at: str = Field(description="记录时间")
