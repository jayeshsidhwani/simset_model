from model_builder import ModelBuilder
from nltk.stem import SnowballStemmer

class Model():

    def __init__(self):
        self.model = ModelBuilder().build().condense().model
        self.stemmer = SnowballStemmer('english')

    def simset(self, word):
        stemmed_word = self.stemmer.stem(word)
        return self.model.get(stemmed_word, [])