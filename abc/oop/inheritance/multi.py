class A:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print(f"Hi, this is {self.name}")


if __name__ == "__main__":
    a = A("apple")
    a.hi()
