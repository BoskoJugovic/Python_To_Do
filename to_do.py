import json
from json.decoder import JSONDecodeError

filename = 'to_do.txt'
to_do_list = []
try:
    with open(filename) as f:
        try:
            to_do_list = json.load(f)
        except JSONDecodeError:
            pass
except FileNotFoundError:
    print("Create a file 'to_do.txt' in this folder")
    exit()


def take_input():
    while True:
        choice = input("\nWelcome! (Type 'exit' if you want to end the app)\n"
                       "\t1) Create new item\n"
                       "\t2) List all existing items\n"
                       "\t3) Sort all existing items\n"
                       "\t4) Search for an item\n"
                       "\t5) Delete an item\n"
                       "Your choice: ")

        if choice == 'exit':
            return
        elif choice == '1':
            create()
        elif choice == '2':
            list_items()
        elif choice == '3':
            sort_by = input("\nSort by:"
                              "\n\t1) Title"
                              "\n\t2) Priority"
                              "\nYour choice: ")
            asc_desc = input("\n\t1)Ascending"
                             "\n\t2)Descending"
                             "\nYour choice: ")
            if (sort_by == '1' or sort_by == '2') and (asc_desc == '1' or asc_desc == '2'):
                sort(sort_by, asc_desc)
        elif choice == '4':
            search_by = input("\nSearch by:"
                              "\n\t1) Title"
                              "\n\t2) Priority"
                              "\nYour choice: ")
            if search_by == '1' or search_by == '2':
                search(search_by)
        elif choice == '5':
            delete()
        else:
            print("\nChoose an option from 1 - 5\n")


def create():
    while True:
        print("\nType 'go back' to return to the menu and 'exit app' to end the app\n")
        title = input("Title: ").strip()
        if title == '':
            break

        content = input("Content: ").strip()
        if content == '':
            break

        priority = input("Priority (number 1 - 5): ").strip()
        try:
            if int(priority) not in range(1, 6):
                break
        except ValueError:
            print('Priority must be a number between 1 and 5')

        items = {
            'Title': f'{title}',
            'Content': f'{content}',
            'Priority': f'{priority}'
        }

        to_do_list.append(items)
        save(to_do_list)

        choice = input("\nDo you want to enter another item:"
                       "\n\t1) Yes"
                       "\n\t2) No"
                       "\nYour choice: ")
        if choice == '1':
            continue
        else:
            break


def list_items():
    try:
        for item in to_do_list:
            print('\n')
            for key, value in item.items():
                print(f"{key}: {value}")
    except ValueError:
        print("\nYou need to add items to the list first")


def sort(sort_by, asc_desc):
    if sort_by == '1':
        if asc_desc == '1':
            sorted_list = sorted(to_do_list, key=lambda d: d['Title'])
        else:
            sorted_list = sorted(to_do_list, key=lambda d: d['Title'], reverse=True)
    else:
        if asc_desc == '1':
            sorted_list = sorted(to_do_list, key=lambda d: d['Priority'])
        else:
            sorted_list = sorted(to_do_list, key=lambda d: d['Priority'], reverse=True)
    save(sorted_list)

def search(search_by):
    item_found = False
    if search_by == '1':
        search_item = input("\nTitle: ")
        for item in to_do_list:
            if search_item == item['Title']:
                print(item)
                item_found = True
    else:
        search_item = input("\nPriority: ")
        for item in to_do_list:
            if search_item == item['Priority']:
                print()
                item_found = True

    if not item_found:
        print("\nNo such items found")

def delete():
    item_to_delete = input("What item would you like to delete? ")
    for item in to_do_list:
        if item_to_delete == item['Title']:
            deleted_item = item
            to_do_list.remove(deleted_item)
            print(f"\nSuccessfully deleted {deleted_item['Title']}")
            save(to_do_list)
            return
    print("\nNo such item found in file")


def save(items):
    with open(filename, 'w') as f:
        f.write(json.dumps(items))


take_input()
