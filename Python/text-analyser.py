import string
import re

class TextAnalyzer:
    def __init__(self, text):
        self.text = text.lower()  # Convert text to lowercase for consistency

    def word_count(self):
        words = self.text.split()
        return len(words)

    def sentence_count(self):
        sentences = re.split(r'[.!?]', self.text)
        return len(sentences) - 1  # Adjust for extra empty sentence

    def character_count(self):
        return len(self.text)

    def average_word_length(self):
        words = self.text.split()
        total_chars = sum(len(word) for word in words)
        return total_chars / len(words)

    def flesch_reading_ease(self):
        words = self.word_count()
        sentences = self.sentence_count()
        syllables = self.count_syllables()  # Implement syllable count
        score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
        return score

    def gunning_fog_index(self):
        words = self.word_count()
        sentences = self.sentence_count()
        complex_words = self.count_complex_words()  # Implement complex word count
        grade_level = 0.4 * ((words / sentences) + (100 * complex_words / words))
        return grade_level

    def count_syllables(self, wor=""):
        # Ans = 0
        count = 0
        text = self.text.split() if wor == "" else wor.split()
        for i in text:
            vowels = 'aeiouy'
            word = i.lower()
            if word[0] in vowels:
                count += 1
            for index in range(1, len(word)):
                if word[index] in vowels and word[index - 1] not in vowels:
                    count += 1
            if word.endswith('e'):
                count -= 1
            if count == 0:
                count += 1
        return count

    def count_complex_words(self):
        text = self.text
        complex_words_list = set()  # Using a set for faster lookups
        with open('Python\complex_words.txt', 'r') as file:
            for line in file:
                complex_words_list.add(line.strip().lower())
        words = text.split()
        complex_word_count = 0
        for word in words:
            if self.count_syllables(word) >= 3 or word.lower() in complex_words_list:
                complex_word_count += 1
        return complex_word_count

    def frequency_analysis(self, n=10):
        words = self.text.split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:n]
        return most_common

text = "This is a sample text that I wrote for the text-analyser program. "
analyzer = TextAnalyzer(text)

print("Word count:", analyzer.word_count())
print("Sentence count:", analyzer.sentence_count())
print("Character count:", analyzer.character_count())
print("Average word length:", analyzer.average_word_length())
print("Flesch Reading Ease:", analyzer.flesch_reading_ease())
print("Gunning Fog Index:", analyzer.gunning_fog_index())
print("Most common words:", analyzer.frequency_analysis())

