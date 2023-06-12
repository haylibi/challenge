from PIL import Image
im = Image.open('blank.png')
data = im.getdata()
cyphered = ''
K = []
count = 0
temp = ''
for i in range(0,83900+1,100):
    (a,b,c) = data[i]
    x = i%3
    if x == 0:
        cyphered += bin(a)[-1]
    elif x == 1:
        cyphered += bin(b)[-1]
    elif x == 2:
        cyphered += bin(c)[-1]
        

#I noticed that the numbers changed from the RGB code were always, 
#first the Red one, second the Green one and third the Blue one
#Mathematically, the Red part changed when x%3 == 0 (data[x]), Green with (x%3 == 1) and blue (x%3 == 2)
#After that, I decided to just pick the bits as follow:
#last bit from red when x%3 == 0, last bit from green when x%3 == 1 and last bit from blue when x%3 == 2
#I stopped after the blue bit never changed again (83900) and got the following message):
#'100011110001110011011101000110000101110010011101000010000001101111011001100010000001101101011001010111001101110011011000010110011101100101001111100101001001101111011100110110010101110011001000000110000101110010011001010010000001110010011001010110010000101100001000000111010001101000011001010010000001110011011010110111100100100000011010010111001100100000011000100110110001110101011001010010111000100000010101110110100001101111001000000110011101101111011101000010000000110101001000000110011001110010011011110110110100100000011001010111100001100001011011010011111100100000010110010110010101110011001000000111001101101001011100100010110000100000011010010111010001110011001000000101100101101111011101010010000100111100011001010110111001100100001000000110111101100110001000000110110101100101011100110111001101100001011001110110010100111110000000'
#All it was left was to do a bitshift of 6 to the right (or left, I'm confused) and we would begin the message with \x02, which is the start of message
#(because of the tip the professor told us, the message starts with bytes[2])
#And, after taking that bit sequence and converting it to a string, I got the message:
#'\x02<start of message>Roses are red, the sky is blue. Who got 5 from exam? Yes sir, its You!<end of message>'

    
def bin2decimal(n):                 #Convert binary (int/str) to decimal (integer) 
    number = 0
    n = str(n)
    for i in range(1,len(n)+1):
        if n[-i] == '1':
            number += pow(2,i-1)
    return number

def bin2txt(A):                   #Convert from ASCII (str/binary integer) to text (str)
    A = str(A)
    if len(A)%8!=0:
        A = '0'*(8-len(A)%8)+A
    txt = ''
    for i in range(int(len(A)/8)):
        txt += chr(bin2decimal(A[8*i:8*i+8]))
    return txt




#TO GET THE MESSAGE:
cyphered = cyphered[-6:] + cyphered[:-6]
print(bin2txt(cyphered))
