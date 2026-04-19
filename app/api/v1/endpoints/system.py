from datetime import datetime

from fastapi import APIRouter, Request

from app.schemas.common import ApiResponse, ResponseMeta
from app.schemas.time_info import TimeInfoData
from app.services.time_service import TimeService

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/time-info", response_model=ApiResponse[TimeInfoData], summary="获取时间、时间戳和UUID")
def get_time_info(request: Request):
    data = TimeService.get_time_info()
    return ApiResponse[TimeInfoData](
        data=data,
        # meta=ResponseMeta(
        #     request_id=request.state.request_id,
        #     timestamp=datetime.now(),
        #     path=request.url.path,
        # ),
    )
