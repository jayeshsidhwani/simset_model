from nltk.stem import SnowballStemmer
import code

class ModelBuilder():

    def __init__(self):
        self.model = {}
        self.stemmer = SnowballStemmer('english')

    def build(self):
        with open('data/candidate_synonyms.txt') as f:
            all_words = f.read().split('\n')
            for words in all_words:
                if words:
                    word, similar = words.split(',')
                    word, similar = self.stemmer.stem(word), self.stemmer.stem(similar)
                    if word not in self.model: self.model[word] = {}
                    self.model[word][similar] = 1
        return self

    def condense(self):
        condensed_model = {}
        for word, similars in self.model.items():
            for similar in similars:
                if self.model.get(similar, {}).has_key(word):
                    if condensed_model.has_key(word):
                        condensed_model[word].append(similar)
                    else:
                        condensed_model[word] = [similar]
        self.model = condensed_model
        return self

if __name__ == '__main__':
    print ModelBuilder().build().condense().model