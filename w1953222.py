# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20223004/w1953222
# Date: 13/12/2022

#Part 1 - Main Version 
user_input = input("Are you a student? y/n ")
#staff version  
progress = 0 
trailing = 0  
retriever = 0 
exclude = 0
final_marks_output = [] #defining a list to store inputs which are marks

if user_input == "n": #to run staff version
    while (user_input == "n"):
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
                            total = pass_credit + defer_credit + fail_credit
                            if(total) != 120:
                                print("Total incorrect") #total of 3 input marks must be 120
                            elif(pass_credit == 120):
                                print("Progress")
                                progress += 1
                                final_marks_output.append(["Progress",  pass_credit, defer_credit, fail_credit])
                            elif(pass_credit == 100):
                                print("Progress (module trailer)")
                                trailing += 1
                                final_marks_output.append(["Progress (module trailer)", pass_credit, defer_credit, fail_credit])
                            elif(fail_credit >= 80):
                                print("Exclude")
                                exclude += 1
                                final_marks_output.append(["Exclude", pass_credit, defer_credit, fail_credit])
                            else:
                                print("Do not progress - module retriever")
                                retriever += 1
                                final_marks_output.append(["Module retriever", pass_credit, defer_credit, fail_credit])
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
        
        
        #Part 2 – List (extension) 
        print("#Part 2 - List (extension) ")
        for data in final_marks_output:
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")
        print("-" * 60)   
        
        #Part 3 - Text File (extension)
        print("#Part 3 - Text File (extension)")
        file = open("student marks.txt", "w") #open for writing, if it already exists its content will be deleted 
        for data in final_marks_output:
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")
        file.write(str(final_marks_output))
        file.close()
        
        print("-" * 60) 
        file = open("student marks.txt", "r") #open for reading
        print(file.read())
        file.close() 

        
#to run student version 
else: 
    #User-Defined Functions
    def out_of_range(credits):
        if credits not in range(0, 121, 20):
            print("Out of range")
            return True 
        
    #Student interface 
    '''
        here if we get only check_range as a variable, the try block won't execute because the varible stays false forever.
        so, we get another has _error variable so the try block will execute with an OR gate when one of the varibles fulfill the condition.
        if both varibles do not fulfill the condition, program will keep asking user to enter a credit value which is inside the above given range.
    '''
    try:
        check_range = False 
        has_error = False
        while has_error == False or check_range == True:
            pass_credit = int(input("Please enter your credits at pass: "))
            has_error = True
            check_range = out_of_range(pass_credit)
            
        check_range = False
        has_error = False
        while has_error == False or check_range == True:
            defer_credit = int(input("Please enter your credits at defer: "))
            has_error = True
            check_range = out_of_range(defer_credit)
            
        check_range = False
        has_error = False
        while has_error == False or check_range == True:
            fail_credit = int(input("Please enter your credits at fail: "))
            has_error = True
            check_range = out_of_range(fail_credit)
            
        total = pass_credit + defer_credit + fail_credit
        if(total) != 120:
            print("Total incorrect") #total of 3 input marks must be 120
        elif(pass_credit == 120):
            print("Progress")
        elif(pass_credit == 100):
            print("Progress (module trailer)")
        elif(fail_credit >= 80):
            print("Exclude") 
        else:
            print("Do not progress - module retriever")
    except ValueError:
        print("Integer required")
        print('')
    except NameError:
        print('')

    
#Part 4 – Dictionary (separate program) 

 

