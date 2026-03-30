import csv
# imports fuctions to use csv files


# dictionary of students
students = {

    1001926355 : {"name": "melissa",
                  "age" : 23,
                  "course" : 1,
                  "active" : True},
    1234568920 : {"name": "diego",
                  "age" : 24,
                  "course" : 2,
                  "active" : True},
    1648212010 : {"name": "eduardo",
                  "age" : 20,
                  "course" : 1,
                  "active" : False},
    1856200494 : {"name": "isabela",
                  "age" : 24,
                  "course" : 2,
                  "active" : True},
                       
                  }

# fuction to add new student
def add_student():

    global students

    validate_student = True

    # loop to validate student's type of data
    while validate_student:

        try:

            id = int(input("Write student ID: ").strip())

            if id not in students:

                name = input("Write name: ").strip().lower()
                course = int(input("Write course (1 or 2): ").strip())

                if course == 1:
                    course == 1

                elif course == 2:
                    course == 2

                else:
                    print("Write a valid course")
                    validate_student =  False

                age = int(input("Write age: ").strip())
                validate_active = int(input("Is the student active? (1. yes 2. no): ").strip())
                active = True

                if validate_active == 1:
                    active == True
                elif validate_active == 2:
                    active == False

                else:
                    print("Write a valid option")
                    validate_student =  False

                # adds new student
                students[id] = {"name": name,
                    "age" : age,
                    "course" : course,
                    "active" : active
                }
                validate_student = False

            else:
                print("This student already exists")
                validate_student = False

        except ValueError:

            print("Invalid input")

    return_menu()

# fuction to show all the students
def read_list():

    global students

    if not students:
        print("The list of students is empty")

    # prints student's information
    else:
        for id,data in students.items():
            print(f"{id} | Name: {data['name']} | Age: {data['age']} | Course: {data['course']} | Active: {data['active']}")

    return_menu()

# fuction to update a student
def update_student():
    global students

    for id,data in students.items():
        print(f"{id} | Name: {data['name']} | Age: {data['age']} | Course: {data['course']} | Active: {data['active']}")


    validate_student = True

    # loop to validate student's type of data
    while validate_student:

        try:

            id = int(input("Write student's id: ").strip())

            if students.get(id):

                name = input("Write name: ").strip().lower()
                course = int(input("Write course (1 or 2): ").strip())

                if course == 1:
                    course == 1

                elif course == 2:
                    course == 2

                else:
                    print("Write a valid course")
                    validate_student =  False

                age = int(input("Write age: ").strip())
                validate_active = int(input("Is the student active? (1. yes 2. no): ").strip())
                active = True

                if validate_active == 1:
                    active == True
                elif validate_active == 2:
                    active == False
                else:
                    print("Insert valid option")
                    validate_student =  False

                students[id] = {"name": name,
                        "age" : age,
                        "course" : course,
                        "active" : active
                }
                print(f"{name} updated")
                validate_student =  False

            else:
                print(f"{id} is not on the students' list.")
                validate_student =  False

        except ValueError:
                print("Insert valid data")

    return_menu()

# fuction to search a student
def search_student():
    
    global students

    try:

        id = int(input("Write student's id: ").strip())

        # search the student
        if students.get(id):

            print(students.get(id))

        else:
            print(f"{id} not in students' list")

    except ValueError:
        print("Insert valid ID")

    return_menu()

# fuction to delete a student
def delete_student():
    global students

    for id,data in students.items():
        print(f"{id} | Name: {data['name']} | Age: {data['age']} | Course: {data['course']} | Active: {data['active']}")

    id = input("Write ID to delete: ").strip()
    try:
        id = int(id)
        # searchs whether the student exists
        if id in students:
            del students[id]
            print(f"{id} deleted")
        else:
            print(f"{id} not in students' list")

    except ValueError:
        print("Insert valid ID")

    return_menu()

# fuction to save as csv file
def save_csv(add_header=True):
    global students

    # fuction to convert the dictionary to csv file
    with open("students.csv","w",encoding='utf-8') as f:
        writer = csv.writer(f)
        # writes headers
        writer.writerow(["ID","Name","Age", "Course","Active"])
        # writes rows
        for id, data in students.items():
            writer.writerow([id,data["name"],
                             data["age"],
                             data["course"],
                             data["active"]])
            
    print("CSV file created")
    return_menu()

# fuction to load csv
def load_csv():
    global students

    try:
        # reads a csv file and converts it to a dictionary
        with open("students.csv","r",encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # matchs the information
                try:
                    id = int(row["ID"].strip())
                    name = row["Name"].strip().lower()
                    age = int(row["Age"])
                    course = int(row["Course"])
                    active = bool(row["Active"])

                    if id in students:
                        print(f"´{id} already in students' list, updating...")

                    students[id] = {
                        "name" : name,
                        "age" : age,
                        "course" : course,
                        "active" : active}

                except ValueError:
                    print(f"Error in row: {row}")

            print("CSV loaded")
                
    except FileNotFoundError:
        print("File not found")

    
    return_menu()
                
# fuction to return to menu
def return_menu():
    back = input("""Do you want to return to main menu?
        1. Yes
        2. Exit

        Select one option: """).strip()

    if back == "1":
        return True
    elif back == "2":
        print("Exit")
        exit(0)  # exits the program 
    else:
        print("Invalid option, try again.")


