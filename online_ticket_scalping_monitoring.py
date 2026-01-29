# Online Ticket Scalping Monitor - POC

transactions = []

def print_menu():
    print("\n1. Create transaction log")
    print("2. Read transaction logs")
    print("3. Update transaction log")
    print("4. Delete transaction log")
    print("5. Detect scalping activities")
    print("6. Analyze ticket trends")
    print("7. Exit")

def create_transaction():
    event_id = input("Enter event ID: ")
    ticket_id = input("Enter ticket ID: ")
    price = float(input("Enter price: "))
    transactions.append({
        "event_id": event_id,
        "ticket_id": ticket_id,
        "price": price
    })

def read_transactions():
    if not transactions:
        print("No transaction logs available.")
        return
    for i, t in enumerate(transactions):
        print(i, t)

def update_transaction():
    if not transactions:
        print("No logs to update.")
        return
    index = int(input("Enter index of transaction log to update: "))
    if 0 <= index < len(transactions):
        transactions[index]["event_id"] = input("Enter new event ID: ")
        transactions[index]["ticket_id"] = input("Enter new ticket ID: ")
        transactions[index]["price"] = float(input("Enter new price: "))
    else:
        print("Invalid index.")

def delete_transaction():
    if not transactions:
        print("No logs to delete.")
        return
    index = int(input("Enter index of transaction log to delete: "))
    if 0 <= index < len(transactions):
        transactions.pop(index)
        print("Transaction log deleted.")
    else:
        print("Invalid index.")

def detect_scalping():
    prices = {}
    for t in transactions:
        key = (t["event_id"], t["ticket_id"])
        prices.setdefault(key, []).append(t["price"])

    scalping_found = False
    for p in prices.values():
        if len(p) >= 3 and p == sorted(p):
            scalping_found = True

    if scalping_found:
        print("Potential scalping activities detected.")
    else:
        print("No potential scalping activities detected.")

def analyze_trends():
    if not transactions:
        print("No data available for analysis.")
        return
    price_list = [t["price"] for t in transactions]
    print("Patterns indicative of scalping behavior identified:")
    print(price_list)

def main():
    while True:
        print_menu()
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            create_transaction()
        elif choice == 2:
            read_transactions()
        elif choice == 3:
            update_transaction()
        elif choice == 4:
            delete_transaction()
        elif choice == 5:
            detect_scalping()
        elif choice == 6:
            analyze_trends()
        elif choice == 7:
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

main()
