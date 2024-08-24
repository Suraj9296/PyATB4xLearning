# Match statement

#match the op and execute

#syntax

#match variable:
#    case pattern1:
#        #code block
#    case pattern2:
#        #code block

#write a program to ask the use which browser he wants to run automation

browser_name = input("Enter the browser name \n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("execute the firefox code")
    case "chrome":
        print("execute the chrome code")
    case _:
        print("Browser not found")
