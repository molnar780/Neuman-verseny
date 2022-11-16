   


with open("szoveg1.txt", "rb") as f:
    lines = [str(line).split(" ") for line in f.readlines()]
    words_with_i=0
    for i in range(len(lines)):
        for word in lines[i]:
            if "i" in word:
                words_with_i+=1
            elif "I" in word:
                words_with_i+=1
            
print(words_with_i)