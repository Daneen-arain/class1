from collections import Counter

# Sample list and string
nums = [1, 2, 2, 3, 3, 3, 4]
text = "daneenrules"

# -------------------------
# Manual Frequency Using Dictionary (for List)
freq_dict_list = {}
for num in nums:
    if num in freq_dict_list:
        freq_dict_list[num] += 1
    else:
        freq_dict_list[num] = 1

print("Manual Frequency in List:", freq_dict_list)

# -------------------------
# Manual Frequency Using Dictionary (for String)
freq_dict_str = {}
for char in text:
    if char in freq_dict_str:
        freq_dict_str[char] += 1
    else:
        freq_dict_str[char] = 1

print("Manual Frequency in String:", freq_dict_str)

# -------------------------
# Using Counter (Short Way)
print("Counter Frequency in List:", Counter(nums))
print("Counter Frequency in String:", Counter(text))
