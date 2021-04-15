
class Condition:

    key = None
    operator = None
    value = None

    def __init__(self, key, operator, value):
        self.key = key
        self.value = value
        self.operator = operator


class Validator:

    def valid(self, expression, response_holder):
        items = expression.split("->")
        expression = items[1]
        condition = self.parse(expression)
        return self.do_valid_internal(condition, response_holder)

    def do_valid_internal(self, condition, response_holder):
        raise Exception("不合法校验器")

    def ensure_expression_valid(self, expression: str):
        items = expression.split("->")
        if len(items) < 2:
            raise Exception("表达式不合法")

    def parse(self, expression) -> Condition:
        items = expression.split(" ")
        index = 0
        condition = None
        while index < len(items) -1:
            condition = Condition(items[index], items[index + 1], items[index + 2])
            index += 2
        return condition

    def support(self, expression: str):
        return expression.startswith(self.get_start_with())

    def get_start_with(self, expression: str):
        raise Exception("不合法校验器")

    def eq(self, value1, value2):
        return value1 == value2

    def neq(self, value1, value2):
        return value1 != value2

    def gt(self, value1, value2):
        return value1 > value2

    def gte(self, value1, value2):
        return self.gt(value1, value2) or self.eq(value1, value2)

    def lt(self, value1, value2):
        return value1 < value2

    def lte(self, value1, value2):
        return self.lt(value1, value2) or self.eq(value1, value2)

    def is_null(self, value):
        return value is None

    def is_not_null(self, value):
        return value is not None

    method = {
        "eq": eq,
        "neq": neq,
        "gt": gt,
        "gte": gte,
        "lt": lt,
        "lte": lte,
        "is_null": is_null,
        "is_not_null": is_not_null,
    }

    def get_operator_method(self, operator):
        return self.method[operator]
