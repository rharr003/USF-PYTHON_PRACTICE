def single_letter_count(word, letter):
    count = 0
    for item in word:
        if item == letter:
            count +=1
    return count