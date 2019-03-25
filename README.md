# SimpleAutomaton

This python program stimulates a simple automaton that accepts or discards given words. Words need to belong in a specific Language (automaton language) otherwise they will be discarded. Automaton reads the word just once and takes a decision (so, it’s not recursive) 

In order to run the script type in command line:
python3 automata.py filename 

as the above command indicates python 3 needs to be installed in your system.

About variable:
- finals[] → A list that stores automaton’s final states
- num_finals → A variable that stores the number of final states
- ab[] → A list that stores the alphabet
- num_states → a variable that stores the total number of states (final and not final)
- s[] → List that stores the initial state
- current_s → Variable that stores the current state (initially points at s[0] ) 
- trans[] → List that stores the transitions
- num_trans → Variable that stores the number of transitions
- word → String variable that stores the word that user type
- word_list[] → A list that stores the word

text file has to have a specific strict format. Here is an example: 

3 \* Automaton’s total states *\
1 \* Initial state is state number 1 *\
2 \* There are 2 final states *\
2 3 \* States 2 and 3 are final states *\
6 \* There 6 transition in total *\
1 a 2 \* If automaton is in state 1, it can go to state 2 only if it reads “a” etc... *\
1 b 1 \* a,b is automaton’s alphabet and can be anything like numbers or even symbols. *\
2 a 3 \*If automaton is in state 2, it can go to state 3 only if it reads “a”*\
2 b 1 \*If automaton is in state 2, it can go to state 1 only if it reads “b”*\
3 a 3 \*If automaton is in state 3, it can ramain to state 3 only if it reads “a”*\
3 b 1 \*If automaton is in state 3, it can go to state 1 only if it reads “b”*\ 

When you make your own file don’t leave the comments inside \**\.

There are some test files:
- ex2_1b.txt → Accepts the words that start or finish with 01
- ex2_2a.txt → Accepts the words that have at least one a and at least one b
- ex2_3b.txt → Accepts all the words with regular expression a*b
