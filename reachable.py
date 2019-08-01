import goody
import prompt
from collections import defaultdict

#Submitter: whsieh2(Hsieh, Wesley) 32294447

def read_graph(file : open) -> {str:{str}}:
    file_dict = {}
    for line in file.readlines(): 
        if line[0] in file_dict.keys():
            file_dict[line[0]] += ',' + line[2]
        else:
            file_dict[line[0]] = line[2]
    return file_dict

def graph_as_str(graph : {str:{str}}) -> str:
    print("Graph: any node -> [all that node's destination nodes]")
    for keys in sorted(graph_dict):
        print('  ', keys, '->', graph_dict[keys].split(','))

def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    #create reached nodes
    reached_set = []
    
    #created list of nodes to go to 
    exploring_list = [start_node]
    
    #while exploring_list.len() > 0, remove first one (use .pop()) and put in reached set 
    #for all nodes related to that node that aren't in reached, put in exploring
    
    #list comprehension example
    #x = [i**2 for i in irange(1,10) if i%2 ==0]
    continue_running = True
    while continue_running: 
        if trace == True: 
            print('reached set = ', reached_set , '\n', 'exploring list = ', exploring_list)
        if exploring_list[0] not in reached_set:
            if trace == True: 
                print("removing node from exploring list and adding it to reached list: node = ", exploring_list[0])
            reached_set.append(exploring_list.pop(0))
            length = len(reached_set)-1
            if reached_set[length] in graph.keys():
                for i in graph[reached_set[length]].split(','):
                    exploring_list.append(i)    
                if trace == True:
                    print("after adding all nodes reachable directly from ", reached_set[length], 
                          " but not already in reached, exploring = ", exploring_list, '\n')
            else: 
                print("after adding all nodes reachable directly from ", reached_set[length], 
                          " but not already in reached, exploring = ", exploring_list, '\n')
        else: 
            if trace == True:
                print("removing node from exploring list and adding it to reached list: node = ", exploring_list[0])
                print("after adding all nodes reachable directly from, ", exploring_list.pop(),
                      " but not already in reached, exploring = ", exploring_list, '\n')
                
        if len(exploring_list) == 0:
            continue_running = False
    
    print("From ", start_node, " the reachable nodes are", reached_set)
if __name__ == '__main__':
    # Write script here
    while True:
        file_name = input("Choose the file name representing the graph: ")     
        try:
            file = open(file_name, 'r') 
        except:  
            print("Invalid file name try again")
        else:
            break
    
    #read file return dictionary 
    graph_dict = read_graph(file)
    
    #print dictionary in format
    graph_as_str(graph_dict)
    
    #establish loop to do reachable until "quit"
    continue_bool = True
    while continue_bool:
        start_node = input("Choose the start node (or choose quit)")
        print(start_node)
        if start_node in graph_dict.keys():
            trace_bool = input("Choose whether to trace the algorithm[True]: ").capitalize()
            if (trace_bool == 'True' or trace_bool == 'true'):
                reachable(graph_dict, start_node, True)
            elif (trace_bool == 'False' or trace_bool == 'false'):
                reachable(graph_dict, start_node, False)
            else: 
                print("invalid input, try again")
        elif start_node == 'quit': 
            continue_bool = False
        else: 
            print("Entry error: ", start_node, '; Illegal: not a source node')
            print("Please enter a legal String")
        
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
