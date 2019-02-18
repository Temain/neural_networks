import re


class TextReader:
    def __init__(self, path):
        with open(path, 'r') as f:
            self.text = f.read()

    def get_text(self):
        text_lower = self.text.lower()
        text_clear = re.sub('[^a-zA-Z]+', '', text_lower)\
            .replace('\r', '').replace('\n', '')
        return text_clear

    def get_sentences(self):
        text_lower = self.text.lower()
        text_clear = re.sub('[^0-9a-zA-Z\\s.]+', '', text_lower)\
            .replace('\r', '').replace('\n', '').replace('. ', '.')
        sentences = text_clear.split('.')
        sentences = list(filter(None, sentences))
        for sent in sentences:
            print(sent + '\r\n')
        print("Sentences count: " + str(len(sentences)))
        return sentences

    def get_words(self):
        text_lower = self.text.lower()
        text_clear = re.sub('[^a-zA-Z\\s]+', '', text_lower).replace('\r', '').replace('\n', '')
        words_list = text_clear.split(' ')
        words = sorted(set(words_list))
        print("Words count: " + str(len(words)))
        return words
