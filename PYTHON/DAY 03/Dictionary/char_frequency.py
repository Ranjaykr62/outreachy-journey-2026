text = "hello world"

# Empty dictionary to store frequency
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:", freq)
