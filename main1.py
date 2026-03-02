# attendance tracking system

# # dictionary to store attendance
# attendance = {}

# def show_menu():
#     print("Attendance Tracker")
#     print("1. Add Attendance")
#     print("2. View Attendance")
#     print("3. Exit")
# def Add_Attendance():
#     name = input("enter student name: ")
#     status = input("enter status (present/absent): ")
#     attendance[name] = status
#     print("attendance added successfully")
# def View_Attendance():
#     if not attendance:
#         print("No records found")
#     else:
#         print("---------attendance records----------")
#         for name, status in attendance.items():
#             print(f"{name} - {status}")
# def main():
#     while True:
#         show_menu()
#         choice = input("enter your choice:")
#         if choice == 1:
#             Add_Attendance()
#         elif choice == 2:
#             View_Attendance()
#         elif choice == 3:
#             print("exiting prigram")
#             break
#         else:
#             print("invalid choice")
# main()
        






 # dictionary to store attendance
attendance = {}

def show_menu():
    print("attendance tracker")
    print("1. Add Attendance")
    print("2. View Attendance")
    print("3. Exit")
def Add_Attendance():
    name = input("enter student name: ")
    status = input("enter status (present/absent): ")
    attendance[name] = status
    print("attendance added successfully")
def View_Attendance():
    if not attendance:
        print("No records found")
    else:
        print("---------attendance records----------")
        for name, status in attendance.items():
            print(f"{name} - {status}")
def main():
    while True:
        show_menu()
        choice = input("enter your choice:")
        if choice == "1":
            Add_Attendance()
        elif choice == "2":
            View_Attendance()
        elif choice == "3":
            print("exiting prigram")
            break
        else:
            print("invalid choice")
        
main()