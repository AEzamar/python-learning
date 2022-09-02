def reverse(st):
    st_list = st.split()
    i = -1
    reverse_st = []
    for word in st_list:
        reverse_st.append(st_list[i])
        i += -1
    return " ".join(reverse_st)


print(reverse("Hello Dang World!"))