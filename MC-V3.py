# Define the table headers and data
headers = ["Conversion Type", "Number System", "Digits", "Explanation"]
data = [
    ["1. Denary to Binary (Base 2)", "Denary: 0-9", "0, 1", "Converting Denary to Binary involves dividing the Denary number by 2 repeatedly and recording remainders."],
    ["2. Denary to Octal (Base 8)", "Denary: 0-9", "0, 1, 2, 3, 4, 5, 6, 7", "Converting Denary to Octal involves dividing the Denary number by 8 repeatedly and recording remainders."],
    ["3. Denary to Hexadecimal (Base 16)", "Denary: 0-9", "0-9, A-F", "Converting Denary to Hexadecimal involves dividing the Denary number by 16 repeatedly and recording remainders."],
    ["4. Binary to Denary (Base 10)", "Binary: 0, 1", "0, 1", "Converting Binary to Denary involves multiplying each digit by 2 raised to a power and adding them up."],
    ["5. Octal to Denary (Base 10)", "Octal: 0-7", "0, 1, 2, 3, 4, 5, 6, 7", "Converting Octal to Denary involves multiplying each digit by 8 raised to a power and adding them up."],
    ["6. Hexadecimal to Denary (Base 10)", "Hexadecimal: 0-9, A-F", "0-9, A-F", "Converting Hexadecimal to Denary involves multiplying each digit by 16 raised to a power and adding them up."],
]

# Function to print the table
def print_table(headers, data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for i, header in enumerate(headers):
        print(f"{header.ljust(col_widths[i])}  |", end=" ")
    print()
    print("-" * (sum(col_widths) + len(col_widths) * 4 - 1))
    for row in data:
        for i, item in enumerate(row):
            print(f"{item.ljust(col_widths[i])}  |", end=" ")
        print()

# Function to explain Denary to Binary conversion
def explain_denary_to_binary(denary):
    binary_result = bin(denary)[2:]
    explanation = []
    explanation.append(f"Starting with Denary number: {denary}")
    explanation.append("Step-by-Step Binary Conversion:")
    explanation.append(f"1. Divide {denary} by 2.")
    explanation.append(f"2. Write down the remainder (0 or 1) as the rightmost digit.")
    explanation.append(f"3. Repeat steps 1 and 2 with the quotient until the quotient becomes 0.")
    explanation.append(f"4. Read the binary digits from bottom to top to get the final result: {binary_result}")
    explanation.append(f"Binary Result: {binary_result}")
    return explanation

# Function to explain Denary to Octal conversion
def explain_denary_to_octal(denary):
    octal_result = oct(denary)[2:]
    explanation = []
    explanation.append(f"Starting with Denary number: {denary}")
    explanation.append("Step-by-Step Octal Conversion:")
    explanation.append(f"1. Divide {denary} by 8.")
    explanation.append(f"2. Write down the remainder (0-7) as the rightmost digit.")
    explanation.append(f"3. Repeat steps 1 and 2 with the quotient until the quotient becomes 0.")
    explanation.append(f"4. Read the octal digits from bottom to top to get the final result: {octal_result}")
    explanation.append(f"Octal Result: {octal_result}")
    return explanation

# Function to explain Denary to Hexadecimal conversion
def explain_denary_to_hexadecimal(denary):
    hex_result = hex(denary)[2:].upper()
    explanation = []
    explanation.append(f"Starting with Denary number: {denary}")
    explanation.append("Step-by-Step Hexadecimal Conversion:")
    explanation.append(f"1. Divide {denary} by 16.")
    explanation.append(f"2. Write down the remainder (0-9 or A-F) as the rightmost digit.")
    explanation.append(f"3. Repeat steps 1 and 2 with the quotient until the quotient becomes 0.")
    explanation.append(f"4. Read the hexadecimal digits from bottom to top to get the final result: {hex_result}")
    explanation.append(f"Hexadecimal Result: {hex_result}")
    return explanation

# Function to explain Binary to Denary conversion
def explain_binary_to_denary(binary):
    denary_result = int(binary, 2)
    explanation = []
    explanation.append(f"Starting with Binary number: {binary}")
    explanation.append("Step-by-Step Denary Conversion:")
    explanation.append(f"1. Start with the Binary number: {binary}")
    explanation.append(f"2. Convert it to Denary using the formula.")
    explanation.append(f"Denary Result: {denary_result}")
    return explanation

# Function to explain Octal to Denary conversion
def explain_octal_to_denary(octal):
    denary_result = int(octal, 8)
    explanation = []
    explanation.append(f"Starting with Octal number: {octal}")
    explanation.append("Step-by-Step Denary Conversion:")
    explanation.append(f"1. Start with the Octal number: {octal}")
    explanation.append(f"2. Convert it to Denary using the formula.")
    explanation.append(f"Denary Result: {denary_result}")
    return explanation

# Function to explain Hexadecimal to Denary conversion
def explain_hexadecimal_to_denary(hexadecimal):
    denary_result = int(hexadecimal, 16)
    explanation = []
    explanation.append(f"Starting with Hexadecimal number: {hexadecimal}")
    explanation.append("Step-by-Step Denary Conversion:")
    explanation.append(f"1. Start with the Hexadecimal number: {hexadecimal}")
    explanation.append(f"2. Convert it to Denary using the formula.")
    explanation.append(f"Denary Result: {denary_result}")
    return explanation

# Function to get user's choice
def get_user_choice():
    print("Choose the type of conversion you want to perform:")
    for i, conversion in enumerate(data):
        print(f"{i + 1}. {conversion[0]}")
    choice = int(input("Enter the number corresponding to the conversion type: "))
    return data[choice - 1]

# Function to get user's input number, allowing hexadecimal input
def get_input_number():
    user_input = input("Insert Number for Conversion: ")
    return user_input

# Function to ask if the user wants to convert another value
def ask_to_convert_another():
    choice = input("Do you want to convert another value? (1 for yes, 2 for no): ")
    return choice

# Main program
while True:
    chosen_conversion = get_user_choice()
    conversion_type = chosen_conversion[0]
    number_system = chosen_conversion[1]
    digits = chosen_conversion[2]
    explanation = chosen_conversion[3]

    print(f"Starting with {conversion_type}: {number_system}")
    print(f"Digits: {digits}")
    print()
    print(explanation)

    if "Denary to Binary" in conversion_type:
        denary = int(get_input_number())
        explanation = explain_denary_to_binary(denary)

    elif "Denary to Octal" in conversion_type:
        denary = int(get_input_number())
        explanation = explain_denary_to_octal(denary)

    elif "Denary to Hexadecimal" in conversion_type:
        denary = int(get_input_number())  # Input should be in Denary (base 10)
        explanation = explain_denary_to_hexadecimal(denary)

    elif "Binary to Denary" in conversion_type:
        binary = get_input_number()
        explanation = explain_binary_to_denary(binary)

    elif "Octal to Denary" in conversion_type:
        octal = get_input_number()
        explanation = explain_octal_to_denary(octal)

    elif "Hexadecimal to Denary" in conversion_type:
        hexadecimal = get_input_number()
        explanation = explain_hexadecimal_to_denary(hexadecimal)

    # Display the explanation
    print()
    print(f"Starting with {conversion_type}: {number_system}")
    print(f"Digits: {digits}")
    print()
    for step in explanation:
        print(step)

    another_conversion = ask_to_convert_another()
    if another_conversion != '1':
        print("Thank you for using the conversion tool.")
        break
