from result.handler.validator import Validator
import json


def ensure_exists_key(key, result):
    if not hasattr(result, key):
        raise Exception("校验规则存在不合法key" + "【" + key + "】")


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
        ensure_exists_key(condition.key, response_holder)
        value = response_holder.code
        operator = condition.operator
        method = super().get_operator_method(operator)
        if operator != "is" or operator != "is_not":
            return method(self, condition.value, value)
        else:
            return method(self, value)

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
        :param expression:
        :return:
        """
        if response_holder.code == 200:
            result = response_holder.result
            object = json.loads(result)
            ensure_exists_key(condition.key, object)
            operator = condition.operator
            value = self.obtain_value(condition.key, object)
            method = super().get_operator_method(operator)
            if operator != "is" or operator != "is_not":
                return method(self, condition.value, value)
            else:
                return method(self, value)
        else:
            return False

    def obtain_value(self, key: str, object):
        items = key.split(".")
        value = None
        for item in items:
            value = object[item]
        return value

    def get_start_with(self):
        return self.start_with
