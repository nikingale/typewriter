# read corpus for obtaining ranks
with open("resources/google-corpus.txt") as input:
    content = input.readlines()
corpus = dict()
rank = 1
for x in content:
    corpus[x.strip()] = rank
    rank += 1


# create souce of truth dict with rank
dict_words = list(i for i in wordnet.all_synsets())
print('dict_words', len(dict_words))
unsorted_dictionary = dict()
for word in dict_words:
    key = word.lemmas()[0].name().lower()
    if key in corpus:
        unsorted_dictionary[key] = corpus[key]


# sort dict to creat new ranks based on current dict size
dictionary = dict(sorted(unsorted_dictionary.items(), key=lambda x: x[1]))
wordRank = 1
for word in dictionary:
    dictionary[word] = wordRank
    wordRank += 1

dictionary_size = len(dictionary)

with open('word_rank.json', 'w') as fp:
    json.dump(dictionary, fp)