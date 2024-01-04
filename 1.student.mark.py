# empty list 
student_infor  =[]

def input_number_students():
    number = int(input("input number of students : "))
    return number 

# main 
def main (): 
    while True :
        print (" 1 .  input information students ")
        print (" 2 .  input information couses ")
        print (" 3 .  input mark of couses ")
        print (" 0 : break ")
        
        option = int(input("choose :x "))
        if option == 0 :
            print("ok , you break ")
            break 
        
        if option == 1 :
            input_number_students
if __name__ == "__main__":
    main()