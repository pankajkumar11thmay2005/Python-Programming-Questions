s = "programming"

vowels = set("aeiou")
vowel_count = 0
consonant_count = 0

for ch in s.lower():
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)