from tkinter import *
# Mosque class is imported here
from mosques import Mosque

# start tkinter
root = Tk()
root.geometry("800x260")
root.title("Mosques Application by Ahmed AlTurki")

# globals
mosque = Mosque()  # object initialization
index = 1  # to manage lines in the listbox
listbox = Listbox()  # this value will be changed in part2


# displays all current records on the listbox in PART2
def display_mosques():
    global listbox
    global index

    # this variable will contain a list of all records in database
    mosques_list = mosque.display()

    for record in mosques_list:
        listbox.insert(index, record)
        index = index + 1


# adds a record to the database using the insert() function from the Mosque class
def add_mosque(id, name, type, coordinates, address, imam_name):
    mosque.insert(id, name, type, address, coordinates, imam_name)


# deletes a record using delete() from the class
def delete_mosque(id):
    mosque.delete(id)


# displays a record on the listbox in PART2 with a given mosque name, using search() from the class
def search_mosque(name):
    global index

    listbox.insert(index, mosque.search(name))
    index = index + 1


# changes the value of the imam name given a correct mosque name, using update() from the class
def update_table(name, imam_name):
    if mosque.search(name) is not None:
        mosque.update(name, imam_name)


# contains the structure and design of the GUI
def main():
    # placing parts as required in the assignment
    part1_frame = LabelFrame(root, text="PART1", width=400, height=125)
    part1_frame.grid(row=0, column=0, sticky='snew', ipadx=5)

    part2_frame = LabelFrame(root, text="PART2", width=400, height=250)
    part2_frame.grid(row=0, column=1, sticky='snew')

    part3_frame = LabelFrame(root, text="PART3", width=250, height=125)
    part3_frame.grid(row=0, column=0, sticky='sw')

    part4_frame = LabelFrame(root, text="PART4", width=150, height=125)
    part4_frame.grid(row=0, column=0, sticky='se')

    # for empty spaces
    space = Label(part1_frame, text="")

    # inside part1 we need two columns, entries to get info

    # first column
    id_label = Label(part1_frame, text="ID")
    id_label.grid(row=0, column=0)

    id_entry = Entry(part1_frame)
    id_entry.grid(row=0, column=1)

    column1space1 = Label(part1_frame, text="")
    column1space1.grid(row=1, column=0)

    type_label = Label(part1_frame, text="Type")
    type_label.grid(row=2, column=0)

    # define option variable for the option menu
    option_var = StringVar()
    option_var.set("Jamea")

    type_option = OptionMenu(part1_frame, option_var, "Jamea", "Masjid")
    type_option.grid(row=2, column=1, ipadx=20)

    column1space2 = Label(part1_frame, text="")
    column1space2.grid(row=3, column=0)

    co_label = Label(part1_frame, text="Coordinates")
    co_label.grid(row=4, column=0)

    co_entry = Entry(part1_frame)
    co_entry.grid(row=4, column=1)

    column1space3 = Label(part1_frame, text="")
    column1space3.grid(row=5, column=0)

    # second column
    name_label = Label(part1_frame, text="Name")
    name_label.grid(row=0, column=2)

    name_entry = Entry(part1_frame)
    name_entry.grid(row=0, column=3)

    space.grid(row=1, column=2)

    address_label = Label(part1_frame, text="Address")
    address_label.grid(row=2, column=2)

    address_entry = Entry(part1_frame)
    address_entry.grid(row=2, column=3)

    space.grid(row=3, column=2)

    imam_label = Label(part1_frame, text="Imam_name")
    imam_label.grid(row=4, column=2, ipadx=5)

    imam_entry = Entry(part1_frame)
    imam_entry.grid(row=4, column=3)

    space.grid(row=5, column=2)

    # part2 is a listbox
    global listbox
    listbox = Listbox(part2_frame, height=15, width=65)
    listbox.grid(row=0, column=0)

    # part3 is 4 buttons for different commands
    space.grid(row=0, column=0, sticky='snw')

    display_all_button = Button(part3_frame, text="Display_All", width=15,
                                command=lambda: display_mosques())
    display_all_button.grid(row=0, column=1, sticky='sn', ipadx=8, ipady=5, padx=3, pady=5)

    search_button = Button(part3_frame, text="Search By Name", width=15,
                           command=lambda: search_mosque(name_entry.get()))
    search_button.grid(row=0, column=2, sticky='sn', ipadx=8, ipady=5, padx=3, pady=5)

    add_button = Button(part3_frame, text="Add Entry", width=15,
                        command=lambda: add_mosque(id_entry.get(), name_entry.get(),
                                                   option_var.get(), co_entry.get(),
                                                   address_entry.get(),
                                                   imam_entry.get()))
    add_button.grid(row=1, column=1, sticky='sn', ipadx=8, ipady=5, padx=3, pady=5)

    delete_button = Button(part3_frame, text="Delete Entry", width=15,
                           command=lambda: delete_mosque(id_entry.get()))
    delete_button.grid(row=1, column=2, sticky='sn', ipadx=8, ipady=5, padx=3, pady=5)

    # part4 is 2 buttons for extra credit
    update_button = Button(part4_frame, text="Update Table", width=15,
                           command=lambda: update_table(name_entry.get(), imam_entry.get()))
    update_button.grid(row=0, column=0, sticky='sn', ipadx=8, ipady=5, padx=5, pady=5)

    display_map_button = Button(part4_frame, text="Display on Map", width=15)
    display_map_button.grid(row=1, column=0, sticky='sn', ipadx=8, ipady=5, padx=5, pady=5)

    # to keep the GUI running
    root.mainloop()


main()
