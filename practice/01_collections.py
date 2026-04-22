"""
练习 01: Python 常见数据类型操作（经典写法 + 简化写法）
运行: python practice/01_collections.py
"""


def list_demo() -> None:
    print("\n=== list 演示 ===")
    nums = [1, 2, 3]

    # 经典写法: 逐个 append
    nums.append(4)
    nums.append(5)



    # 简化写法: extend 一次追加多个
    nums.extend([6, 7])

    print("当前列表:", nums)
    print("下标取值 nums[0]:", nums[0])
    print("切片 nums[1:4]:", nums[1:4]) # 左闭右开

    # 经典写法: for 循环累加
    total = 0
    for n in nums:
        total += n
    print("经典写法求和:", total)

    # 简化写法: 内置 sum
    print("简化写法求和:", sum(nums))


def dict_demo() -> None:
    print("\n=== dict 演示 ===")
    user = {"id": "u1", "name": "mark"}

    # 经典写法: 直接赋值新增字段
    user["age"] = 20
    print(user)

    # 简化写法: update 批量更新
    user.update({"city": "shanghai", "active": True})

    print("当前字典:", user)
    print("取值 user.get('id'):", user.get("id"))
    print("取值 user['name']:", user["name"])

    # 安全取值: key 不存在时给默认值,没有默认值返回None
    level = user.get("level")
    print("user.get('level'):", level)

    print("遍历键值对:")
    for k, v in user.items():
        print(f"  {k} -> {v}")


def set_demo() -> None:
    print("\n=== set 演示 ===")
    tags = {"python", "fastapi"}

    # set 没有 append, 用 add
    tags.add("mysql")
    tags.add("python")  # 重复值不会生效
    tags.add(3)
    print("去重后集合:", tags)

    for tag in tags:
        result = f"集合元素 ——> {tag}"
        print(result)


def tuple_demo() -> None:
    print("\n=== tuple 演示 ===")
    point = (10, 20)
    x, y = point
    print("元组解包 x, y:", x, y)
    for t in point:
        print(t)


if __name__ == "__main__":
    list_demo()
    # dict_demo()
    # set_demo()
    # tuple_demo()