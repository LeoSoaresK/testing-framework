from framework_xunit import TestCase, TestResult

class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception("Erro inesperado")

if __name__ == "__main__":
    result = TestResult()
    
    test_pass = TestStub("test_success")
    test_pass.run(result)
    
    test_fail = TestStub("test_failure")
    test_fail.run(result)
    
    test_err = TestStub("test_error")
    test_err.run(result)
    
    print(f"Relatório Final: {result.summary()}")
    assert result.summary() == "3 run, 1 failed, 1 error"