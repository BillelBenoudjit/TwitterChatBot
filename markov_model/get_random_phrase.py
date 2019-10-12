import markovify
import json

with open('small_markov_model_state_3.json', 'rb') as f:
	markov_model_state_3 = markovify.NewlineText.from_json(f.read())

print(markov_model_state_3.make_sentence())