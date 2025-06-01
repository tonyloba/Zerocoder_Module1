def square(x):
    sq = x * x
    perimeter = 4 * x
    diagonal = x * (2 ** 0.5)
    #return (f"Square: {sq} , Perimeter: {perimeter} , Diagonal: {diagonal}")
    return (sq , perimeter , diagonal)

print(square(float(input("Enter a number: "))))