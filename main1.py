class Employee:

    def __init__(self):
        print("Employpee created")

    def __del__(self):
        print("detrcor calles")

def create_obj():
    print("Making object...")
    obj = Employee()
    print("function and...")
    return obj

print("calling create_obj()function end...")
obj = create_obj()
print("program End...")