def load_stock(): #el awal na5od el mawgood fl file ne7otoh f an empty dict
    stock={}
    try:
        with open("stock.txt", "r") as file:
            for line in file:
                line=line.strip()
                if not line:
                    continue
                name, quantity = line.split(",")
                stock[name.strip().lower()] = int(quantity)
    except FileNotFoundError:
        print("Error: stock.txt was not found.")
    except (ValueError, IndexError):
        print("Error: stock.txt contains corrupted data.")
    return stock

def save_stock(stock): #deh 34an lma nezawed use it to save 
    with open("stock.txt", "w") as file:
        for name, quantity in stock.items():
            file.write(f"{name},{quantity}\n")

def show_stock(stock): #display lw feh items or say if empty
    if not stock:
        print("Stock is empty.")
        return

    for index, (name, quantity) in enumerate(stock.items(), start=1): #starting el id b 1 34an n display sa7
        print(f"{index}. {name}: {quantity}")

def get_stock_name(stock): #helper function 34an tozbot el input bta3 el user to the exact one
    show_stock(stock)

    choice = input("Enter stock name or ID: ").strip()

    if choice.isdigit(): #lw input kan rakam
        stock_id = int(choice) #lazem type caasting cause it's taking a string wna ha compare with int
        names = list(stock.keys()) #n sync them ma3 el keys el mawgooda

        if 1 <= stock_id <= len(names):
            return names[stock_id - 1] #IMP el -1 34an el zero indexing wna badya el id mn 1

        print("Invalid stock ID.") #ka2enaha else
        return None

    return choice.lower() 

def add_stock(stock):
    name = get_stock_name(stock)
    if name is None: #lw none is typed
        return
    if name not in stock: #dah to add a whole new item
        print("This is a new stock item.")
    while True:
        amount = input("Enter how much to add: ").strip()
        if not amount.isdigit():
            print("Please enter a valid positive number.")
            continue
        amount = int(amount) #nafs fkrt 34an input s str
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue
        break
    if name in stock: #lw not a neew item
        stock[name] += amount
    else: #lw a new item
        stock[name] = amount
    print(f"{amount} added to {name}.")

def remove_stock(stock):
    show_stock(stock)
    choice = input("Enter stock name or ID: ").strip()
    if choice.isdigit():
        stock_id = int(choice)
        names = list(stock.keys())
        if not (1 <= stock_id <= len(names)):
            print("Invalid stock ID.")
            return
        name = names[stock_id - 1] #same as prev
    else:
        name = choice.lower()
        if name not in stock:
            print("Stock item does not exist.") #lazem yeb2a mawgood to remove it
            return
    while True:
        amount = input("Enter how much to remove: ").strip()
        if not amount.isdigit():
            print("Please enter a valid positive number.")
            continue
        amount = int(amount)
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue
        if amount > stock[name]:
            print("Cannot remove more stock than available.") #mayenfa34 yeb2a feh stock bl -1 after removing akeed
            continue
        break
    stock[name] -= amount
    print(f"{amount} removed from {name}.")

def main():
    stock = load_stock()
    while True:
        print("\n        STOCK MANAGER      ")
        print("1.Add stock")
        print("2.Remove stock")
        print("3.Show stock")
        print("4.Exit")
        choice = input("Enter your choice: ").strip()
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue
        if choice == "1":
            add_stock(stock)
        elif choice == "2":
            remove_stock(stock)
        elif choice == "3":
            show_stock(stock)
        elif choice == "4":
            save_stock(stock)
            print("Stock saved. Goodbye!")
            break
if __name__ == "__main__":
    main()