# Python Program - Convert Binary to Decimal

print("Enter 'x' for exit.");
binary = input("Enter number in Binary Format: ");
if binary == 'x':
    exit();
else:
    decimal = int(binary, 2);
    print(binary,"in Decimal =",decimal);
    temp = int(binary, 2);
    print(binary,"in Hexadecimal =",hex(temp));
    temp = int(binary, 2);
    print(binary,"in Octal =",oct(temp));
