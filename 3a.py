def analyze_sentence(sentence):
 word_count = len(sentence.split())
 digit_count = 0
 uppercase_count = 0
 lowercase_count = 0
 for char in sentence:
 if char.isdigit():
 digit_count += 1
 elif char.isupper():
 uppercase_count += 1
 elif char.islower():
 lowercase_count += 1
 return word_count, digit_count, uppercase_count, lowercase_count
user_sentence = input("Enter a sentence: ")
word_count, digit_count, uppercase_count, lowercase_count = 
analyze_sentence(user_sentence)
print("Number of words:", word_count)
print("Number of digits:", digit_count)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
