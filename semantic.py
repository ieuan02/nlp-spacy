import spacy
nlp = spacy.load('en_core_web_md')

# EXTRACT 1: Similarity comparison of "cat", "monkey" and "banana"
print("EXTRACT 1 RESULTS:")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("")

"""
The comparison of the three words and their values follows logically. Cat and monkey share the highest similarity
amongst our sample, as they are both animals. Secondly, the higher similarity between banana and monkey (as opposed to
cat and monkey) makes sense to us; as bananas are part of a monkey's diet, unlike cats, and hence both words are much
more likely to show alongside each other, and share a relation, hence the higher similarity. Cats don't normally eat
bananas, and as we'd expect, provides the lowest similarity value. Below is an example I have provided:
"""

print("MY OWN EXAMPLE:")
task_words = nlp('dog rabbit bark')
for task_word1 in task_words:
    for task_word2 in task_words:
        if task_word1 != task_word2:  # if clause removes duplicate comparisons, where we know similarity would be 1.0
            print(task_word1.text, task_word2.text, task_word1.similarity(task_word2))
print("")

"""
My example follows a similar trend to extract 1. Dog and rabbit are closest, given they are both animals, though dog is
more similar to bark than rabbit, due to the fact that dogs bark and the two words will be used in conjunction more in
language given this context.
"""


# EXTRACT 2: Similarity comparison as previous with inclusion of "apple"
print("EXTRACT 2 RESULTS:")
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("")


# EXTRACT 3: Comparison of longer sentences
print("EXTRACT 3 RESULTS:")
sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
