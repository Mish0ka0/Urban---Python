class WordsFinder:
    file_names = []

    def __init__(self, *file_names):
        for file in file_names:
            self.file_names.append(file)

    @staticmethod
    def string_replace(st):
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for char in punctuation:
            st = st.replace(char, '')
        return st

    def get_all_words(self):
        all_words = {}
        for files in self.file_names:
            with open(files, encoding='utf-8') as file:
                a = []
                for line in file:
                    line1 = self.string_replace(line).lower()
                    a.extend(line1.split())
                all_words.update({files: a})
        return all_words

    def find(self, word):
        my_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                index = words.index(word.lower()) + 1
                my_dict[name] = index
        return my_dict

    def count(self, word):
        my_dict = {}
        a = 0
        for name, words in self.get_all_words().items():
            for wrod in words:
                if word.lower() == wrod:
                    a += 1
            my_dict[name] = a
        return my_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
