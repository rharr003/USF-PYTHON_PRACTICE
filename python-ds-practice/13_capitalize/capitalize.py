def capitalize(phrase):

    return str(phrase.split(' ')[0].title()) + " " + ' '.join(phrase.split(' ')[1:])

print(capitalize('hello john my name'))