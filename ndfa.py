import goody
import collections

#Hsieh Wesley, whsieh2, 3229447

def read_ndfa(file : open) -> {str:{str:{str}}}:
    ndfa = collections.defaultdict(list)
    for line in file.readlines():
        split_line = line.strip().split(';')            
        state =split_line.pop(0)
        if len(split_line) == 0:
            ndfa[state] = None
        for i in range(0, int(len(split_line)/2)):
            ndfa[state].append((split_line[2*i], split_line[2*i+1]))
    return dict(ndfa)


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    ndfa_str = 'The Description of the chosen Non-Deterministic Finite Automaton \n'
    for key in sorted(ndfa.keys()):
        if ndfa[key] != None:
            ndfa_str += '  ' + str(key) + ' transitions: ' + str(ndfa[key]) + '\n'
        else: 
            ndfa_str += '  ' + str(key) + ' transitions: [] \n'
            
    return ndfa_str

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    to_return = []
    to_return.append(state)
    curr_state = set()
    curr_state.add(state)
    #print('initial state', curr_state)
    count = 0
    state_count = 0
    
    for value in inputs:
        #print(value, curr_state)
        possible_state = set()
        for state in curr_state:
            if state not in ndfa.keys():
                return to_return
            elif ndfa[state] == None: 
                return to_return
            for order in ndfa[state]:
                #print('ndfa state', ndfa[state])
                if value == order[0]:
                    possible_state.add(order[1])
                    state_count += 1
                else:
                    if count == len(ndfa[state])-1 and state_count == len(curr_state)-1:
                        to_return.append((value, None))
                        break
                    else:
                        count += 1
                        state_count += 1        
        curr_state = set()        
        if len(possible_state) != 0:      
            for state in possible_state:
                if state in ndfa.keys(): 
                    curr_state.add(state)
        else: 
            to_return.append((value, None))
            print(to_return)
            return to_return
        #curr_state = list(possible_state)
        #print(curr_state)
        to_return.append((value, possible_state))
        state_count = 0
                
    return to_return         
        


def interpret(result : [None]) -> str:
    interpret_str = 'Start state = '
    interpret_str += result[0] + '\n'
    result.pop(0)
    
    for x in result: 
        if x[1] == None: 
            interpret_str += '  Input = ' + str(x[0]) + '; illegal input: simulation terminated \n'
        else:
            interpret_str += '  Input = ' + str(x[0]) + '; new possible states = ' + str(sorted(list(x[1]))) + '\n'
        
    if result[len(result)-1][1] == None: 
        interpret_str += 'Stop state(s) = None \n'
    else:
        interpret_str += 'Stop state(s) = ' + str(sorted(list(result[len(result)-1][1]))) + '\n'
    
    return interpret_str

if __name__ == '__main__':
    # Write script here
    while True:
        name = input('Choose the file name representing the non-deterministic finite automaton:')
        try: 
            file = open(name, 'r')
        except:
            print('Incorrect file name, try again: ')
        else: 
            break                
    
    ndfa = read_ndfa(file)
    print(ndfa_as_str(ndfa))
    
    while True: 
        parity = input('Choose the file name representing start-states and their inputs:  ')
        try: 
            file2 = open(parity, 'r')
        except: 
            print('Incorrect file name, try again:')
        else: 
            break   
        
    for line in file2.readlines():
        split_line = line.strip().split(';')
        #print(split_line)
        #print('after process', process(ndfa, split_line[0], split_line[1:len(split_line)]))   
        print('Being tracing the next NDFA simulation')
        print(interpret(process(ndfa, split_line[0], split_line[1:len(split_line)])))
    
    '''to_interpret = []
    for line in file2.readlines():
        split_line = line.strip().split(';')
        
        to_interpret.append()'''
           
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
