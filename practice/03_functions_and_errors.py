"""
练习 03: 函数、类型转换、异常处理（经典写法 + 简化写法）
运行: python practice/03_functions_and_errors.py
"""


def parse_port(raw: str) -> int:
    """
    把字符串端口转成 int。
    演示 try/except 的经典写法。
    """
    try:
        port = int(raw.strip())
        # 假如这里还有很多业务代码,可能报错
    except ValueError as e:
        raise ValueError(f"端口不是有效数字: {e}")
    except Exception as e:
        # 统一抛出更易懂的业务错误
        # 这里把错误信息记录到日志文件
        raise ValueError(f"系统异常，请稍后再试")

    if not (1 <= port <= 65535):
        raise ValueError(f"端口超出范围: {port}")
    return port


def format_user(name: str, age: int | None = None) -> dict:
    """
    返回用户信息。
    演示默认参数和条件字段。
    """
    data = {"name": name.strip()}

    # 经典写法
    if age is not None:
        data["age"] = age

    return data


def safe_divide(a: float, b: float) -> float | None:
    """
    演示简单异常处理。
    b=0 时返回 None，而不是抛错。
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def demo() -> None:
    print("\n=== parse_port ===")
    print(parse_port(" 你好 "))

    print("\n=== format_user ===")
    print(format_user(" mark "))
    print(format_user(" alice ", 18))

    print("\n=== safe_divide ===")
    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))


if __name__ == "__main__":
    demo()