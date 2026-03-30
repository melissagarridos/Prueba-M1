from function import add_student, read_list, update_student, delete_student, save_csv, load_csv, return_menu, search_student
# import functions from the correct file

# main loop that runs the menu with all the functions

def menu():
    
    loop = True

    while loop:

        print("""Select one option:
            
            1. Add student
            2. Read student's list
            3. Update student
            4. Look for a student
            5. Delete student
            6. Save data as CSV
            7. Load CSV
            8. Exit""")
        
        option = input("Please select one option: ").strip()

        try:

            option = int(option)

            match option:

                case 1:
                    add_student()
                case 2:
                    read_list()
                case 3:
                    update_student()
                case 4:
                    search_student()
                case 5:
                    delete_student()
                case 6:
                    save_csv()
                case 7:
                    load_csv()
                case 8:
                    print("Exit")
                    loop = False
                case _:
                    print("Insert a valid option")
                    continue
    
        except ValueError:
            print("Choose a valid option")
# closes the menu fuction



# runs the program
menu()