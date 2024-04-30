import csv


def read_csv():
    with open("info.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for i in csv_reader:
            print(i)


# This code read the data from csv file

def write_csv(copy_list):
    with open("info.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(copy_list)


# This code write a data to csv file

def add_data():
    with open("info.csv", "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Phill", "Foden"])


# This code add data to csv file

def csv_to_list(file_name):
    copy_list = []
    with open(file_name, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for i in csv_reader:
            copy_list.append(i)
    print(copy_list)
    return copy_list


# This code change data to list


def change_csv(id, name="not provided", surname='not provided', age='not provided'):
    status = False
    copy_list = csv_to_list()
    for i in copy_list:
        if i[0] == id:
            status = True
            if name != "not provided" and surname != "not provided" and age != "not provided":
                i[1] = name
                i[2] = surname
                i[3] = age
            elif name != "not provided":
                i[1] = name
            elif surname != "not provided":
                i[2] = surname
            elif age != "not provided":
                i[3] = age

    write_csv(copy_list)
    return status


# change_csv()


def sort_by_age(choice):
    copy_list = csv_to_list()
    header = copy_list[0]
    data = copy_list[1:]
    if choice == "ASC":
        sorted_data = sorted(data, key=lambda x: int(x[3]))
    elif choice == "DESC":
        sorted_data = sorted(data, key=lambda x: int(x[3]), reverse=True)

    sorted_info = [header] + sorted_data
    result = sorted_info
    return result


# This code sort data by age

while True:
    print("1-Change csv")
    print("2-read scv")
    print("3-Sort by age")
    print("4-Exit")
    menu = input("Enter your choice")

    if menu == "1":
        id = input("Enter user id")
        if change_csv(id):
            print("Id exist")
            print("1-Change everyting")
            print("2-Change name")
            print("3-Change surname")
            print("4-Change age")
            choice = input("Enter your choice")
            if choice == "1":
                new_name = input("Enter new user name")
                new_surname = input("Enter new user surname")
                new_age = input("Enter new user age")
                change_csv(id, new_name, new_surname, new_age)
            elif choice == "2":
                new_name = input("Enter new user name")
                change_csv(id, name=new_name)
            elif choice == "3":
                new_surname = input("Enter new user surname")
                change_csv(id, surname=new_surname)
            elif choice == "4":
                new_age = input("Enter new user age")
                change_csv(id, age=new_age)
        elif id == "stop":
            break
        else:
            print("Id not found")
    elif menu == "2":
        read_csv()
    elif menu == "3":
        print("1-Sort by ASC")
        print("2-Sort by DESC")
        choice = input("Enter your choice")
        if choice == "1":
            for i in sort_by_age('ASC'):
                print(i)
        elif choice == "2":
            for i in sort_by_age('DESC'):
                print(i)
    elif menu == "4":
        exit()
