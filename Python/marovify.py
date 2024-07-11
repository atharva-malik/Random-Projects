import markovify

#* Hope flickered in sacrifice, a golden light. - Marovify.py

file = open("Python\markov.txt", "r")
text = file.read()

model = markovify.Text(text, state_size=1)

print(model.make_sentence())
