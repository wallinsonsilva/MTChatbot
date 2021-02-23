from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import warnings
warnings.filterwarnings(action = 'ignore')
from main.SubstituicoesPalavras.ThesaurosRest import ThesaurosRest

the = ThesaurosRest()

antonimo = the.versoes_antonimo('I want to change my email and phone now')
for a in antonimo:
    print(a)

brown_ic = wordnet_ic.ic('ic-brown.dat')

entrada = 'well'

sinonimos = wn.synsets(entrada,wn.VERB)
for s in sinonimos:
    for l in s.lemmas():
        print(l)
        print(l.name())
        for a in l.antonyms():
            print(a)