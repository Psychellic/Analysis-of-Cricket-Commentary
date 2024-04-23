from nltk.stem import WordNetLemmatizer
from collections import defaultdict

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Dictionary for holding the lemmatized words and their total frequencies
lemma_freq = defaultdict(int)

# Read the file and process each line
with open('tokens.txt', 'r') as file:
    for line in file:
        # Split the line into word and its frequency
        word, freq = line.strip().split()
        # Lemmatize the word
        lemma_word = lemmatizer.lemmatize(word)
        # Aggregate the frequencies
        lemma_freq[lemma_word] += int(freq)

# Sort the dictionary by frequency (from highest to lowest)
sorted_lemma_freq = dict(sorted(lemma_freq.items(), key=lambda item: item[1], reverse=True))

# Write the sorted lemmatized dictionary to a file
with open('lemma.txt', 'w') as fout:
    for word, freq in sorted_lemma_freq.items():
        fout.write(f"{word} {freq}\n")
