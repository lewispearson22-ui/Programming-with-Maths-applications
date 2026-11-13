from random import *

characters = ["Jon Snow","Tyrion Lannister","Rick Sanchez","Morty Smith","Walter White","Jesse Pinkman","Saul Goodman","Gon Freecs","Killua Zoldyck","Levi Ackermann","Ichigo Kurosaki","Light Yagami","Thorfinn Karlsefni","Saturo Gojo","Yuji Itadori","Sung Jin-Woo"]

shuffle(characters)
sentence = ""
for character in range(len(characters)):
    if character == 0:
        sentence = f"{characters[character]}"
    elif character == len(characters) -1:
        sentence = f"{sentence} and {characters[character]}"
    else:
        sentence = f"{sentence},{characters[character]}"
    
print(sentence)


