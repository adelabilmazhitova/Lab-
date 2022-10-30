######################1
# def test_jackpot(array):
#     for i in range(len(array)):
#         if (array[i]==array[i+1]==array[i-1] ):
#             return True
#         else:
#             return False
# print(test_jackpot([ "&&", "&", "&&&", "&&&&"]))
############################2
# def arrayValuesTypes(array):
#     a = []
#     for i in range(len(array)):
#         a.append(type(array[i]))
#     return a
# print(arrayValuesTypes([21.1, "float", "array", ["I am array"], True, 214]))
#######################3
# class Country:
#     def __init__(self, country, area, population):
#         self.country = country
#         self.area = area
#         self.population = population
#         if self.population > 250000000 or self.area > 3000000:
#             self.is_big = True
#         else:
#             self.is_big = False
#
#     def compare_pd(self, country1):
#         if self.population / self.area > country1.population / country1.area:
#             print(f'{self.country} has a larger population density than {country1.country}')
#         else:
#             print(f'{self.country} has a smaller population density than {country1.country}')
#
# australia = Country('Australia', 23545500, 7692024)
# andorra = Country('Andorra', 76098, 468)
# andorra.compare_pd(australia)
# print(f'{australia.is_big} , Australia is a big country')
# print(f'{andorra.is_big} , Andorra is a big country')
############################4
def sortByLength(array):
    for i in range(len(array)):
        array.sort()
    return array
print(sortByLength(["Google", "Apple", "Microsoft"]))
