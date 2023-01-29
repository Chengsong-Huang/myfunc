def divide_line(words,size=60):
    print('*'*size)
    print(' '*((size-len(words))//2)+words+' '*((size-len(words))//2))
    print('*'*size)