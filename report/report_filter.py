from report.statistic import statistic_report
from execution_chain.filter import Filter


class ReportFilter(Filter):
    """
     将excel中获取的数据用于请求后台，并获取结果
    """
    report_view_report = statistic_report

    def do_filter(self, case_holder):

        print("report filter generate the test report")
        self.report_view_report.report(case_holder)
        self.chain.execute_internal(case_holder)
