   


with open("szoveg1.txt", "rb") as f:
    lines = [str(line).split(" ") for line in f.readlines()]
    words_i__an=0
    for i in range(len(lines)):
        for word in lines[i]:
            if "i" in word:
                n=len(word)
                for char in range(n):
                    if "i" == word[char] and char+4<n-1:
                        if word[char+2] == "a" and word[char+3] == "n":
                            words_i__an += 1
            
print(words_i__an)