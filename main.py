#FSA Simulator

inp = open('input.txt', 'r')
output = open('output.txt', 'w')
output.write("Alexey Tolkachev\n")

# Reading the 1st line - number of cases
test_counter = int(inp.readline().replace("\n", ""))
for test_number in range(test_counter):
    automata_settings = []
    transitions = {}
    # For each case we read exactly 5 line, in which describe the automaton configuration
    for i in range(5):
        automata_settings.append(inp.readline().replace("\n", ""))

    # Parsing each line and saving it in corresponding data structure
    states = automata_settings[0].replace("{", "").replace("}", "").split(",")
    alphabet = automata_settings[1].replace("{", "").replace("}", "").split(",")
    initial_state = automata_settings[2]
    final_states = automata_settings[3].replace("{", "").replace("}", "").split(",")
    transitions_temp = automata_settings[4].replace("{", "").replace("}", "").split(",")

    # Additional parsing transitions, splitting each one by "arrow" and saving it in dictionary
    for trans in transitions_temp:
        key_value_split = trans.split("->")
        transitions[key_value_split[0]] = key_value_split[1]

    # Next part is to read the string counter and read the same count of string and save it into list
    strings = []
    string_counter = int(inp.readline().replace("\n", ""))
    for i in range(string_counter):
        strings.append(inp.readline().replace("\n", ""))

    # This method parsing each string through the automaton and give us the result of passing with corresponding path
    def pathing_automaton(string):

        # Each pass begins from the initial state
        path = initial_state
        current_state = initial_state

        # If string is empty - we don't need to check anything in transitions dictionary
        if string != "" and string != "\n":
            c = 0

            # This is the wrapper to build the valid left part of transition expression
            # which contained in dictionary as a key
            key = current_state + "(" + string[c] + ")"

            # While the string has any symbols and last transition is valid we could
            # move to the next symbol
            while c < (len(string)) and transitions.get(key) is not None:
                    current_state = transitions.get(key)
                    if current_state is not None:
                        path = path + "->" + current_state
                        if c == len(string) - 1:
                            break
                        c = c + 1
                        key = current_state + "(" + string[c] + ")"
                    else :
                        break

        # This part is checking is the last saved state final
        for st in final_states:
            if current_state == st:
                result = "True," + path
            else:
                result = "False," + path
        return result+"\n"

    # Writing each case number
    output.write(str(test_number+1)+"\n")
    for s in strings:
        output.write(pathing_automaton(s))

output.close()
