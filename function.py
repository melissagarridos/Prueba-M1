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

def add_student():

    global students

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

            age = int(input("Write age: ").strip())
            validate_active = int(input("Is the student active? (1. yes 2. no): ").strip())
            active = True

            if validate_active == 1:
                active == True
            elif validate_active == 2:
                active == False

            else:
                print("Write a valid option")

            students[id] = {"name": name,
                  "age" : age,
                  "course" : course,
                  "active" : active
            }
    
        else:
            print("This student already exists")

    except ValueError:

        print("Invalid input")

    return_menu()



def read_list():

    global students

    if not students:
        print("The list of students is empty")

    else:
        for id,data in students.items():
            print(f"{id} | Name: {data['name']} | Age: {data['age']} | Course: {data['course']} | Active: {data['active']}")

    return_menu()

def update_student():
    global students

    print(students)

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

            age = int(input("Write age: ").strip())
            validate_active = int(input("Is the student active? (1. yes 2. no): ").strip())
            active = True

            if validate_active == 1:
                active == True
            elif validate_active == 2:
                active == False

            students[id] = {"name": name,
                  "age" : age,
                  "course" : course,
                  "active" : active
            }
            print(f"{name} updated")

        else:
            print(f"{id} is not on the students' list.")

    except ValueError:
            print("Insert valid data")

    return_menu()

def search_student():
    
    global students

    try:

        id = int(input("Write student's id: ").strip())

        if students.get(id):

            print(students.get(id))

        else:
            print(f"{id} not in students' list")

    except ValueError:
        print("Insert valid ID")

    return_menu()

def delete_student():
    global students

    print(students)

    id = input("Write ID to delete: ").strip()
    try:
        id = int(id)

        if id in students:
            del students[id]
            print(f"{id} deleted")
        else:
            print(f"{id} not in students' list")

    except ValueError:
        print("Insert valid ID")

    return_menu()

def save_csv():
    pass

def load_csv():
    pass

def return_menu():
    back = input("""Do you want to return to main menu?
        1. Yes
        2. Exit

        Select one option: """).strip()

    if back == "1":
        return True
    elif back == "2":
        print("Exit")
        exit(0)  
    else:
        print("Invalid option, try again.")


