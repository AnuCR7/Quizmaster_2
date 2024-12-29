goldenisland={'gold coins','diamonds','rubies','emeralds','sapphires'}
silverisland={'silver coins','emeralds','rubies','pearls'}

def display_treasures():
    print('golden island treasures',goldenisland)
    print('silver island treasures',silverisland)

#union
def combine_treasures():
    combined=goldenisland.union(silverisland)
    print('all treasures',combined)

#intersection
def split_treasures():
    split=goldenisland.intersection(silverisland)
    print(split)

#difference
def differ_treasure():
    unique=goldenisland.difference(silverisland)
    print('\n Treasure(s) unique to Golden Island are ',unique)

#difference
def differ_treasure_1():
    unique_2=silverisland.difference(goldenisland)
    print('\n Treasure(s) unique to Silver Island are ',unique_2)

#Symmetric Difference
def unique_to_either():
    unique_1=goldenisland.symmetric_difference(silverisland)
    print('\n Treasures unique to both islands are ',unique_1)



def menu():
    while True:
        print("\n--- Treasure Hunt Menu ---")
        print("1. Display Treasures")
        print("2. Combine Treasures (Union)")
        print("3. Common Treasures (Intersection)")
        print("4. Unique to Golden Island (Difference)")
        print("5. Unique to Silver Island (Difference)")
        print("6. Unique to Either Island (Symmetric Difference)")
        print("7. Add a Treasure")
        print("8. Remove a Treasure")
        print("9. Check for a Treasure")
        print("0. Exit")
        choice=input('\n choose an option: ')
        if choice=='1':
            display_treasures()
        elif choice=='2':
            combine_treasures()
        elif choice=='3':
            split_treasures()
        elif choice=='4':
            differ_treasure()
        elif choice=='5':
            differ_treasure_1()
        elif choice=='3':
            unique_to_either()
        elif choice=='0':
            print('Goodbye Adventurer')
            break
        else:
            print('Invalid option please try again')


            


menu()