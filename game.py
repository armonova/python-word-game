def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


def search_line(letters, words):
    find_words = []
    for c in range(len(letters[0])):
        for l in range(len(letters)):
            word_find = None
            for w in range(len(words)):
                if words[w][0] == letters[l][c]:
                    find_words.append({
                        'word': words[w],
                        'start': {'column': c, 'line': l},
                        'end': {}
                    })
                    for i in range(len(words[w])):
                        if (len(letters) - 1) >= (l + i):
                            if words[w][i] != letters[l + i][c]:
                                index = find(find_words, 'word', words[w])
                                find_words.pop(index)
                                break
                            if i == (len(words[w]) - 1):
                                index = find(find_words, 'word', words[w])
                                find_words[index]['end'] = {'column': c, 'line': l + i}
                                word_find = words[w]
                        else:
                            # print(findWords)
                            index = find(find_words, 'word', words[w])
                            find_words.pop(index)
                            break
            if word_find != None:
                index = words.index(word_find)
                words.pop(index)
    return find_words


def search_columns(letters, words):
    find_words = []
    for l in range(len(letters)):
        for c in range(len(letters[l])):
            word_find = None
            for w in range(len(words)):
                if words[w][0] == letters[l][c]:
                    find_words.append({
                        'word': words[w],
                        'start': {'column': c, 'line': l},
                        'end': {}
                    })
                    for i in range(len(words[w])):
                        if (len(letters[l]) - 1) >= (c + i):
                            if words[w][i] != letters[l][c + i]:
                                index = find(find_words, 'word', words[w])
                                find_words.pop(index)
                                break
                            if i == (len(words[w]) - 1):
                                index = find(find_words, 'word', words[w])
                                find_words[index]['end'] = {'column': c + i, 'line': l}
                                word_find = words[w]
                        else:
                            # print(findWords)
                            index = find(find_words, 'word', words[w])
                            find_words.pop(index)
                            break
            if word_find != None:
                index = words.index(word_find)
                words.pop(index)
    return find_words


letters = [['C', 'M', 'O', 'C', 'H', 'I', 'L', 'A', 'K'],
           ['Â', 'I', 'V', 'S', 'W', 'U', 'L', 'Y', 'E'],
           ['T', 'J', 'N', 'U', 'J', 'A', 'Ó', 'X', 'M'],
           ['A', 'A', 'R', 'T', 'M', 'Ó', 'L', 'Ê', 'Q'],
           ['M', 'Q', 'T', 'I', 'O', 'F', 'G', 'C', 'À'],
           ['A', 'U', 'P', 'A', 'R', 'T', 'H', 'U', 'R'],
           ['N', 'E', 'N', 'S', 'I', 'H', 'A', 'T', 'T'],
           ['C', 'T', 'P', 'M', 'L', 'Â', 'Ó', 'I', 'O'],
           ['O', 'A', 'Ô', 'F', 'T', 'C', 'Ô', 'B', 'A']]

words = ['TAMANCO', 'UTI', 'ARTHUR']

# print('A = ', letters)
# print('Words: ', words)
# print(len(letters))
# print(len(letters[0]))

returnFunction = search_line(letters, words) + search_columns(letters, words)
print(returnFunction)
