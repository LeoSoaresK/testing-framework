from framework_xunit import TestCase

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

if __name__ == "__main__":
    spy = TestSpy("test_method")
    spy.run()
    print(f"Sequência executada: {spy.log}")
    assert spy.log == "set_up test_method tear_down"