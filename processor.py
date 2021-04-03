import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from utils import expand_contractions, get_wordnet_pos
import json


with open('word_rank.json') as json_file:
    dictionary = json.load(json_file)


def decontract(text):
    decontracted = expand_contractions(text)
    return decontracted


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def filter(tokens):
    filtered = list()
    for token in tokens:
        if token.isalpha():
            filtered.append(token.lower())
    return filtered


def tag(words):
    return nltk.pos_tag(words)


def lemmatize(words):
    roots = list()
    lemmatizer = WordNetLemmatizer()
    for word in words:
        tag = word[1]
        wordnet_tag = get_wordnet_pos(tag)
        inflection = word[0]
        if wordnet_tag == '':
            root = inflection
        else:
            root = lemmatizer.lemmatize(inflection, get_wordnet_pos(tag))
        roots.append(root)
    return roots


# compute word score
def get_word_score(roots):
    word_scores = dict()
    for root in roots:
        if root in dictionary:
            word_scores[root] = calculate_percentile(dictionary[root])
    return word_scores


# calculate percentile
def calculate_percentile(rank):
    percentile  = rank * 100 / len(dictionary)
    return round(percentile, 2)


# calculate and return words with respective word scores
def process(text):
    decontracted_text = decontract(text)

    tokens = tokenize(decontracted_text)

    filtered_tokens = filter(tokens)

    tagged_tokens = tag(filtered_tokens)

    roots = lemmatize(tagged_tokens)

    word_scores = get_word_score(roots)

    return word_scores