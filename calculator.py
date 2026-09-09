def calculate(expression: str) -> float:
    parts = expression.strip().split()
    if len(parts) != 3:
        raise ValueError("请输入格式：数字 运算符 数字，例如：2 + 3")

    left_text, operator, right_text = parts
    left = float(left_text)
    right = float(right_text)

    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ValueError("除数不能为 0")
        return left / right
    raise ValueError("仅支持 + - * / 四则运算")


def main() -> None:
    print("简易计算器（输入 q 退出）")
    while True:
        user_input = input("请输入表达式：")
        if user_input.strip().lower() in {"q", "quit", "exit"}:
            print("已退出。")
            break
        try:
            result = calculate(user_input)
            if result.is_integer():
                print(f"结果：{int(result)}")
            else:
                print(f"结果：{result}")
        except ValueError as error:
            print(f"错误：{error}")


if __name__ == "__main__":
    main()
