import sys
import time

def type_line(text, delay=0.121):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


lyrics_1 = [
"Arz Kiya Hai....."
]
lyrics_2 = [
"Kayar jo the, vo shayar bane",
"Ab kya kya karein ye ishq mein",
"Na kehte the kuch jo, lage khoj mein",
"Kya lafz chune?\n",

"Naye aashiq ye, ishq mein tere hain faiz bane",
"Arz kiya hai",
"Humne bhi likha kuch tere baare mein\n",

"Aise tu lage ki gulaab hai",
"Aur aise tu lage ki gulaab hai",
"Aur aise tu lage ki gulaab hai",
"Baghon mein dil ke",
"Khilke in fizaaon mein chhaye ho haaye\n",

"Aur vaise hum to tere hi gulaam hain",
"Aur vaise hum to tere hi gulaam hain",
"Baadshah dil ke, teri baazi mein",
"Jo tu chahe to…\n",

"Doobe dilon ki kya nau banu?",
"Main khud tar paaoon na aankhon mein",
"Shayar ki fitrat mein hi doobna",
"Main kya hi ladu toofanon se\n",

"Ishq mein tere hain faiz bane",
"Arz kiya hai",
"Humne bhi likha kuch tere baare mein\n",

"Haathon ko sambhaale mere haathon mein",
"Kaise haathon ko sambhaale mere haathon mein?",
"Jab tak neend na aaye in lakeeron mein",
"Baatein hon…\n",

]
lyrics_3 = [
"Haan…\n"
]
lyrics_4 = [
"Sabne to sab keh diya hai",
"Kya hi kahoon jo abhi bhi ankaha hai?",
"Main haay…\n",

"Na Mirza, na Mir",
"Na maahir, na zaahir",
"Karoon kuch naya main?",
"Haay… par…\n",

"Jo bhi likha hai, jiya hai",
"Haan jiya hai\n",

"Aise, aise, aise, kaise, vaise, jaise",
"Jaise main padhun mere dil mein jo",
"Meri aankhen bhi padhein teri aankhon ko\n",

"Kya ye mehfil mein baithe?",
"Ya uthe daud jaane ko? haaye\n",

"Teri aankhon mein taarifon ki talaash hai",
"Meri mehfil tere jaane se veeraan hai",
"Main bas shayar bana hoon",
"Sirf tu sunne aaye to…\n",

"Shayad shayar bana hoon",
"Sirf tu sunne aaye to",

]


for line in lyrics_1:
    type_line(line)
    time.sleep(24) 

for line in lyrics_2:
    type_line(line)
    time.sleep(0.75) 

for line in lyrics_3:
    type_line(line)
    time.sleep(43) 

for line in lyrics_4:
    type_line(line)
    time.sleep(0.85) 