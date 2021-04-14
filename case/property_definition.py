class Property:
    # 表示对应用例的属性名
    name = None
    # excel中对应属性的列号
    index = 0

    def __init__(self, name, index):
        self.name = name
        self.index = index

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index
