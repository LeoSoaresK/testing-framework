class TestResult:
    def __init__(self):
        self.run_count = 0
        self.failures = []
        self.errors = []

    def test_started(self):
        self.run_count += 1

    def add_failure(self, test):
        self.failures.append(test)

    def add_error(self, test):
        self.errors.append(test)

    def summary(self):
        return f"{self.run_count} run, {len(self.failures)} failed, {len(self.errors)} error"

class TestSuite:
    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestLoader:
    def __init__(self):
        self.test_method_prefix = "test"

    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        return [m for m in methods if m.startswith(self.test_method_prefix)]

    def make_suite(self, test_case_class):
        suite = TestSuite()
        for name in self.get_test_case_names(test_case_class):
            suite.add_test(test_case_class(name))
        return suite

class TestRunner:
    def __init__(self):
        self.result = TestResult()

    def run(self, test):
        test.run(self.result)
        print(self.result.summary())
        return self.result

class TestCase:
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError:
            result.add_failure(self.test_method_name)
        except Exception:
            result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def assert_equal(self, first, second):
        if first != second:
            raise AssertionError(f"{first} != {second}")

    def assert_true(self, expr):
        if not expr:
            raise AssertionError(f"{expr} is not true")

    def assert_false(self, expr):
        if expr:
            raise AssertionError(f"{expr} is not false")

    def assert_in(self, member, container):
        if member not in container:
            raise AssertionError(f"{member} not found in {container}")