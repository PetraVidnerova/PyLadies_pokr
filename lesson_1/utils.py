def yes_or_no(question):
    while True:
        response = input(question+" A/N ")
        if not response:
            continue
        first_letter = response[0].upper()
        if first_letter == "A":
            return True
        if first_letter == "N":
            return False

def menu(list_of_options):
    print()
    for i, option in enumerate(list_of_options):
        print(f"{i:>3}. {option}")
    print()
    
    while True:
        try:
            return int(input("Co si vybereš? "))
        except ValueError:
            continue
    
def login():
    jmeno = input("Zadej svůj login: ")
    return jmeno
    
