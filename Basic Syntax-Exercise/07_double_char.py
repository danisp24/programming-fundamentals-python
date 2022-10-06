input_string = input()

while input_string != "End":
    output = ""
    if input_string == "SoftUni":
        input_string = input()
        continue

    for i in input_string:

        output = output + i * 2
    print(output)
    input_string = input()