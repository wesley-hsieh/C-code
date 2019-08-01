import goody
import collections

#Hsieh Wesley, whsieh2, 3229447


def read_fa(file : open) -> {str:{str:str}}:
    fa = collections.defaultdict(list)
    for line in file.readlines():
        split_line = line.strip().split(';')            
        state =split_line.pop(0)
        for i in range(0, int(len(split_line)/2)):
            fa[state].append((split_line[2*i], split_line[2*i+1]))
    return dict(fa)

def fa_as_str(fa : {str:{str:str}}) -> str:
    fa_str = "The Description of the chose Finite Automaton \n"
    for key in fa.keys():
        fa_str += '  ' + str(key) + ' transitions: ' + str(fa[key]) + '\n'
        
    return fa_str

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    to_return = []
    to_return.append(state)
    curr_state = state
    count = 0
    
    for value in inputs: 
        for orders in fa[curr_state]:
            if value == orders[0]:
                to_return.append((value, orders[1]))
                curr_state = orders[1]
                count = 0
                break
            else:
                #print(value, orders, count)
                if count == len(fa[curr_state])-1:
                    to_return.append((value, None))
                    count = 0
                    break
                else: 
                    count += 1
            
    return to_return    

def interpret(fa_result : [None]) -> str:
    result_str = ''
    result_str += "Begin tracing the next FA simulation \n Start state = " + str(fa_result[0]) + '\n'
    fa_result.pop(0)

    for x in fa_result: 
        if x[1] == None: 
            result_str += "  Input = " + str(x[0]) + '; illegal input: simulation terminated \n'
        else: 
            result_str += "  Input = " + str(x[0]) + '; new state = ' + str(x[1]) + '\n'
        
    result_str += "Stop state = " + str(fa_result[len(fa_result)-1][1]) + '\n'

    return result_str

if __name__ == '__main__':
    # Write script here
    while True:
        name = input('Choose the file name representing the finite automaton:')
        try: 
            file = open(name, 'r')
        except:
            print('Incorrect file name, try again: ')
        else: 
            break                
    
    finite = read_fa(file)
    print(fa_as_str(finite))
    
    while True: 
        parity = input('Choose the file name representing start-states and their inputs:  ')
        try: 
            file2 = open(parity, 'r')
        except: 
            print('Incorrect file name, try again:')
        else: 
            break

    to_interpret = []
    for line in file2.readlines():
        split_line = line.strip().split(';')
        
        to_interpret.append(process(finite, split_line[0], split_line[1:len(split_line)]))
        print(interpret(process(finite, split_line[0], split_line[1:len(split_line)])))
    
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
