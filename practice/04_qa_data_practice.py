"""
练习 04: 贴近当前项目的 QA 数据处理练习
运行: python practice/04_qa_data_practice.py
"""

from collections import defaultdict
from datetime import datetime


qa_rows = [
    {"id": "1", "query": "你好", "answer": "你好这是答案", "created_at": "2026-04-21 10:00:00"},
    {"id": "2", "query": "天气", "answer": "天气这是答案", "created_at": "2026-04-21 10:01:00"},
    {"id": "3", "query": "你好", "answer": "你好这是答案", "created_at": "2026-04-21 10:03:00"},
]


def get_latest_by_query_classic(rows: list[dict], query: str) -> dict | None:
    """
    经典写法: 循环 + 比较时间，找到某个 query 的最新记录。
    """
    latest = None
    for row in rows:
        if row["query"] != query:
            continue
        if latest is None:
            latest = row
            continue

        current_time = datetime.strptime(row["created_at"], "%Y-%m-%d %H:%M:%S")
        latest_time = datetime.strptime(latest["created_at"], "%Y-%m-%d %H:%M:%S")
        if current_time > latest_time:
            latest = row

    return latest


def get_latest_by_query_simple(rows: list[dict], query: str) -> dict | None:
    """
    简化写法: 先过滤，再 max。
    """
    filtered = [r for r in rows if r["query"] == query]
    if not filtered:
        return None

    return max(filtered, key=lambda r: r["created_at"])


def group_count_by_query(rows: list[dict]) -> dict:
    """
    统计每个 query 出现次数。
    """
    counter = defaultdict(int)
    for row in rows:
        counter[row["query"]] += 1
    return dict(counter)


def remove_duplicate_query_keep_latest(rows: list[dict]) -> list[dict]:
    """
    去重: 相同 query 只保留最新一条。
    """
    latest_map: dict[str, dict] = {}
    for row in rows:
        query = row["query"]
        old = latest_map.get(query)
        if not old or row["created_at"] > old["created_at"]:
            latest_map[query] = row

    return list(latest_map.values())


def demo() -> None:
    print("\n=== 原始数据 ===")
    for r in qa_rows:
        print(r)

    print("\n=== 查某个 query 最新记录(经典) ===")
    print(get_latest_by_query_classic(qa_rows, "你好"))

    print("\n=== 查某个 query 最新记录(简化) ===")
    print(get_latest_by_query_simple(qa_rows, "你好"))

    print("\n=== 分组计数 ===")
    print(group_count_by_query(qa_rows))

    print("\n=== 去重后保留最新 ===")
    for r in remove_duplicate_query_keep_latest(qa_rows):
        print(r)


if __name__ == "__main__":
    demo()