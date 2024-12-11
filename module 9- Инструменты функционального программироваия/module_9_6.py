def all_variants(text):
    for i in range(len(text)):
        if i < len(text):
            a = i + 1
            count = 0
            while i < len(text):
                yield text[count: a + count]
                count += 1
                i += 1


ob = all_variants('abc')
for o in ob:
    print(o)

