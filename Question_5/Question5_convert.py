
  
def convert_to_bahasa(num):
  
    # Get number of digits
    # in given number
    l = len(num)
  
    # 
    if (l == 0):
        print("empty string")
        return
  
    if (l > 3):
        print("Number must be less or equal to 999")
        return
  

    single_digits =["kosong", "satu", "dua", "tiga",
                     "empat", "lima", "enam", "tujuh",
                     "lapan", "sembilan"]
  
#leave the first one because array starts with zero
    two_digits = ["", "sepuluh", "sebelas", "dua belas",
                  "tiga belas", "empat belas", "lima belas",
                  "enam belas", "tujuh belas", "lapan belas",
                  "sembilan belas"]
  
#leave the first and second because array starts with zero and no such thing as 'satu puluh'
    tens_multiple = ["", "", "dua puluh", "tiga puluh", "empat puluh",
                     "lima puluh", "enam puluh", "tujuh puluh", "lapan puluh",
                     "sembilan puluh"]
  
    tens_power = ["ratus", "ribu"]
  
  
    # For single digit number
    if (l == 1):
        print(single_digits[ord(num[0]) - 48])
        return
  
    # Iterate while num is not '\0'
    x = 0
    while (x < len(num)):
  
        # Code path for first 2 digits
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48],
                      end=" ")
                print(tens_power[l - 3], end=" ")
                # here len for 3
  
            l -= 1
  
        else:
  

            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48)
                print(two_digits[sum])
                return
  
            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return
  

            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(tens_multiple[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(single_digits[ord(num[x]) - 48])
        x += 1
  
num = input("Insert number to convert: ")
convert_to_bahasa(num)


