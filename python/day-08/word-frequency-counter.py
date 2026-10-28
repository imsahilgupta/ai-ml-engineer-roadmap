text = input("Enter a sentence: ").lower()

# Basic normalization and tokenization
words = text.split()

word_counts = {}

for word in words:
    # Remove common punctuation around each word
    word = word.strip(".,!?;:\"'()[]{}")

    if not word:
        continue

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nWord frequencies:")

for word, count in word_counts.items():
    print(f"{word}: {count}")

print("Unique words:", len(word_counts))
