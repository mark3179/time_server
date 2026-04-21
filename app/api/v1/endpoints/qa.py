from datetime import datetime
import logging

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.db.mysql import get_db
from app.schemas.common import ApiResponse, ResponseMeta
from app.schemas.qa import AskRequest, AskResponseData
from app.services.qa_service import QAService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/qa", tags=["qa"])


@router.post("/ask", response_model=ApiResponse[AskResponseData], summary="问答接口")
def ask_question(request: Request, payload: AskRequest, db: Session = Depends(get_db)):
    query = payload.query

    # 用于演示 HTTPException 的触发
    if query == "__http_error__":
        raise HTTPException(status_code=400, detail="manual http exception")

    # 用于演示未捕获异常的触发
    if query == "__server_error__":
        raise RuntimeError("manual unhandled exception")

    try:
        # 假设这里是数据库操作
        testprint = "测试try-catch"
        if testprint == "测试try-catch" and query == "__db_error__":
            raise HTTPException(status_code=500, detail="Lost connection to DB")  # 真实情况下是不需要手动抛的
    # except HTTPException as e:
    #     # 1. 手动记录日志：因为我们已经捕获了它，全局处理器就不会再记录了
    #     # 所以我们需要在这里手动记录，确保程序员能看到具体的错误原因
    #     logger.error(f"Database connection failed: {str(e)}")
        
    #     # 2. 返回特定的业务异常：给前端一个明确的错误提示
    #     raise HTTPException(status_code=503, detail="数据库连接失败，请稍后再试") # 这里是为了改错误信息才这样的要不然可以直接raise e
    except Exception as e:
        # 1. 记录原始错误堆栈到日志（非常重要，否则你就不知道到底哪里出 Bug 了）
        logger.exception(f"执行过程中发生未预期错误: {str(e)}") # exception 会记录错误堆栈信息,也是error级别的日志
        
        # 2. 直接抛出一个带自定义信息的 HTTPException
        # 这样就不会触发全局的“系统繁忙”逻辑，而是返回你指定的这段话
        raise HTTPException(status_code=500, detail="问答服务暂时不可用，我们正在紧急修复")

    data = QAService.answer(db=db, query=query)
    return ApiResponse[AskResponseData](
        data=data,
        # meta=ResponseMeta(
        #     request_id=request.state.request_id,
        #     timestamp=datetime.now(),
        #     path=request.url.path,
        # ),
    )
