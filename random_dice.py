class MyClass:
  def __init__(self, key: str, value: int):
    self.key = key
    self.value = value
    self.__my_int = 5

  def other_fun(self):
    print(self.key, self.value + self.__my_int)




my_instance_of_class = MyClass("hello", 2)
