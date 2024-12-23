# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20223004/w1953222
# Date: 13/12/2022

#Part 4 – Dictionary (separate program) 
user_input = input("Are you a student? y/n ")

#student version  
progress = 0
trailing = 0
retriever = 0
exclude = 0 
#defining a dictionary to store inputs which are marks
dictionary = {"Progress": [],
            "Progress (module trailer)": [],  
            "Module retriever": [], 
            "Exclude": []}  

id_list = [] #defining a list to store student ids
loop_continue = "y"

if user_input == "y": #to run student version
    while loop_continue: 
        student_id = input("Enter your student id: ")
        if student_id not in id_list:
            id_list.append(student_id) 
        else: 
            print("Enter a unique student id") 
            break        
        try: 
            pass_credit = int(input("\nPlease enter your credits at pass: "))
            if pass_credit not in range(0, 121, 20):
                print("Out of range")  
            else: 
                defer_credit = int(input("Please enter your credit at defer: "))
                if defer_credit not in range(0, 121, 20):
                    print("Out of range")
                else: 
                    fail_credit = int(input("Please enter your credit at fail: "))
                    if fail_credit not in range(0, 121, 20):
                        print("Out of range")
                    else:
                        marks = (student_id, pass_credit, defer_credit, fail_credit)
                        total = pass_credit + defer_credit + fail_credit
                        if(total) != 120:
                            print("Total incorrect") #total of 3 input marks must be 120
                        elif(pass_credit == 120):
                            print("Progress")
                            progress += 1
                            dictionary["Progress"].append(marks)
                        elif(pass_credit == 100):
                            print("Progress (module trailer)")
                            trailing += 1
                            dictionary["Progress (module trailer)"].append(marks)
                        elif(fail_credit >= 80):
                            print("Exclude")
                            exclude += 1
                            dictionary["Exclude"].append(marks)
                        else:
                            print("Do not progress - module retriever")
                            retriever += 1
                            dictionary["Module retriever"].append(marks)
        except ValueError:
            print("Integer required")
            print('')
        except NameError:
            print('') 
        print()
        print("Would you like to enter another set of data? ")
        loop_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
        if loop_continue == "q":
            break 
            
            
if loop_continue == "q": 
    print()
    print("-" * 60)    
    print("Histogram")
    print("Progress ", progress, ":", "*" * progress)
    print("Trailer  ", trailing, ":", "*" * trailing)
    print("Retriever", retriever, ":", "*" * retriever)
    print("Excluded ", exclude, ":", "*" * exclude)
    print()
    count = progress + trailing + retriever + exclude 
    print(count, " outcomes in total.")
    print("-" * 60)
    print()
    
    #Part 4 – Dictionary (separate program) 
    print("Part 4 - Dictionary (separate program) ")
    for (key, value) in dictionary.items():
        for i in value:
            print(f"{i[0]}:{key} - {i[1]}, {i[2]}, {i[3]}")
        

