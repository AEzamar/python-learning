vowels = 'aeiou'
itn = 0
vowel_count = 0
def vowel_counter(str):
    for char in str:
        if char == vowels[itn]:
            vowel_count += 1
    itn += 1
    print(f"The number of vowels in this string is: {vowel_count}")