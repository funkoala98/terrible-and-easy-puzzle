import letter_generator
passed_check = False
attempts = 0
slot = 0
slot1 = ""
slot2 = ""
slot3 = ""
slot4 = ""
slot5 = ""
slot6 = ""
slot7 = ""
slot8 = ""
slot9 = ""
slot10 = ""
slot11 = ""
slot12 = ""
slot13 = ""
slot14 = ""
slot15 = ""
slot16 = ""
slot17 = ""
slot18 = ""
slot19 = ""
slot20 = ""
slot21 = ""
slot22 = ""
slot23 = ""
slot24 = ""
slot25 = ""
slot26 = ""
slot27 = ""
slot28 = ""
slot29 = ""
slot30 = ""
slot31 = ""
slot32 = ""
slot33 = ""
slot34 = ""
slot35 = ""
slot36 = ""

cypher1 = ""
cypher2 = ""
cypher3 = ""
cypher4 = ""
cypher5 = ""
cypher6 = ""
cypher7 = ""
cypher8 = ""
cypher9 = ""
cypher10 = ""
cypher11 = ""
cypher12 = ""

debug_mode = input("Debug mode? (y/n): ")
debug_mode = debug_mode == "y" or debug_mode == "Y"
print(debug_mode)

slot1 = letter_generator.generate_symbol()
if debug_mode:
    print("Slot 1: " + slot1)

while not passed_check:
    slot2 = letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot2", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 2: " + slot2 + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot3= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot3", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 3: " + slot3+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot4= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot4", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 4: " + slot4+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot5= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot5", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 5: " + slot5+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot6= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot6", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 6: " + slot6+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot7= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot7", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 7: " + slot7+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot8= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot8", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 8: " + slot8+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot9= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot9", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 9: " + slot9+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot10= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot10", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 10: " + slot10+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot11= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot11", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 11: " + slot11+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot12= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot12", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 12: " + slot12+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot13= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot13", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 13: " + slot13+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot14= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot14", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 14: " + slot14+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot15= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot15", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 15: " + slot15+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot16= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot16", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 16: " + slot16+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot17= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot17", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 17: " + slot17+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot18= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot18", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 18: " + slot18+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot19= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot19", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 19: " + slot19+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot20= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot20", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 20: " + slot20+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot21= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot21", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 21: " + slot21+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot22= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot22", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 22: " + slot22+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot23= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot23", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 23: " + slot23+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot24= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot24", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 24: " + slot24+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot25= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot25", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 25: " + slot25+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot26= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot26", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 26: " + slot26+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot27= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot27", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 27: " + slot27+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot28= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot28", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 28: " + slot28+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot29= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot29", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 29: " + slot29+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot30= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot30", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 30: " + slot30+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot31= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot31", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 31: " + slot31+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot32= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot32", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 32: " + slot32+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot33= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot33", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 33: " + slot33+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot34= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot34", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 34: " + slot34+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot35= letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot35", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 35: " + slot35+ " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    slot36 = letter_generator.generate_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_symbol("slot36", slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26, slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36)
    if debug_mode:
        print("Slot 36: " + slot36 + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False


while not passed_check:
    cypher1 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher1", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 1: " + str(cypher1) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher2= letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher2", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 2: " + str(cypher2) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher3 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher3", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 3: " + str(cypher3) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher4 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher4", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 4: " + str(cypher4) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher5 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher5", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 5: " + str(cypher5) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher6 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher6", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 6: " + str(cypher6) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher7 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher7", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 7: " + str(cypher7) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher8 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher8", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 8: " + str(cypher8) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher9 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher9", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 9: " + str(cypher9) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher10 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher10", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 10: " + str(cypher10) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher11 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher11", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 11: " + str(cypher11) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False

while not passed_check:
    cypher12 = letter_generator.gen_code_symbol()
    attempts = attempts + 1
    passed_check = letter_generator.check_cypher("cypher12", cypher1, cypher2, cypher3, cypher4, cypher5, cypher6, cypher7, cypher8, cypher9, cypher10, cypher11, cypher12)
    if debug_mode:
        print("Cypher 12: " + str(cypher12) + " (attempt " + str(attempts) + ")")
attempts = 0
passed_check= False


print("  | " + str(cypher1) + " | " + str(cypher2) + " | " + str(cypher3) + " | " + str(cypher4) + " | " + str(cypher5) + " | " + str(cypher6) + " |")
print("---------------------------")
print(str(cypher7) + " | " + str(slot1) + " | " + str(slot2) + " | " + str(slot3) + " | " + str(slot4) + " | " + str(slot5) + " | " + str(slot6) + " |")
print("---------------------------")
print(str(cypher8) + " | " + str(slot7) + " | " + str(slot8) + " | " + str(slot9) + " | " + str(slot10) + " | " + str(slot11) + " | " + str(slot12) + " |")
print("---------------------------")
print(str(cypher9) + " | " + str(slot13) + " | " + str(slot14) + " | " + str(slot15) + " | " + str(slot16) + " | " + str(slot17) + " | " + str(slot18) + " |")
print("---------------------------")
print(str(cypher10) + " | " + str(slot19) + " | " + str(slot20) + " | " + str(slot21) + " | " + str(slot22) + " | " + str(slot23) + " | " + str(slot24) + " |")
print("---------------------------")
print(str(cypher11) + " | " + str(slot25) + " | " + str(slot26) + " | " + str(slot27) + " | " + str(slot28) + " | " + str(slot29) + " | " + str(slot30) + " |")
print("---------------------------")
print(str(cypher12) + " | " + str(slot31) + " | " + str(slot32) + " | " + str(slot33) + " | " + str(slot34) + " | " + str(slot35) + " | " + str(slot36) + " |")
print("---------------------------")