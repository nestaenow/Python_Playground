def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 3))

# Test I
# Population density function
def population_density(population, land_area):
    return population / land_area
# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
