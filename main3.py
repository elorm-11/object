a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

def area():

    # calculate the sides
    s = (a + b + c) / 2

    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    return area

area()

def perimeter():

    # Calculate the perimeter
    perim = a + b + c

    return perim

perimeter()


print( 'Area is: ',format(area,'.1f'))
print( 'Perimeter is: ',format(perim,',.1f'))


main()