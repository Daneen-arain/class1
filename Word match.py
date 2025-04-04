def count_matching_words(words):
    ctr = 0  # Counter for matching words
    lst = []  # List to store matching words

    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:  # Check conditions
            ctr += 1
            lst.append(word)
    
    result = {"Matching words": lst, "Count": ctr, "Total words": len(words)}  # Store results
    print("Result:", result)  # Print the result

# Example usage
words_list = ["level", "hello", "wow", "python", "radar", "abcba", "chat", "noon"]
count_matching_words(words_list)


