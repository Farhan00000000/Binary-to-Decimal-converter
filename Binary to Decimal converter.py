def binary_to_decimal(binary):
    binary = str(binary)
    integer, fraction = binary.split('.')
    
    # Convert the integer part
    integer_decimal = int(integer, 2)
    
    # Convert the fractional part
    fraction_decimal = 0
    for i in range(len(fraction)):
        fraction_decimal += int(fraction[i]) * 2**(-(i+1))
    
    # Add the integer and fractional parts
    decimal = integer_decimal + fraction_decimal
    return decimal
# Take the binary number from the user/s
binary = float(input("Your binary number : "))
print(binary_to_decimal(binary))
