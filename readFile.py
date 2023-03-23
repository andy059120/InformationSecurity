def numberConvertToBinaryDigits(number):
  binaryDigitsReverse = ""
  while (number != 0):
    binaryDigitsReverse += "0" if (number % 2 == 0) else "1"
    number /= 2
    number = int(number)
  binaryDigits = binaryDigitsReverse[::-1]
  while (len(binaryDigits) < 8):
    temp = "0"
    temp += binaryDigits
    binaryDigits = temp
  return binaryDigits

# read txt files
americanCivilWar = open('/filepath/Txt_File.txt','r')
americanCivilWar_Binary = open('/filepath/Txt_File_Binary.txt','w')
americanCivilWar_Int = open('/filepath/Txt_File_Int.txt','w')
americanCivilWarRead = americanCivilWar.read()

# reset files
americanCivilWar_Binary.write("")
americanCivilWar_Binary.close()
americanCivilWar_Int.write("")
americanCivilWar_Int.close()

# write to binary
appendFile = open('/filepath/Txt_File_Binary.txt','a')
with appendFile:
  for i in americanCivilWarRead:
    appendFile.write(numberConvertToBinaryDigits(ord(i)))

appendFile.close()

# write to integer
appendFile = open('/filepath/Txt_File_Int.txt','a')
with appendFile:
  for i in americanCivilWarRead:
    appendFile.write(str(ord(i)))
    appendFile.write(" ")
    # print(int(i))
    # print(ord(i), end = " ")

appendFile.close()
americanCivilWar.close()

# read BMP files
picture = open('/filepath/Img_File.bmp','rb')
picture_Binary = open('/filepath/Img_File_Binary.txt','w')
picture_Int = open('/filepath/Img_File_Int.txt','w')
picture_CaesarCipher = open('/filepath/Img_CaesarCipher.txt','w')
pictureRead = picture.read()

# reset files
picture_Binary.write("")
picture_Binary.close()
picture_Int.write("")
picture_Int.close()
picture_CaesarCipher.write("")
picture_CaesarCipher.close()

# write to binary
data = bytearray(pictureRead)
data = str(pictureRead)
appendFile = open('/filepath/Img_File_Binary.txt','a')
with appendFile:
  for i in pictureRead:
    appendFile.write(numberConvertToBinaryDigits(i))

appendFile.close()

# write to integer
data = str(pictureRead)
appendFile = open('/filepath/Img_File_Int.txt','a')
with appendFile:
  for i in pictureRead:
    appendFile.write(str(i))
    appendFile.write(" ")

appendFile.close()
