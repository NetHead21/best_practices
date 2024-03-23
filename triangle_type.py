# Write a program identifying what type of each record in the TRIANGLES table using its
# three side lengths.
# Output one of the following statements for each record in the table:

# Equilateral: It's a triangle with  sides of equal length.
# Isosceles: It's a triangle two  sides of equal length.
# Scalene: It's a triangle with  sides of differing lengths.
# Not A Triangle: The given values of A, B, and C don't form a triangle.

# side1 = int(input("Enter side 1:"))
# side2 = int(input("Enter side 2:"))
# side3 = int(input("Enter side 3:"))


# if side1 == side2 == side3:
#     print("Equilateral triangle")
# elif side1 == side2 or side2 == side3 or side3 == side1:
#     print("Isosceles triangle")
# else:
#     print("Scalene")

# sides = list(map(int, input("Enter sides: ").split()))
# if len(set(sides)) == 1:
#     print("Equilateral triangle")
# elif len(set(sides)) == 2:
#     print("Isosceles triangle")
# else:
#     print("Scalene")

triangles: dict[int, str] = {
    1: "Equilateral",
    2: "Isosceles",
    3: "Scalene",
}

sides = list(map(int, input("Enter sides: ").split()))
print(f"Is a {triangles[len(set(sides))]} triangle")
