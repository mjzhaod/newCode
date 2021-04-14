from result.handler.result_validator import FieldValidator, ResponseValidator
default_validator = [FieldValidator(), ResponseValidator()]


def valid(expression, response_holder):
    actual_validator = obtain_actual_validator(expression)
    return actual_validator.valid(expression, response_holder)


def obtain_actual_validator(expression):
    for candidate in default_validator:
        if candidate.support(expression):
            return candidate
