from result.handler.validator import Validator
import json


class ResponseValidator(Validator):
    """
    校验response 级别的
    """
    start_with = "response"

    def do_valid_internal(self, condition, response_holder):
        """
        暂时支持 code判断
        :param expression:
        :return:
        """
        value = response_holder[condition.key]
        operator = condition.operator
        method = super.get_operator_method(operator)
        if operator != "is" or operator != "is_not":
            return method(condition.value, value)
        else:
            return method(value)

    def get_start_with(self):
        return self.start_with


class FieldValidator(Validator):
    """
    校验response中返回json时，字段的值是否合法
    支持
    is null
    is_not null
    eq gt gte lt lte between not_eq
    """

    start_with = "field"

    def do_valid_internal(self, condition, response_holder):
        """
        暂时支持 code判断
        :param expression:
        :return:
        """
        result = response_holder.result
        object = json.loads(result)
        operator = condition.operator
        value = self.obtain_value(condition.key, object)
        method = super.get_operator_method(operator)
        if operator != "is" or operator != "is_not":
            return method(condition.value, value)
        else:
            return method(value)

    def obtain_value(self, key: str, object):
        items = key.split(".")
        value = None
        for item in items:
            value = object[item]
        return value

    def get_start_with(self):
        return self.start_with
