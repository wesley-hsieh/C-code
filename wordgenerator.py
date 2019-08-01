import goody
from goody import irange
import prompt
from random import choice
import collections

#Hsieh Wesley, whsieh2, 3229447

# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
    fake = collections.defaultdict(list)
    for line in file.readlines():
        line_s = line.split()
        for i in range(0, len(line_s)-os):
            if line_s[i+os] not in fake[tuple(line_s[i:i+os])]:
                fake[tuple(line_s[i:i+os])].append(line_s[i+os])

    return dict(fake)



def corpus_as_str(corpus : {(str):[str]}) -> str:
    corpus_str = str()
    for key in corpus.keys():
        corpus_str += '  ' + str(key) +  "can be followed by any of: " +  str(corpus[key]) + '\n'
        
    max_key = max(corpus, key = lambda x: len(set(corpus[x])))
    min_key = min(corpus, key = lambda x: len(set(corpus[x])))
    corpus_str += 'max/min list lengths = ' + str(len(corpus[max_key])) +  '/' +  str(len(corpus[min_key])) + '\n'
    
    return corpus_str

def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    lst = [start[i] for i in range(0, len(start))]
    for i in range(0+len(start), int(count)):
        next_word = choice(corpus[tuple(start)])
        lst.append(next_word)
        start.pop(0)
        start.append(next_word)
        
    print("Random text = ", lst)
        
            
if __name__ == '__main__':
    # Write script here
    order = int(input("Choose the order statistic: "))
    while True:
        name = input("Choose the file name to process: ")
        try: 
            file = open(name, 'r')
        except: 
            print("incorrect file name try again")
        else:
            break
        
    corpus = read_corpus(order, file)
   
    print(corpus_as_str(corpus))
    
    print("Choose ", order, " words to start with")
    words = []
    for i in range(0, order):
        prompt = 'Choose word ' + str(i+1) + ': ' 
        words.append(input(prompt))
            
    num_of_words = input('Choose # of words to generate: ')  
    produce_text(corpus, words, num_of_words) 

            
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
