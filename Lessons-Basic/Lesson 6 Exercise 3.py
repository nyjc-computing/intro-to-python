# Do not modify this program!
# A copy of this code is saved in Lesson 6 Exercise 3.py in case
# you accidentally overwrite the code below
import os

items = ['Load student details from file',
         'See student details',
         'Add student',
         'Save student details to file',
         'Quit the program'
        ]
quit = False
studentdata = []

while not quit:
    print_menu(items)
    option = input('Choose an option: ')
    if option == '1':
        ## Add your code from Task 2 below to get a valid filename from the user 
        ## BEGIN SOLUTION
        valid = False
        while not valid:
            filename = input('Enter filename to load: ')
            if os.path.isfile(filename):
                valid = True
            else:
                print('Invalid filename.')
        studentdata = load(filename)
        ## END SOLUTION
    elif option == '2':
        for i in range(len(studentdata)):
            print(f'{studentdata[i][0]}: {studentdata[i][1]}')
    elif option == '3':
        student = input('Enter student name: ')
        class_ = input('Enter student class: ')
        studentdata.append([name,class_])
    elif option == '4':
        filename = input('Enter filename to save student data to: ')
        if os.path.isfile(filename):
            overwrite = input('File already exists. Overwrite? (Y/N): ')
            if overwrite.lower() == 'Y':
                mode = 'w'
            else:
                mode = 'a'
        else:
            mode = 'w'
        count = save(filename,mode,studentdata) # this function does not exist yet!
        print(f'{count} records saved.')
    elif option == '5':
        quit = True
    else:
        print('Invalid option.')