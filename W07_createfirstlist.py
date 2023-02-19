def main():
    #create a list. this is a list of strings, but a list can contain any kind of data, such as numbers
    my_list = ["Read the scriptures", "Do my homework", "Clean the house", "Feed the animals", "Go to the store"]

    # print the list - see the print_list function below
    print_list(my_list)

    ########################################################################
    # get one item from the list.
    # The first item in the list is item 0 (my_list[0]).
    # The next item is item 1 (my_list[1]) and so on.
    # to get an item from the list, you can do it list this:
    my_item = my_list[0]
    print(f"The first item in the list is '{my_item}'")
    # get and print the second item from the list
    my_item = my_list[1]
    print(f"The second item in the list is '{my_item}'")

    ########################################################################
    # add an item to the end of the list
    my_list.append("Say prayers")
    # print the list - make sure the item we added is there
    print_list(my_list)

    ########################################################################
    # remove an item from the list
    # there are many different ways to remove an item from a list
    # this is one way
    item_to_delete = my_list[2]
    my_list.remove(item_to_delete)
    # print the list - make sure the item we deleted is gone
    print_list(my_list)


def print_list(list):
    #print how many items are in the list
    count = len(list)
    print(f">> There are {count} items in the list")
    # print every item in the list
    for i in list:
        print(f"{i}")


if __name__ == "__main__":
    main()