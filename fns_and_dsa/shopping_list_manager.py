def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added '{item}' to the shopping list.")
            else:
                print("No item entered. Please try again.")
                
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
                
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()