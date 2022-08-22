def vowel_counter(str):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for char in str.lower():
        if char in vowels_list: 
            vowel_count += 1
        
    return f"The number of vowels in this string is: {vowel_count}"


print(vowel_counter("zdslw"))
print(vowel_counter("Lalafell"))