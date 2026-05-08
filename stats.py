def get_num_words(text):
    words = text.split()
    return len(words)

def counter(text):
    dic = {}
    for word in text:
        lowered = word.lower()
        if lowered in dic:
            dic[lowered] += 1
        else:
            dic[lowered] = 1
    return dic

sorted_list = {"char": "a", "num": 0}

def sort_on(sorted_list):
    return sorted_list["num"]

def report(counter):
    rapport = []
    for char in counter:
        value = counter[char]
        rapport.append({"char": char, "num": value})
    rapport.sort(reverse=True, key=sort_on)
    return rapport