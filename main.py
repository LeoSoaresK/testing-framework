from framework_xunit import TestCase, TestResult, TestSuite

class TestStub(TestCase):
    def test_success(self):
        assert True
    def test_failure(self):
        assert False
    def test_error(self):
        raise Exception

class TestSpy(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""
    def set_up(self):
        self.log += "set_up "
    def test_method(self):
        self.log += "test_method "
    def tear_down(self):
        self.log += "tear_down"

class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()
    def test_result_success_run(self):
        stub = TestStub("test_success")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 0 error"
    def test_result_failure_run(self):
        stub = TestStub("test_failure")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 1 failed, 0 error"
    def test_result_error_run(self):
        stub = TestStub("test_error")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 1 error"
    def test_template_method(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.log == "set_up test_method tear_down"

class TestSuiteTest(TestCase):
    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        assert len(suite.tests) == 2
    def test_suite_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.run(result)
        assert result.summary() == "2 run, 1 failed, 0 error"

if __name__ == "__main__":
    final_result = TestResult()
    suite = TestSuite()
    
    suite.add_test(TestCaseTest("test_result_success_run"))
    suite.add_test(TestCaseTest("test_result_failure_run"))
    suite.add_test(TestCaseTest("test_result_error_run"))
    suite.add_test(TestCaseTest("test_template_method"))
    suite.add_test(TestSuiteTest("test_suite_size"))
    suite.add_test(TestSuiteTest("test_suite_run"))
    
    suite.run(final_result)
    print(f"{final_result.summary()}")
    assert len(final_result.failures) == 0 and len(final_result.errors) == 0