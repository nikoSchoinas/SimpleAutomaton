import sys

if len(sys.argv) != 2:
    print("Use:", sys.argv[0], "<input file>")
    sys.exit(1)
# file's name
input_file = sys.argv[1]

# input_file = "ex2_3b.txt"

# finals is a list that stores all the final states of the automaton
finals = []

# ab list includes the alphabet of the automaton
ab = []

# trans is a list that stores all the possible transitions from one state to another
trans = []
with open(input_file) as f:

    # temp is a help variable that reads from file and then is converted to the appropriate data type.
    temp = f.readline().split()

    # number of states
    num_states = int(temp[0])

    # starting state
    s = f.readline().split()

    # current_s is the current state of the automaton
    current_s = s[0]
    # temp = f.readline().split()
    # s = int(temp[0])

    # number of final states
    temp = f.readline().split()
    num_final = int(temp[0])

    # insert elements in finals list
    temp = f.readline().split()
    for i in range(num_final):
        finals.append((temp[i]))

    # number of transitions
    temp = f.readline().split()
    num_trans = int(temp[0])

    # insert all possible transitions to trans list
    for j in range(num_trans):
        temp = f.readline().split()
        trans.append(temp)
        if temp[1] not in ab:
            ab.append(temp[1])

    f.close()

    # a boolean variable that handles user's preference to continue or not.
    want_continue = True
    while want_continue:
        word = input("\nAlphabet is: " + str(ab) + " Give a word to check if it belongs to automaton's language: ")

        # word variable is a String so it needs to be converted to a list of characters (word_list)
        word_list = list(word)

        for k in range (len(word_list)):
            # check if character belongs to alphabet
            if word_list[k] not in ab:
                print("Character " + word_list[k] + " not in alphabet")
                exit(1)
            else:
                for l in range(num_trans):  # check trans list for the right transition.
                    if current_s == trans[l][0] and word_list[k] == trans[l][1]:
                        current_s = trans[l][2]
                        break
        if current_s in finals:
            print("word: " + word + " belongs to automaton's language!\n")
        else:
            print("word: " + word + " DOES NOT belong to automaton's language!\n")

        temp = input("Want to continue? [y/n] ")

        # exit condition
        if temp != 'y':
            want_continue = False
        else:
            k = 0
            l = 0
            current_s = s[0]

    exit(0)

