"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    f = open(filename)
    words = f.read().split()
    frequencies = {}

    for i in range(len(words)):
        if (words[i] not in frequencies):
            frequencies[words[i]] = 1
        else: 
            frequencies[words[i]] += 1        

    occurrences = frequencies.values()

    max = 0
    for j in range(len(occurrences)):
        if (occurrences[j] > max): max = occurrences[j]

    words_list = []    

    while (max > 0):
        for key in frequencies:
            if (frequencies[key] == max): words_list.append(key)
        max -= 1

    f.close()

    return words_list      

    pass

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    f = open(filename)
    words = f.read().split()
    frequencies = {}

    for i in range(len(words)):
        if (len(words[i]) >= min_chars):
            if (words[i] not in frequencies):
                frequencies[words[i]] = 1
            else: 
                frequencies[words[i]] += 1        

    occurrences = frequencies.values()

    max = 0
    for j in range(len(occurrences)):
        if (occurrences[j] > max): max = occurrences[j]

    words_list = []    

    while (max > 0):
        for key in frequencies:
            if (frequencies[key] == max): words_list.append(key)
        max -= 1

    f.close()    

    return words_list      
  
    pass

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    f = open(filename)
    words = f.read().split()
    frequencies = {}

    for i in range(len(words)):
        if (len(words[i]) >= min_chars):
            if (words[i] not in frequencies):
                frequencies[words[i]] = 1
            else: 
                frequencies[words[i]] += 1        

    occurrences = frequencies.values()

    max = 0
    for j in range(len(occurrences)):
        if (occurrences[j] > max): max = occurrences[j]

    words_list = []    

    while (max > 0):
        for key in frequencies:
            if (frequencies[key] == max): words_list.append((key,max))
        max -= 1

    f.close()    

    return words_list    

    pass

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        f = open(filename)
        words = f.read().split()
        frequencies = {}

        for i in range(len(words)):
            if (len(words[i]) >= min_chars):
                if (words[i] not in frequencies):
                    frequencies[words[i]] = 1
                else: 
                    frequencies[words[i]] += 1        

        occurrences = frequencies.values()

        max = 0
        for j in range(len(occurrences)):
            if (occurrences[j] > max): max = occurrences[j]

        words_list = []    

        while (max > 0):
            for key in frequencies:
                if (frequencies[key] == max): words_list.append((key,max))
            max -= 1

        return words_list

        f.close()    
    except IOError:
        print 'File missing!'
    finally:
        print 'All done!'
    pass