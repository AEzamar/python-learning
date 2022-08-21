def vowel_counter(str):
    vowels = 'aeiou'
    vowel_count = 0
    itn = 0
    for char in str:
        if char == vowels[itn]:
            vowel_count += 1
    itn += 1
    print(f"The number of vowels in this string is: {vowel_count}")


vowel_counter("zdslw")