s = input("Please write down a sentence: ")
words = s.split()
avg = sum(len(word) for word in words) / len(words)
print(avg)