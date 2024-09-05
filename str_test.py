# test_string = "Hello World"
#
# # print(test_string[0:2])
# # print(test_string[2:5])
# # print(test_string[6:])
# print(test_string[-9:-1])
# print(test_string[:: -1])

# i=0
# while i<10:
#     for j in range(10):
#         print("i=",i,"j=",j)
#
#     i+=1



class roobit:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def name_age(self):
        print(self.name, self.age)

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

    @staticmethod
    def static_method():
        print("static_method")


if __name__ == "__main__":
    r = roobit("roobit", 25)
    r.name_age()
    c =roobit.from_string("roobit,28")
    print(c.name, c.age)
    roobit.static_method()