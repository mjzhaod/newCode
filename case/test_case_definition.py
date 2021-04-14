
class TestCaseDefinition:
    """
    定义一个测试用例在流转过程中涉及到的变量
    """
    path = None
    properties_holder = None

    def __init__(self, path, properties):
        self.path = path
        self.properties_holder = properties

    def get_path(self):
        return self.path

    def get_properties(self):
        return self.properties_holder

