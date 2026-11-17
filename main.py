import coffeeserver, cafeserver



# Back-End
def main_menu():
    print("=====================================")
    print("Welcome to x coffee app")
    print("how may I help you?")
    print("A. Find a recommended cafe near your chosen location")
    print("B. Coffee Recipe")
    print("=====================================")
    menuSelect = input("Selection: ")
    if menuSelect == ("A"):
        confirmA = input("You have selected A. Find a recoomended cafe near your chosen location. confirm? (Y/N)")
        if confirmA == ("Y"):
            SelectA
        elif confirmA == ("N"):
            main_menu()
        else:
            print("invalid character detected going back to the start...")
            print("=====================================")
            main_menu()

def SelectA():
    print("Selection A Confirmed")
    print("Where would you like to find a cafe? enter a location: City" )
    cafe_loc_find = input("Cafe: ")

# Front-End
main_menu()
