print ("Icon Project""\n")
print ("Please ensure that you have your icon ready as a single line of 1s and 0s." "\n")
print ("'1s' will be interperted as an 'X' pixel.")
print ("'0s' will be interperted a an 'O' pixel." "\n")
input ("Press ENTER when you are ready to begin." "\n")

complete_icon = []

def user_input(rows):
    counter = 1 
    while counter < rows + 1:
        user_row = str(input (f'Please type in row {counter} of your icon.  Rember to add a space between each character and verify your input before hitting enter: '))
        complete_icon.append(user_row.split())
        counter += 1

def display_normal_pixel(pixel):
    if pixel =="0":
        return "O"
    else:
        return "X"

def display_inverted_pixel(pixel):
    if pixel =="0":
        return "X"
    else:
        return "O"

def print_icon(icon, display_pixel_function ):
    for row in icon:
        for pixel in row:
            print(display_pixel_function(pixel), end="")
        print("\r")

def scaling(icon, multiplier):
    scaling_icon = []
    for row in icon:
        for i in range(multiplier):
            new_row = []
            for cell in row:
                for i in range(multiplier):
                    new_row.append(cell)
            scaling_icon.append(new_row)
    return scaling_icon
            


user_input(10)

user_invert_response = input ("Would you like to see your image inverted?  Please type 'Yes' or 'No'.  ")
user_scaling_response = input ("Would you like scale your image?  Please type 'Yes' or 'No'.  ")

if user_scaling_response == "Yes":
    multiplier = int(input ("Please enter a the number of times you would like to see your image scaled in the form of a whole number.  "))
    complete_icon = scaling(complete_icon, multiplier)

if user_invert_response == "Yes":
    print_icon(complete_icon, display_inverted_pixel)
else: 
    print_icon(complete_icon, display_normal_pixel)