def vowel_counter(str):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    itn = 0
    for char in str.lower():
        if char in vowels_list: 
            vowel_count += 1
            #print(char)
            #print(vowels_list[itn])
    itn += 1
        
    print(f"The number of vowels in this string is: {vowel_count}")


vowel_counter("zdslw")
vowel_counter("Lalafell")