# tuple = ("COP 2510", "EGN 3000L", "MAC 2281", "MUH 3016", "PHY 2048")
# tuplecoursename=('Programming Consepts', 'Foundation')

# z= dict(zip(tuple, tuplecoursename)) #to concatenate tuple and tuplecoursename as dictionary
# print (z)
# coursename = {
#     "COP 2510": "Programming Concepts",
#     "EGN 3000L": "Foundations of Engineering Lab",
#     "MAC 2281": "Calculus I",
#     "MUH 3016": "Survey of Jazz",
#     "PHY 2048": "General Physics I"
# }
# instructor = {
#     "COP 2510": "Z. Beasley",
#     "EGN 3000L": "J. Anderson",
#     "MAC 2281": "A. Makaryus",
#     "MUH 3016": "A. Wilkins",
#     "PHY 2048": "G. Pradhan"
# }
# classtimes = {
#     "COP 2510": "MW 12:30pm – 1:45pm",
#     "EGN 3000L": "TR 11:00am – 12:15pm",
#     "MAC 2281": "MW 9:30am – 10:45am",
#     "MUH 3016": "online asynchronous",
#     "PHY 2048": "TR 5:00pm – 6:15pm"
# }

# coursenumber= input('Enter course number: ')

# if coursenumber in tuple:
#     print('The course details are: ')
#     print('\tCourse Name:', coursename[coursenumber])
#     print('\tInstructor:', instructor[coursenumber])
#     print('\tClass Times:', classtimes[coursenumber])
# else:
#     print(f'{coursenumber} is an invalid course number')

dayoftheweek= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
data= []

days_input= input('Enter which day of the week you want to select: ')

for day in dayoftheweek:
    while True:
        if days_input.capitalize() in dayoftheweek:
                sales_input= int(input(f'Enter the sales for {days_input}: '))
                if sales_input>0:
                    data.append(sales_input)
                    break
                else: 
                    sales_input= input(f'Input was invalid. Re-enter the sales for {days_input}:')
        else: 
            print('Invalid day of the week')

data_sum= sum(data)
data_min=min(data)
data_max= max(data)

print(f'The total sales is ${data_sum}.00\nThe minimum sale amount was: ${data_min}.00\nThe maximum sale amount was: ${data_max}.00')

    

