import secrets
import string
def generate_symbol():
    #Generate a random letter of digit
    symbol = secrets.randbelow(36)
    if symbol == 0:
         symbol = "A"
    elif symbol == 1:
         symbol = "B"
    elif symbol == 2:
         symbol = "C"
    elif symbol == 3:
         symbol = "D"
    elif symbol == 4:
         symbol = "E"
    elif symbol == 5:
         symbol = "F"
    elif symbol == 6:
         symbol = "G"
    elif symbol == 7:
         symbol = "H"
    elif symbol == 8:
         symbol = "I"
    elif symbol == 9:
         symbol = "J"
    elif symbol == 10:
         symbol = "K"
    elif symbol == 11:
         symbol = "L"
    elif symbol == 12:
         symbol = "M"
    elif symbol == 13:
         symbol = "N"
    elif symbol == 14:
         symbol = "O"
    elif symbol == 15:
         symbol = "P"
    elif symbol == 16:
         symbol = "Q"
    elif symbol == 17:
         symbol = "R"
    elif symbol == 18:
         symbol = "S"
    elif symbol == 19:
         symbol = "T"
    elif symbol == 20:
         symbol = "U"
    elif symbol == 21:
         symbol = "V"
    elif symbol == 22:
         symbol = "W"
    elif symbol == 23:
         symbol = "X"
    elif symbol == 24:
         symbol = "Y"
    elif symbol == 25:
         symbol = "Z"
    elif symbol == 26:
         symbol = "0"
    elif symbol == 27:
         symbol = "1"
    elif symbol == 28:
         symbol = "2"
    elif symbol == 29:
         symbol = "3"
    elif symbol == 30:
         symbol = "4"
    elif symbol == 31:
         symbol = "5"
    elif symbol == 32:
         symbol = "6"
    elif symbol == 33:
         symbol = "7"
    elif symbol == 34:
         symbol = "8"
    else:
         symbol = "9"
    return symbol
def check_symbol(symbol,symbol1,symbol2,symbol3,symbol4,symbol5,symbol6,symbol7,symbol8,symbol9,symbol10,symbol11,symbol12,symbol13,symbol14,symbol15,symbol16,symbol17,symbol18,symbol19,symbol20,symbol21,symbol22,symbol23,symbol24,symbol25,symbol26,symbol27,symbol28,symbol29,symbol30,symbol31,symbol32,symbol33,symbol34,symbol35, symbol36):
    #Check if the symbol is the same as any other symbol in the list (returns boolean)
    if symbol == "slot1":
        return True
    elif symbol == "slot2":
        if symbol2 == symbol1:
            return False
    elif symbol == "slot3":
        if symbol3 == symbol1 or symbol3 == symbol2:
            return False
    elif symbol == "slot4":
        if symbol4 == symbol1 or symbol4 == symbol2 or symbol4 == symbol3:
            return False
    elif symbol == "slot5":
        if symbol5 == symbol1 or symbol5 == symbol2 or symbol5 == symbol3 or symbol5 == symbol4:
            return False
    elif symbol == "slot6":
        if symbol6 == symbol1 or symbol6 == symbol2 or symbol6 == symbol3 or symbol6 == symbol4 or symbol6 == symbol5:
            return False
    elif symbol == "slot7":
        if symbol7 == symbol1 or symbol7 == symbol2 or symbol7 == symbol3 or symbol7 == symbol4 or symbol7 == symbol5 or symbol7 == symbol6:
            return False
    elif symbol == "slot8":
        if symbol8 == symbol1 or symbol8 == symbol2 or symbol8 == symbol3 or symbol8 == symbol4 or symbol8 == symbol5 or symbol8 == symbol6 or symbol8 == symbol7:
            return False
    elif symbol == "slot9":
        if symbol9 == symbol1 or symbol9 == symbol2 or symbol9 == symbol3 or symbol9 == symbol4 or symbol9 == symbol5 or symbol9 == symbol6 or symbol9 == symbol7 or symbol9 == symbol8:
            return False
    elif symbol == "slot10":
        if symbol10 == symbol1 or symbol10 == symbol2 or symbol10 == symbol3 or symbol10 == symbol4 or symbol10 == symbol5 or symbol10 == symbol6 or symbol10 == symbol7 or symbol10 == symbol8 or symbol10 == symbol9:
            return False
    elif symbol == "slot11":
        if symbol11 == symbol1 or symbol11 == symbol2 or symbol11 == symbol3 or symbol11 == symbol4 or symbol11 == symbol5 or symbol11 == symbol6 or symbol11 == symbol7 or symbol11 == symbol8 or symbol11 == symbol9 or symbol11 == symbol10:
            return False
    elif symbol == "slot12":
        if symbol12 == symbol1 or symbol12 == symbol2 or symbol12 == symbol3 or symbol12 == symbol4 or symbol12 == symbol5 or symbol12 == symbol6 or symbol12 == symbol7 or symbol12 == symbol8 or symbol12 == symbol9 or symbol12 == symbol10 or symbol12 == symbol11:
            return False
    elif symbol == "slot13":
        if symbol13 == symbol1 or symbol13 == symbol2 or symbol13 == symbol3 or symbol13 == symbol4 or symbol13 == symbol5 or symbol13 == symbol6 or symbol13 == symbol7 or symbol13 == symbol8 or symbol13 == symbol9 or symbol13 == symbol10 or symbol13 == symbol11 or symbol13 == symbol12:
            return False
    elif symbol == "slot14":
        if symbol14 == symbol1 or symbol14 == symbol2 or symbol14 == symbol3 or symbol14 == symbol4 or symbol14 == symbol5 or symbol14 == symbol6 or symbol14 == symbol7 or symbol14 == symbol8 or symbol14 == symbol9 or symbol14 == symbol10 or symbol14 == symbol11 or symbol14 == symbol12 or symbol14 == symbol13:
            return False
    elif symbol == "slot15":
        if symbol15 == symbol1 or symbol15 == symbol2 or symbol15 == symbol3 or symbol15 == symbol4 or symbol15 == symbol5 or symbol15 == symbol6 or symbol15 == symbol7 or symbol15 == symbol8 or symbol15 == symbol9 or symbol15 == symbol10 or symbol15 == symbol11 or symbol15 == symbol12 or symbol15 == symbol13 or symbol15 == symbol14:
            return False
    elif symbol == "slot16":
        if symbol16 == symbol1 or symbol16 == symbol2 or symbol16 == symbol3 or symbol16 == symbol4 or symbol16 == symbol5 or symbol16 == symbol6 or symbol16 == symbol7 or symbol16 == symbol8 or symbol16 == symbol9 or symbol16 == symbol10 or symbol16 == symbol11 or symbol16 == symbol12 or symbol16 == symbol13 or symbol16 == symbol14 or symbol16 == symbol15:
            return False
    elif symbol == "slot17":
        if symbol17 == symbol1 or symbol17 == symbol2 or symbol17 == symbol3 or symbol17 == symbol4 or symbol17 == symbol5 or symbol17 == symbol6 or symbol17 == symbol7 or symbol17 == symbol8 or symbol17 == symbol9 or symbol17 == symbol10 or symbol17 == symbol11 or symbol17 == symbol12 or symbol17 == symbol13 or symbol17 == symbol14 or symbol17 == symbol15 or symbol17 == symbol16:
            return False
    elif symbol == "slot18":
        if symbol18 == symbol1 or symbol18 == symbol2 or symbol18 == symbol3 or symbol18 == symbol4 or symbol18 == symbol5 or symbol18 == symbol6 or symbol18 == symbol7 or symbol18 == symbol8 or symbol18 == symbol9 or symbol18 == symbol10 or symbol18 == symbol11 or symbol18 == symbol12 or symbol18 == symbol13 or symbol18 == symbol14 or symbol18 == symbol15 or symbol18 == symbol16 or symbol18 == symbol17:
            return False
    elif symbol == "slot19":
        if symbol19 == symbol1 or symbol19 == symbol2 or symbol19 == symbol3 or symbol19 == symbol4 or symbol19 == symbol5 or symbol19 == symbol6 or symbol19 == symbol7 or symbol19 == symbol8 or symbol19 == symbol9 or symbol19 == symbol10 or symbol19 == symbol11 or symbol19 == symbol12 or symbol19 == symbol13 or symbol19 == symbol14 or symbol19 == symbol15 or symbol19 == symbol16 or symbol19 == symbol17 or symbol19 == symbol18:
            return False
    elif symbol == "slot20":
        if symbol20 == symbol1 or symbol20 == symbol2 or symbol20 == symbol3 or symbol20 == symbol4 or symbol20 == symbol5 or symbol20 == symbol6 or symbol20 == symbol7 or symbol20 == symbol8 or symbol20 == symbol9 or symbol20 == symbol10 or symbol20 == symbol11 or symbol20 == symbol12 or symbol20 == symbol13 or symbol20 == symbol14 or symbol20 == symbol15 or symbol20 == symbol16 or symbol20 == symbol17 or symbol20 == symbol18 or symbol20 == symbol19:
            return False
    elif symbol == "slot21":
        if symbol21 == symbol1 or symbol21 == symbol2 or symbol21 == symbol3 or symbol21 == symbol4 or symbol21 == symbol5 or symbol21 == symbol6 or symbol21 == symbol7 or symbol21 == symbol8 or symbol21 == symbol9 or symbol21 == symbol10 or symbol21 == symbol11 or symbol21 == symbol12 or symbol21 == symbol13 or symbol21 == symbol14 or symbol21 == symbol15 or symbol21 == symbol16 or symbol21 == symbol17 or symbol21 == symbol18 or symbol21 == symbol19 or symbol21 == symbol20:
            return False
    elif symbol == "slot22":
        if symbol22 == symbol1 or symbol22 == symbol2 or symbol22 == symbol3 or symbol22 == symbol4 or symbol22 == symbol5 or symbol22 == symbol6 or symbol22 == symbol7 or symbol22 == symbol8 or symbol22 == symbol9 or symbol22 == symbol10 or symbol22 == symbol11 or symbol22 == symbol12 or symbol22 == symbol13 or symbol22 == symbol14 or symbol22 == symbol15 or symbol22 == symbol16 or symbol22 == symbol17 or symbol22 == symbol18 or symbol22 == symbol19 or symbol22 == symbol20 or symbol22 == symbol21:
            return False
    elif symbol == "slot23":
        if symbol23 == symbol1 or symbol23 == symbol2 or symbol23 == symbol3 or symbol23 == symbol4 or symbol23 == symbol5 or symbol23 == symbol6 or symbol23 == symbol7 or symbol23 == symbol8 or symbol23 == symbol9 or symbol23 == symbol10 or symbol23 == symbol11 or symbol23 == symbol12 or symbol23 == symbol13 or symbol23 == symbol14 or symbol23 == symbol15 or symbol23 == symbol16 or symbol23 == symbol17 or symbol23 == symbol18 or symbol23 == symbol19 or symbol23 == symbol20 or symbol23 == symbol21 or symbol23 == symbol22:
            return False
    elif symbol == "slot24":
        if symbol24 == symbol1 or symbol24 == symbol2 or symbol24 == symbol3 or symbol24 == symbol4 or symbol24 == symbol5 or symbol24 == symbol6 or symbol24 == symbol7 or symbol24 == symbol8 or symbol24 == symbol9 or symbol24 == symbol10 or symbol24 == symbol11 or symbol24 == symbol12 or symbol24 == symbol13 or symbol24 == symbol14 or symbol24 == symbol15 or symbol24 == symbol16 or symbol24 == symbol17 or symbol24 == symbol18 or symbol24 == symbol19 or symbol24 == symbol20 or symbol24 == symbol21 or symbol24 == symbol22 or symbol24 == symbol23:
            return False
    elif symbol == "slot25":
        if symbol25 == symbol1 or symbol25 == symbol2 or symbol25 == symbol3 or symbol25 == symbol4 or symbol25 == symbol5 or symbol25 == symbol6 or symbol25 == symbol7 or symbol25 == symbol8 or symbol25 == symbol9 or symbol25 == symbol10 or symbol25 == symbol11 or symbol25 == symbol12 or symbol25 == symbol13 or symbol25 == symbol14 or symbol25 == symbol15 or symbol25 == symbol16 or symbol25 == symbol17 or symbol25 == symbol18 or symbol25 == symbol19 or symbol25 == symbol20 or symbol25 == symbol21 or symbol25 == symbol22 or symbol25 == symbol23 or symbol25 == symbol24:
            return False
    elif symbol == "slot26":
        if symbol26 == symbol1 or symbol26 == symbol2 or symbol26 == symbol3 or symbol26 == symbol4 or symbol26 == symbol5 or symbol26 == symbol6 or symbol26 == symbol7 or symbol26 == symbol8 or symbol26 == symbol9 or symbol26 == symbol10 or symbol26 == symbol11 or symbol26 == symbol12 or symbol26 == symbol13 or symbol26 == symbol14 or symbol26 == symbol15 or symbol26 == symbol16 or symbol26 == symbol17 or symbol26 == symbol18 or symbol26 == symbol19 or symbol26 == symbol20 or symbol26 == symbol21 or symbol26 == symbol22 or symbol26 == symbol23 or symbol26 == symbol24 or symbol26 == symbol25:
            return False
    elif symbol == "slot27":
        if symbol27 == symbol1 or symbol27 == symbol2 or symbol27 == symbol3 or symbol27 == symbol4 or symbol27 == symbol5 or symbol27 == symbol6 or symbol27 == symbol7 or symbol27 == symbol8 or symbol27 == symbol9 or symbol27 == symbol10 or symbol27 == symbol11 or symbol27 == symbol12 or symbol27 == symbol13 or symbol27 == symbol14 or symbol27 == symbol15 or symbol27 == symbol16 or symbol27 == symbol17 or symbol27 == symbol18 or symbol27 == symbol19 or symbol27 == symbol20 or symbol27 == symbol21 or symbol27 == symbol22 or symbol27 == symbol23 or symbol27 == symbol24 or symbol27 == symbol25 or symbol27 == symbol26:
            return False
    elif symbol == "slot28":
        if symbol28 == symbol1 or symbol28 == symbol2 or symbol28 == symbol3 or symbol28 == symbol4 or symbol28 == symbol5 or symbol28 == symbol6 or symbol28 == symbol7 or symbol28 == symbol8 or symbol28 == symbol9 or symbol28 == symbol10 or symbol28 == symbol11 or symbol28 == symbol12 or symbol28 == symbol13 or symbol28 == symbol14 or symbol28 == symbol15 or symbol28 == symbol16 or symbol28 == symbol17 or symbol28 == symbol18 or symbol28 == symbol19 or symbol28 == symbol20 or symbol28 == symbol21 or symbol28 == symbol22 or symbol28 == symbol23 or symbol28 == symbol24 or symbol28 == symbol25 or symbol28 == symbol26 or symbol28 == symbol27:
            return False
    elif symbol == "slot29":
        if symbol29 == symbol1 or symbol29 == symbol2 or symbol29 == symbol3 or symbol29 == symbol4 or symbol29 == symbol5 or symbol29 == symbol6 or symbol29 == symbol7 or symbol29 == symbol8 or symbol29 == symbol9 or symbol29 == symbol10 or symbol29 == symbol11 or symbol29 == symbol12 or symbol29 == symbol13 or symbol29 == symbol14 or symbol29 == symbol15 or symbol29 == symbol16 or symbol29 == symbol17 or symbol29 == symbol18 or symbol29 == symbol19 or symbol29 == symbol20 or symbol29 == symbol21 or symbol29 == symbol22 or symbol29 == symbol23 or symbol29 == symbol24 or symbol29 == symbol25 or symbol29 == symbol26 or symbol29 == symbol27 or symbol29 == symbol28:
            return False
    elif symbol == "slot30":
        if symbol30 == symbol1 or symbol30 == symbol2 or symbol30 == symbol3 or symbol30 == symbol4 or symbol30 == symbol5 or symbol30 == symbol6 or symbol30 == symbol7 or symbol30 == symbol8 or symbol30 == symbol9 or symbol30 == symbol10 or symbol30 == symbol11 or symbol30 == symbol12 or symbol30 == symbol13 or symbol30 == symbol14 or symbol30 == symbol15 or symbol30 == symbol16 or symbol30 == symbol17 or symbol30 == symbol18 or symbol30 == symbol19 or symbol30 == symbol20 or symbol30 == symbol21 or symbol30 == symbol22 or symbol30 == symbol23 or symbol30 == symbol24 or symbol30 == symbol25 or symbol30 == symbol26 or symbol30 == symbol27 or symbol30 == symbol28 or symbol30 == symbol29:
            return False
    elif symbol == "slot31":
        if symbol31 == symbol1 or symbol31 == symbol2 or symbol31 == symbol3 or symbol31 == symbol4 or symbol31 == symbol5 or symbol31 == symbol6 or symbol31 == symbol7 or symbol31 == symbol8 or symbol31 == symbol9 or symbol31 == symbol10 or symbol31 == symbol11 or symbol31 == symbol12 or symbol31 == symbol13 or symbol31 == symbol14 or symbol31 == symbol15 or symbol31 == symbol16 or symbol31 == symbol17 or symbol31 == symbol18 or symbol31 == symbol19 or symbol31 == symbol20 or symbol31 == symbol21 or symbol31 == symbol22 or symbol31 == symbol23 or symbol31 == symbol24 or symbol31 == symbol25 or symbol31 == symbol26 or symbol31 == symbol27 or symbol31 == symbol28 or symbol31 == symbol29 or symbol31 == symbol30:
            return False
    elif symbol == "slot32":
        if symbol32 == symbol1 or symbol32 == symbol2 or symbol32 == symbol3 or symbol32 == symbol4 or symbol32 == symbol5 or symbol32 == symbol6 or symbol32 == symbol7 or symbol32 == symbol8 or symbol32 == symbol9 or symbol32 == symbol10 or symbol32 == symbol11 or symbol32 == symbol12 or symbol32 == symbol13 or symbol32 == symbol14 or symbol32 == symbol15 or symbol32 == symbol16 or symbol32 == symbol17 or symbol32 == symbol18 or symbol32 == symbol19 or symbol32 == symbol20 or symbol32 == symbol21 or symbol32 == symbol22 or symbol32 == symbol23 or symbol32 == symbol24 or symbol32 == symbol25 or symbol32 == symbol26 or symbol32 == symbol27 or symbol32 == symbol28 or symbol32 == symbol29 or symbol32 == symbol30 or symbol32 == symbol31:
            return False
    elif symbol == "slot33":
        if symbol33 == symbol1 or symbol33 == symbol2 or symbol33 == symbol3 or symbol33 == symbol4 or symbol33 == symbol5 or symbol33 == symbol6 or symbol33 == symbol7 or symbol33 == symbol8 or symbol33 == symbol9 or symbol33 == symbol10 or symbol33 == symbol11 or symbol33 == symbol12 or symbol33 == symbol13 or symbol33 == symbol14 or symbol33 == symbol15 or symbol33 == symbol16 or symbol33 == symbol17 or symbol33 == symbol18 or symbol33 == symbol19 or symbol33 == symbol20 or symbol33 == symbol21 or symbol33 == symbol22 or symbol33 == symbol23 or symbol33 == symbol24 or symbol33 == symbol25 or symbol33 == symbol26 or symbol33 == symbol27 or symbol33 == symbol28 or symbol33 == symbol29 or symbol33 == symbol30 or symbol33 == symbol31 or symbol33 == symbol32:
            return False
    elif symbol == "slot34":
        if symbol34 == symbol1 or symbol34 == symbol2 or symbol34 == symbol3 or symbol34 == symbol4 or symbol34 == symbol5 or symbol34 == symbol6 or symbol34 == symbol7 or symbol34 == symbol8 or symbol34 == symbol9 or symbol34 == symbol10 or symbol34 == symbol11 or symbol34 == symbol12 or symbol34 == symbol13 or symbol34 == symbol14 or symbol34 == symbol15 or symbol34 == symbol16 or symbol34 == symbol17 or symbol34 == symbol18 or symbol34 == symbol19 or symbol34 == symbol20 or symbol34 == symbol21 or symbol34 == symbol22 or symbol34 == symbol23 or symbol34 == symbol24 or symbol34 == symbol25 or symbol34 == symbol26 or symbol34 == symbol27 or symbol34 == symbol28 or symbol34 == symbol29 or symbol34 == symbol30 or symbol34 == symbol31 or symbol34 == symbol32 or symbol34 == symbol33:
            return False
    elif symbol == "slot35":
        if symbol35 == symbol1 or symbol35 == symbol2 or symbol35 == symbol3 or symbol35 == symbol4 or symbol35 == symbol5 or symbol35 == symbol6 or symbol35 == symbol7 or symbol35 == symbol8 or symbol35 == symbol9 or symbol35 == symbol10 or symbol35 == symbol11 or symbol35 == symbol12 or symbol35 == symbol13 or symbol35 == symbol14 or symbol35 == symbol15 or symbol35 == symbol16 or symbol35 == symbol17 or symbol35 == symbol18 or symbol35 == symbol19 or symbol35 == symbol20 or symbol35 == symbol21 or symbol35 == symbol22 or symbol35 == symbol23 or symbol35 == symbol24 or symbol35 == symbol25 or symbol35 == symbol26 or symbol35 == symbol27 or symbol35 == symbol28 or symbol35 == symbol29 or symbol35 == symbol30 or symbol35 == symbol31 or symbol35 == symbol32 or symbol35 == symbol33 or symbol35 == symbol34:
            return False
    elif symbol == "slot36":
        if symbol36 == symbol1 or symbol36 == symbol2 or symbol36 == symbol3 or symbol36 == symbol4 or symbol36 == symbol5 or symbol36 == symbol6 or symbol36 == symbol7 or symbol36 == symbol8 or symbol36 == symbol9 or symbol36 == symbol10 or symbol36 == symbol11 or symbol36 == symbol12 or symbol36 == symbol13 or symbol36 == symbol14 or symbol36 == symbol15 or symbol36 == symbol16 or symbol36 == symbol17 or symbol36 == symbol18 or symbol36 == symbol19 or symbol36 == symbol20 or symbol36 == symbol21 or symbol36 == symbol22 or symbol36 == symbol23 or symbol36 == symbol24 or symbol36 == symbol25 or symbol36 == symbol26 or symbol36 == symbol27 or symbol36 == symbol28 or symbol36 == symbol29 or symbol36 == symbol30 or symbol36 == symbol31 or symbol36 == symbol32 or symbol36 == symbol33 or symbol36 ==symbol34: 
            return False
    return True
def gen_code_symbol():
     symbol = secrets.randbelow(31)
     if symbol == 0:
        symbol = "!"
     elif symbol == 1:
         symbol = '"'
     elif symbol == 2:
         symbol = "#"
     elif symbol == 3:
         symbol = "$"
     elif symbol == 4:
         symbol = "%"
     elif symbol == 5:
         symbol = "&"
     elif symbol == 6:
         symbol = "'"
     elif symbol == 7:
         symbol = "("
     elif symbol == 8:
         symbol = ")"
     elif symbol == 9:
         symbol = "*"
     elif symbol == 10:
         symbol = "+"
     elif symbol == 11:
         symbol = ","
     elif symbol == 12:
         symbol = "-"
     elif symbol == 13:
         symbol = "."
     elif symbol == 14:
         symbol = "/"
     elif symbol == 15:
         symbol = ":"
     elif symbol == 16:
         symbol = ";"
     elif symbol == 17:
         symbol = "<"
     elif symbol == 18:
         symbol = ">"
     elif symbol == 19:
         symbol = "?"
     elif symbol == 20:
         symbol = "@"
     elif symbol == 21:
         symbol = "["
     elif symbol == 22:
         symbol = "\\"
     elif symbol == 23:
         symbol = "]"
     elif symbol == 24:
         symbol = "^"
     elif symbol == 25:
         symbol = "_"
     elif symbol == 26:
         symbol = "`"
     elif symbol == 27:
         symbol = "{"
     elif symbol == 28:
         symbol = "|"
     elif symbol == 29:
         symbol = "}"
     elif symbol == 30:
         symbol = "~"
     return symbol
def check_cypher(symbol,symbol1,symbol2,symbol3,symbol4,symbol5,symbol6,symbol7,symbol8,symbol9,symbol10,symbol11,symbol12,):
    #Check if the symbol is the same as any other symbol in the list (returns boolean)
    if symbol == "cypher1":
        return True
    elif symbol == "cypher2":
        if symbol2 == symbol1:
            return False
    elif symbol == "cypher3":
        if symbol3 == symbol1 or symbol3 == symbol2:
            return False
    elif symbol == "cypher4":
        if symbol4 == symbol1 or symbol4 == symbol2 or symbol4 == symbol3:
            return False
    elif symbol == "cypher5":
        if symbol5 == symbol1 or symbol5 == symbol2 or symbol5 == symbol3 or symbol5 == symbol4:
            return False
    elif symbol == "cypher6":
        if symbol6 == symbol1 or symbol6 == symbol2 or symbol6 == symbol3 or symbol6 == symbol4 or symbol6 == symbol5:
            return False
    elif symbol == "cypher7":
        if symbol7 == symbol1 or symbol7 == symbol2 or symbol7 == symbol3 or symbol7 == symbol4 or symbol7 == symbol5 or symbol7 == symbol6:
            return False
    elif symbol == "cypher8":
        if symbol8 == symbol1 or symbol8 == symbol2 or symbol8 == symbol3 or symbol8 == symbol4 or symbol8 == symbol5 or symbol8 == symbol6 or symbol8 == symbol7:
            return False
    elif symbol == "cypher9":
        if symbol9 == symbol1 or symbol9 == symbol2 or symbol9 == symbol3 or symbol9 == symbol4 or symbol9 == symbol5 or symbol9 == symbol6 or symbol9 == symbol7 or symbol9 == symbol8:
            return False
    elif symbol == "cypher10":
        if symbol10 == symbol1 or symbol10 == symbol2 or symbol10 == symbol3 or symbol10 == symbol4 or symbol10 == symbol5 or symbol10 == symbol6 or symbol10 == symbol7 or symbol10 == symbol8 or symbol10 == symbol9:
            return False
    elif symbol == "cypher11":
        if symbol11 == symbol1 or symbol11 == symbol2 or symbol11 == symbol3 or symbol11 == symbol4 or symbol11 == symbol5 or symbol11 == symbol6 or symbol11 == symbol7 or symbol11 == symbol8 or symbol11 == symbol9 or symbol11 == symbol10:
            return False
    elif symbol == "cypher12":
        if symbol12 == symbol1 or symbol12 == symbol2 or symbol12 == symbol3 or symbol12 == symbol4 or symbol12 == symbol5 or symbol12 == symbol6 or symbol12 == symbol7 or symbol12 == symbol8 or symbol12 == symbol9 or symbol12 == symbol10 or symbol12 == symbol11:
            return False
    return True