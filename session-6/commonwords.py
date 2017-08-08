import re
from operator import itemgetter, attrgetter, methodcaller

IGNORE = [
    'a', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'can', 'do', 'for', 'from',
    'have', 'in', 'is', 'it', 'just', 'more', 'not', 'of', 'on', 'or', 'our',
    'over', 'so', 'than', 'that', 'the', 'their', 'these', 'they', 'this', 'those',
    'to', 'up', 'we', 'with'
]

def get_word_occurence(file_path):
    occurrence = {}
    with open(file_path, 'rU') as speechFile:
        lines = speechFile.readlines()
        for line in lines:
            words = re.findall(r'[^\s!$,-.?":;0-9]+', line)
            lowercaseWords = []
            for word in words:
                lowercaseWords.append(word.lower())
            for word in lowercaseWords:
                if word not in IGNORE:
                    if word in occurrence:
                        occurrence[word] += 1
                    else:
                        occurrence[word] = 1
    return occurrence


def common_words(file_path):
    # Return the list of words that occur more than 10 times in alphabetical order.
    word_count = get_word_occurence(file_path)
    # print(sorted(list(word_count.items())))
    filtered_count = {k: v for k, v in word_count.items() if v > 10}
    words = list(filtered_count.keys())
    return sorted(words)



def most_used_words(file_path):
    # Return the list of the 20 most frequently used words in ascending order (from least commone to most common).
    # If two words have the same frequency, order them in alphabetical order.
    word_count = get_word_occurence(file_path)
    # print(max(word_count.items(), key=itemgetter(1)))
    sorted_list = sorted(word_count.items(), key=lambda x: (x[1], x[0]))
    return sorted_list[-20:]

# print(common_words('./2016_budget_speech.txt'))
# output   ["australia","australian","australians","billion","budget","businesses","cent","contributions","economic","economy","four","government","growth","including","income","job","jobs","measures","million","new","people","per","plan","rate","superannuation","support","tax","time","tonight","will","year","years","young"]
# expected ["australian","australians","billion","budget","businesses","cent","contributions","economic","economy","four","government","growth","including","income","job","jobs","measures","million","new","people","per","plan","rate","superannuation","support","tax","will","year","young"]

print(most_used_words('./2016_budget_speech.txt'))
# output ["government","people","billion","year","income","economy","economic","growth","superannuation","australians","budget","million","cent","businesses","per","plan","new","jobs","tax","will"]
# expect ["four","economy","income","rate","young","billion","people","australians","budget","economic","million","superannuation","businesses","cent","plan","per","new","jobs","tax","will"]