# Python Program - Convert Binary to Decimal

print("Enter 'x' for exit.")
while True:
    binary = None
    binary = input("Enter number in Binary Format: ")
    try:
        binary = int(binary)
    except:
        binary = str(binary)

    if type(binary) != int:
        print("Input Not Valid. - Exiting.")
        exit()
    else:


        decimal = int(binary)#, 2)
        print(binary,"In Decimal: ",decimal)
        print(binary,"In Binary: ",bin(decimal).replace("0b", ""))
        print(binary,"In Hexadecimal: ",hex(decimal).replace("0x", ""))
        print(binary,"In Octal: ",oct(decimal).replace("0o", ""))
