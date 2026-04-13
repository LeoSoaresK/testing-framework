from framework_xunit import TestCase, TestResult, TestSuite, TestLoader, TestRunner

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

class TestLoaderTest(TestCase):
    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        assert len(suite.tests) == 3
    def test_get_test_case_names(self):
        loader = TestLoader()
        names = loader.get_test_case_names(TestStub)
        assert "test_success" in names
        assert "test_failure" in names
        assert "test_error" in names

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite()
    
    suite.add_test(loader.make_suite(TestCaseTest))
    suite.add_test(loader.make_suite(TestSuiteTest))
    suite.add_test(loader.make_suite(TestLoaderTest))
    
    runner = TestRunner()
    runner.run(suite)