print("----------COMPLAINT MANAGEMENT SYSTEM----------")

dict = {}

m = True
def raisee ():
    name = input("Enter User Name: ")
    complaint = input("Enter the complaint: ")
    dict[name] = complaint
    print("---Complaint Successfull!!---")
    print()

def view():
    print(dict)

while(m):

    n = int(input("1. Raise a complaint\n2. View Complaints\n3. Exit\n"))

    if(n == 1 ) :
        raisee()
        continue

    elif (n == 2):
        view()
        continue

    elif (n == 3):
        break

    elif (n > 2):
        print("Error!! Enter a valid number: ")


