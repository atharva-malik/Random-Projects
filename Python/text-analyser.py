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

    def count_syllables(self):
        # Implement syllable counting logic
        pass

    def count_complex_words(self):
        # Implement complex word counting logic
        pass

    def frequency_analysis(self, n=10):
        words = self.text.split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:n]
        return most_common

text = "This is a sample text for analysis. It contains several sentences and words."
analyzer = TextAnalyzer(text)

print("Word count:", analyzer.word_count())
print("Sentence count:", analyzer.sentence_count())
print("Character count:", analyzer.character_count())
print("Average word length:", analyzer.average_word_length())
print("Flesch Reading Ease:", analyzer.flesch_reading_ease())
print("Gunning Fog Index:", analyzer.gunning_fog_index())
print("Most common words:", analyzer.frequency_analysis())

