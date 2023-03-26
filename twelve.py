# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")
        
#     def draw(self):
#         print("draw")
# point = Point(10,20)
# print(point.x)


# # point1 = Point()
# # #point1.draw()
# # point1.x = 10
# # point1.y = 20
# # print(point1.x)
# # point1.draw()

# # point2 = Point()


class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

will = Person("Will Smith")
will.talk()