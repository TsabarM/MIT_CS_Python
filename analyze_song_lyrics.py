# Analyze song lyrics  - example for use python dictionaries
'''
In this example you can see how to create a frequency dictionary mapping str:int.
Find a word that occures the most and how many times.
Find the words that occur at least X times. 
'''

def lyrics_frequencies(lyrics):
    '''
    Creates a Dictionary with the lyrics words and the frequency of each word.
    
    Arguments:  
        lyrics - text. 
    '''
    myDict = {}
    for word in str(lyrics).split():
        if word in myDict:
            myDict[word] +=1
        else:
            myDict[word] = 1
    return myDict

# Find the most common word - return a tuple (word, frequency).
# In case that there is more than one word returns a list. 
def most_common_word(freqs):
    '''
    Find the most common word - return a tuple (word, frequency).
    In case that there is more than one word returns a list. 
    
    Arguments:
        freqs - a dictionary with words and frequncy of each word in the text. 
    '''
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs, minTimes):
    '''
    Find the words that occur at least X times.
    Each itereation deletes the most frequent words as long as the most frequent words 
    frequency is greater than the minTimes of occurences that the user gives. 

    Arguments:
        freqs - a dictionary with words and frequncy of each word in the text. 
        minTimes - {int} - set by the user. The minimum number of occurences for each word.
    '''
    result = []
    done = False
    while done == False:
        temp = most_common_word(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

if __name__ == "__main__":
    with open(r'Muse_Invincible.txt', 'r') as f:
        Invincible = f.read()
    Invincible = lyrics_frequencies(Invincible)
    print(words_often(Invincible, 4))
