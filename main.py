# class Triangle:
#     def __init__(self, file_path: str):
#         self.file = open(f'{file_path}.csv')
#
#
#     def get_petimetr(self):
#         import csv
#         reader = csv.reader(self.file)
#         for side in reader:
#             a, b, c = side
#             print(int(a) + int(b) + int(c))
#
#     def __int__(self):
#         self.file.close()
#         del self.file
#
# triangel = Triangle('triangel')
# triangel.get_petimetr()

#======================================================================
#__bool__

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return int(self.a) + int(self.b) + int(self.c)
#
#
#     def __bool__(self):
#         return int(self.a) == int(self.b) == int(self.c)
#
# triangle_perimetr = []
# with open('triangle.csv') as csv_file:
#     import csv
#     reader = csv.reader(csv_file)
#     for sides in reader:
#         a, b, c = sides
#         if Triangle(a, b, c):
#             print(a, b, c)
#             triangle_perimetr.append(Triangle(a, b, c).get_perimetr())
# print(triangle_perimetr)

#======================================================================

# class User:
#     def __init__(self, f_n, l_n, age):
#         self.f_n = f_n
#         self.l_n = l_n
#         self.age = age
#
#     def __lt__(self, other):
#         return self.age <= other.age
#
#     def __le__(self, other):
#         return self.age >=other.age
#
# user1 = User('Toxir', 'Toxitov', 15)
# user2 = User('Sobir', 'Sobirov', 20)
#
# print(User.__lt__(user1, user2))
# print(User.__le__(user1, user2))

#======================================================================


