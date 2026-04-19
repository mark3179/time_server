from datetime import datetime

from app.schemas.qa import AskResponseData


class QAService:
    @staticmethod
    def answer(query: str) -> AskResponseData:
        return AskResponseData(
            query=query,
            current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
