from datetime import datetime
from uuid import uuid4

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.models.qa_model import QAModel


class QARepository:
    @staticmethod
    def get_by_query(db: Session, query: str) -> dict | None:
        # Raw SQL version
        sql = text(
            """
            SELECT id, query, answer, created_at
            FROM qa
            WHERE query = :query
            ORDER BY created_at DESC
            """
        )
        row = db.execute(sql, {"query": query}).mappings().first()
        return dict(row) if row else None

        # 多条记录
        # rows = db.execute(sql, {"query": query}).mappings().all()
        # return [dict(row) for row in rows]

    @staticmethod
    def get_by_query_orm(db: Session, query: str) -> dict | None:
        # ORM version
        stmt = (
            select(QAModel)
            .where(QAModel.query == query)
            .order_by(QAModel.created_at.desc())
        )
        obj = db.execute(stmt).scalars().first()
        if not obj:
            return None
        return {
            "id": obj.id,
            "query": obj.query,
            "answer": obj.answer,
            "created_at": obj.created_at,
        }

        # 多条记录
        # objs = db.execute(stmt).scalars().all()
        # result = []
        # for obj in objs:
        #     result.append({"id": obj.id, "query": obj.query, "answer": obj.answer, "created_at": obj.created_at})
        # return result

        # 多条记录列表推导式
        # objs = db.execute(stmt).scalars().all()
        # return [
        #     {
        #         "id": obj.id,
        #         "query": obj.query,
        #         "answer": obj.answer,
        #         "created_at": obj.created_at,
        #     }
        #     for obj in objs
        # ]

    @staticmethod
    def insert(db: Session, query: str, answer: str) -> dict:
        now = datetime.now()
        qa_id = str(uuid4())
        sql = text(
            """
            INSERT INTO qa (id, query, answer, created_at)
            VALUES (:id, :query, :answer, :created_at)
            """
        )
        db.execute(
            sql,
            {
                "id": qa_id,
                "query": query,
                "answer": answer,
                "created_at": now,
            },
        )
        db.commit()
        return {
            "id": qa_id,
            "query": query,
            "answer": answer,
            "created_at": now,
        }

    @staticmethod
    def insert_orm(db: Session, query: str, answer: str) -> dict:
        now = datetime.now()
        qa_id = str(uuid4())

        obj = QAModel(
            id=qa_id,
            query=query,
            answer=answer,
            created_at=now,
        )
        db.add(obj)
        db.commit()

        return {
            "id": obj.id,
            "query": obj.query,
            "answer": obj.answer,
            "created_at": obj.created_at,
        }