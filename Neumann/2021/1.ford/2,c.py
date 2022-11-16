   


with open("szoveg1.txt", "rb") as f:
    lines = [str(line).split(" ") for line in f.readlines()]
    words_i_a_n=0
    for i in range(len(lines)):
        for word in lines[i]:
            if "i" and "a" in word:
                if "n" not in word:
                    words_i_a_n+=1
            if "i" and "n" in word:
                if "a" not in word:
                    words_i_a_n+=1
            if "a" and "n" in word:
                if "i" not in word:
                    words_i_a_n+=1
                
print(words_i_a_n+)
