"""
练习 02: 条件、循环、推导式（经典写法 + 简化写法）
运行: python practice/02_loops_and_conditions.py
"""


def condition_demo(score: int) -> str:
    # 经典 if / elif / else
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    return "D"


def loop_demo() -> None:
    print("\n=== 循环演示 ===")
    words = ["python", "qa", "service", "db"]

    # 经典写法: 用 for + append 构造新列表
    upper_words_classic = []
    for w in words:
        upper_words_classic.append(w.upper())
    print("经典写法:", upper_words_classic)

    # 简化写法: 列表推导式
    upper_words_simple = [w.upper() for w in words]
    print("简化写法:", upper_words_simple)

    # 带条件的推导式
    long_words = [
        w 
        for w in words 
        if len(w) > 2
    ]
    print("长度>2:", long_words)


def range_enumerate_demo() -> None:
    print("\n=== range / enumerate 演示 ===")

    print("range(3):")
    for i in range(3):
        print(" i =", i)

    users = ["alice", "bob", "cindy"]
    print("enumerate(users, start=1):")
    for idx, name in enumerate(users, start=1):
    # for idx, name in enumerate(users):
        print(f" {idx}. {name}")


def dict_loop_demo() -> None:
    print("\n=== dict 循环演示 ===")
    score_map = {"alice": 95, "bob": 78, "cindy": 88}

    # 经典写法
    passed = []
    for name, score in score_map.items():
        if score >= 80:
            passed.append(name)
    print("经典写法通过名单:", passed)

    # 简化写法
    passed2 = [name for name, score in score_map.items() if score >= 80]
    print("简化写法通过名单:", passed2)


if __name__ == "__main__":
    # print("score=87 ->", condition_demo(87))
    # loop_demo()
    # range_enumerate_demo()
    dict_loop_demo()