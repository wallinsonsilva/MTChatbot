from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
warnings.filterwarnings(action = 'ignore')

from nltk.corpus import wordnet as wn

synonyms = []
antonyms = []

for syn in wn.synsets("now"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            print(l.antonyms())
            antonyms.append(l.antonyms()[0].name())

# print(set(synonyms))
print(set(antonyms))