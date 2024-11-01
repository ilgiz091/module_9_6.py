def all_variants(text):
    for j in text:
        yield j

    for k in range(2, len(text) + 1):
        for n in range(len(text) - k + 1):
            yield text[n:n + k]

a = all_variants("abc")
for i in a:
    print(i)
