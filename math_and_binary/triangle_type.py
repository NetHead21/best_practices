# Write a program identifying what type of each record in the TRIANGLES table using its
# three side lengths.
# Output one of the following statements for each record in the table:

# Equilateral: It's a triangle with  sides of equal length.
# Isosceles: It's a triangle two  sides of equal length.
# Scalene: It's a triangle with  sides of differing lengths.
# Not A Triangle: The given values of A, B, and C don't form a triangle.


sides = list(map(int, input("Enter sides: ").split()))

triangles: dict[int, str] = {
    1: "Equilateral",
    2: "Isosceles",
    3: "Scalene",
}

print(f"Is a {triangles[len(set(sides))]} triangle")

# if len(set(sides)) == 1:
#     print("Equilateral triangle")
# elif len(set(sides)) == 2:
#     print("Isosceles triangle")
# else:
#     print("Scalene")


# if sides[0] == sides[1] == sides[2]:
#     print("Equilateral triangle")
# elif sides[0] == sides[1] or sides[1] == sides or sides == sides[0]:
#     print("Isosceles triangle")
# else:
#     print("Scalene")
