triangle=[int(input()),int(input()),int(input())]
if sum(triangle) != 180:
    print("Error")
else:
    match len(list(set(triangle))):
        case 1:
            print("Equilateral")
        case 2:
            print("Isosceles")
        case 3:
            print("Scalene")