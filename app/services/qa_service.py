from sqlalchemy.orm import Session

from app.repositories.qa_repository import QARepository
from app.schemas.qa import AskResponseData


class QAService:
    @staticmethod
    def answer(db: Session, query: str) -> AskResponseData:
        # Default: raw SQL query method
        record = QARepository.get_by_query(db=db, query=query)

        # If you want to switch to ORM query method, comment the line above
        # and uncomment the next line.
        # record = QARepository.get_by_query_orm(db=db, query=query)

        if not record:
            answer_text = f"{query}这是答案"

            # Default: raw SQL insert method
            record = QARepository.insert(db=db, query=query, answer=answer_text)

            # If you want to switch to ORM insert method, comment the line above
            # and uncomment the next line.
            # record = QARepository.insert_orm(db=db, query=query, answer=answer_text)

        return AskResponseData(
            query=record["query"],
            answer=record["answer"],
            created_at=record["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
        )