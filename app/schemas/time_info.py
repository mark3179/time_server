from pydantic import BaseModel, Field


class TimeInfoData(BaseModel):
    current_time: str = Field(description="当前本地时间字符串")
    current_time_iso: str = Field(description="ISO8601时间字符串")
    timestamp_seconds: int = Field(description="当前秒级时间戳")
    timestamp_milliseconds: int = Field(description="当前毫秒级时间戳")
    uuid: str = Field(description="随机UUID")
