class CaseInfoHolder:
    case_definition = None
    cases = None
    result = None

    def __init__(self, case_definition):
        self.case_definition = case_definition

    def get_definition(self):
        return self.case_definition

    def set_cases(self, cases):
        self.cases = cases

    def get_cases(self):
        return self.cases
