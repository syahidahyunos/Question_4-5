
import socket

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
  
#because array starts with zero
    two_digits = ["", "sepuluh", "sebelas", "dua belas",
                  "tiga belas", "empat belas", "lima belas",
                  "enam belas", "tujuh belas", "lapan belas",
                  "sembilan belas"]
  

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
                # here len can be 3 or 4
  
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
  


serverIP    = "Server A"
serverPort  = 31337

UDPSocket   = socket.socket()

try:
    UDPSocket.connect((serverIP, serverPort))
    m = UDPSocket.recvfrom(1024)
    convert_to_bahasa(m)

except Exception as Ex:

    print("Exception Occurred: %s"%Ex)

    # Close the socket upon an exception

    UDPSocket.close()


