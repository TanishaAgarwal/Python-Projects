import json
from difflib import get_close_matches

color = json.load(open("Colors.json"))

def translate(word):
    if word in color:
        return color[word]
    elif len(get_close_matches(word,color.keys())) > 0:
        x = get_close_matches(word,color.keys())[0]
        guess = input("Did you mean %s instead? Press (y/n) " %x)
        if guess.lower() == 'y':
            return color[x]
        else:
            return "Sorry!! No Hexacode available"
    else:
        return "Sorry!! No Hexacode available"
    

while True:
    x = input('Enter the color name : ')
    x = x.lower()
    code = translate(x)
    print("HexCode : ",code)
    again = input("Do you want to search any other Colors HexCode (y/n) ? ")
    print('==================================')
    print('==================================')
    if again.lower() == 'y':
        continue
    else:
        break
