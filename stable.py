import prompt
import goody
import copy

#Hsieh Wesley, whsieh2, 3229447

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    file_dict = {}
    for line in open_file.readlines():
        current_line = line.split(';')
        last_entry = current_line[len(current_line)-1].split('\n')
        current_line[len(current_line)-1] = last_entry[0]
        file_dict[current_line[0]] = [None, current_line[1:len(current_line)]]
    return file_dict                                


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    dict_str = str()
    for x in d:
        dict_str += str(x) +  ' -> ' +  str(d[x]) + '\n'
    
    return dict_str

def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    if (order.index(p2) < order.index(p1)):
        return p2
    else: 
        return p1
    
def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    #has men dict return 2-tuples, (man, woman)
    matches = set()
    for man in men:
        matches.add((man, men[man][match]))
    return matches


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    print(trace)
    copy_men = copy.deepcopy(men)
    unmatched = set()
    matches = set() 
    for key in copy_men: 
        if copy_men[key][match] == None: 
            unmatched.add(key)
        
    continue_running = True
    #remove first man from unmatched
    #remove first preference
    #if preference unmatched, match
    #if preference matched, check preference level 
    #if succeeed unmatch girl from guy
    
    if trace == True:  
        print('Women preferences (unchannging)')
        dict_as_str(women, None, False)
    
    while continue_running:        
        if trace == True: 
            print('Men Preferences (current)')
            dict_as_str(copy_men, None, False)
            print('unmatched men = ', unmatched, '\n')
                
        man = unmatched.pop()
            
        woman = copy_men[man][prefs].pop(0)
            
        if women[woman][match] == None:
            if trace == True: 
                print(man, 'proposes to ', woman, ', who is currently unmatched, accepting the proposal', '\n')
            matches.add((man,woman))
            women[woman][match] = man 
            copy_men[man][match] = woman
        else:
            if who_prefer(women[woman][prefs], women[woman][match], man) == man:
                if trace == True: 
                    print(man, 'proposes to ', woman, ', who is currently matched, accepting the proposal, rejectin match with ', women[woman][0], '\n')
                    #unmatch the man and match the woman to the next man 
                matches.remove((women[woman][match], woman))
                matches.add((man, woman))
                unmatched.add(women[woman][match])
                copy_men[women[woman][match]][match] = None
                copy_men[man][match] = woman
                women[woman][match] = man
            else: 
                if trace == True:
                    print(man, 'proposes to ', woman, ', who is currently  matched, rejecting the proposal (likes current match better)', '\n')
                unmatched.add(man)                 
        if len(unmatched) == 0:
            continue_running = False
            
    return matches                    
    
if __name__ == '__main__':
    # Write script here
    while True: 
        men_file = input('Choose a file name representing preferences of the men: ')
        women_file = input('Choose a file name representing preferences of the women: ')
        try: 
            men = open(men_file, 'r')
            women = open(women_file, 'r')
        except:
            print('Invalid file name(s) try again')
        else: 
            break
        
    #read files for matches
    men_pref = read_match_preferences(men)   
    women_pref = read_match_preferences(women)   
    
    print('Men Preferences ')
    print(dict_as_str(men_pref, None, False))
    print('Women Preferences')
    print(dict_as_str(women_pref, None, False))
      
    #print("Men Preferences", '\n', dict_as_str(men_pref, None, False))
    #print("Women Preferences", '\n', dict_as_str(women_pref, None, False))
    trace = input("Choose whether to trace this algorithm[True]: ").capitalize()
    if trace == 'True' or trace == 'true':
        matches = make_match(men_pref, women_pref, True)
    else: 
        matches = make_match(men_pref, women_pref, False)
    print('matches',matches)
      
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
