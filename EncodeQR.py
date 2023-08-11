def EncodeQR(name):

    padding = 0b10000000

    if len(name) < 1 or len(name) > 5:
        print("Upto 5 characters long.")
    else:
        encoded_arr = []
        
        for char in name:
            binary_value = format(ord(char), '08b')
            shifted_number = padding << 1
            encoded_arr.append(str(bin(shifted_number)[2:]) + binary_value)
   
        return ''.join(encoded_arr)

p_name = input("Enter Product Name: ")
encoded_res = EncodeQR(p_name)
print(encoded_res)