from framework_xunit import TestCase, TestResult

class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception

if __name__ == "__main__":
    result = TestResult()
    
    test1 = TestStub("test_success")
    test1.run(result)
    
    test2 = TestStub("test_failure")
    test2.run(result)
    
    test3 = TestStub("test_error")
    test3.run(result)
    
    print(result.summary())
    assert result.summary() == "3 run, 1 failed, 1 error"