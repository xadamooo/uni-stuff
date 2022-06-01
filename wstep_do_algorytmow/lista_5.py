# %% 1


def hamming(string1, string2):
    distance = 0
    length1 = len(string1)
    if length1 == len(string2):
        for i in range(length1):
            if string1[i] != string2[i]:
                distance += 1
    else:
        return
    return distance


def modified_hamming(string1, string2):
    list1 = ['q', 'w', 'e,' 'r', 't', 'y', 'u', 'i', 'o', 'p']
    list2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    list3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    distance = 0
    length1 = len(string1)
    length2 = len(string2)
    if length1 == length2:
        for i in range(length1):
            char1 = string1[i]
            char2 = string2[i]
            try:
                pos1 = list1.index(char1)
                try:
                    pos2 = list1.index(char2)
                    if abs(pos1 - pos2) == 1:
                        distance += 1
                    elif abs(pos1 - pos2) > 1:
                        distance += 2
                except ValueError:
                    try:
                        pos2 = list2.index(char2)
                        if abs(pos1 - pos2) < 2:
                            distance += 1
                        elif abs(pos1 - pos2) > 1:
                            distance += 2
                    except ValueError:
                        distance += 2
            except ValueError:
                try:
                    pos1 = list2.index(char1)
                    try:
                        pos2 = list1.index(char2)
                        if abs(pos1 - pos2) < 2:
                            distance += 1
                        elif abs(pos1 - pos2) > 1:
                            distance += 2
                    except ValueError:
                        try:
                            pos2 = list2.index(char2)
                            if abs(pos1 - pos2) == 1:
                                distance += 1
                            elif abs(pos1 - pos2) > 1:
                                distance += 2
                        except ValueError:
                            distance += 2
                except ValueError:
                    try:
                        pos1 = list3.index(char1)
                        try:
                            pos2 = list2.index(char2)
                            if abs(pos1 - pos2) < 2:
                                distance += 1
                            elif abs(pos1 - pos2) > 1:
                                distance += 2
                        except ValueError:
                            try:
                                pos2 = list3.index(char2)
                                if abs(pos1 - pos2) == 1:
                                    distance += 1
                                elif abs(pos1 - pos2) > 1:
                                    distance += 2
                            except ValueError:
                                distance += 2
                    except ValueError:
                        return
    return distance


def check_in_dict(word, dict):
    try:
        dict.index(word)
    except ValueError:
        similarity_dict = {}
        i = -1
        for phrase in dict:
            i += 1
            if len(phrase) == len(word):
                similarity_dict[phrase] = modified_hamming(word, phrase)
            else:
                pass
        sorted_dict = sorted(similarity_dict.items(), key=lambda kv: kv[1])
        if len(sorted_dict) >= 3:
            for x in range(3):
                print(sorted_dict[x])
        else:
            print(sorted_dict)
    else:
        return('OK')


dict = ['pig', 'bird', 'horse', 'duck', 'cow', 'blue', 'yellow', 'red', 'green', 'pastry',
        'tower', 'building', 'palace', 'castle', 'warrior', 'knight', 'keyboard', 'game', 'mouse', 'rat',
        'dandelion', 'phone', 'speaker', 'vape', 'routing', 'road', 'edge', 'worldwide', 'river', 'ocean',
        'land', 'border', 'fence', 'tree', 'apple', 'countryside', 'landscape', 'weed', 'grass', 'wallet',
        'coat', 'pocket', 'money', 'beer', 'food', 'evening', 'midnight', 'sunrise', 'table', 'chair']

print(hamming('mama', 'nawa'))
print(modified_hamming('mama', 'nawa'))
check_in_dict('paladt', dict)
# %% 2


import pprint
freq_polish = [["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
               [8.167 + 0.990, 1.492, 2.782 + 0.400, 4.253, 12.702 + 1.110, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772,
                4.025 + 1.820, 2.406, 6.749 + 0.200, 7.507 + 0.850, 1.929, 0.095, 5.987, 6.327 + 0.660, 9.056, 2.758,
                0.978, 2.360, 0.150, 1.974, 0.074 + 0.830 + 0.060]]

freq_english = [["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772,
                 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978,
                 2.360, 0.150, 1.974, 0.074]]

freq_german = [["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
               [8.167 + 0.578, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772,
                4.025, 2.406, 6.749, 7.507 + 0.443, 1.929, 0.095, 5.987 + 0.307, 6.327, 9.056 + 0.995, 2.758,
                0.978, 2.360, 0.150, 1.974, 0.074]]

freq_custom = [["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

freq_vc_eng = {'vowels': 0.24, 'consonants': 0.76}
freq_vc_pol = {'vowels': 0.21, 'consonants': 0.79}
freq_vc_ger = {'vowels': 0.23, 'consonants': 0.77}
freq_vc_custom = {'vowels': 0, 'consonants': 0}
vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def freq_table(text, freq_custom):
    text = text.lower()
    text = text.translate(str.maketrans('', '', "!@#$%^~ &*–()-=±+?.,′12−3><‘:º″’©/_\n4°`;ö-‒056789"))
    length = len(text)
    for letter in text:
        index = freq_custom[0].index(letter)
        freq_custom[1][index] += 1
    freq_custom[1] = [x * 100 / length for x in freq_custom[1]]
    return freq_custom[0], freq_custom[1]


def freq_table_to_dict(freq_letter, freq_value):
    freq_dict = {}
    for key in freq_letter:
        for value in freq_value:
            freq_dict[key] = value
            freq_value.remove(value)
            break
    return freq_dict


def compare_tables(table1, table2):
    diff = 0
    for i in range(26):
        diff += abs(table1[i] - table2[i])
    return diff


def freq_vowcon(text, freq_vc_custom):
    text = text.lower()
    text = text.translate(str.maketrans('', '', "!@#$%^~ &*–()-=±+?.,′12−3><‘:º″’©/_\n4°`;ö-‒056789"))
    for letter in text:
        if letter not in vowels:
            freq_vc_custom['consonants'] += 1
        else:
            freq_vc_custom['vowels'] += 1


with open('text.txt', encoding="utf8") as f:
    text = f.read()
    freq1, freq2 = freq_table(text, freq_custom)
    freq_vowcon(text, freq_vc_custom)
    language_diffs = {}
    language_diffs['english'] = compare_tables(freq2, freq_english[1])
    language_diffs['german'] = compare_tables(freq2, freq_german[1])
    language_diffs['polish'] = compare_tables(freq2, freq_polish[1])
    print(f'Most similar language is: {min(language_diffs, key = language_diffs.get)}')
    # print(language_diffs)
    freq_vowcon(text, freq_vc_custom)
    freq_vc_custom['vowels'] /= len(text)
    language_diffs_vowcon = {}
    language_diffs_vowcon['english'] = abs(freq_vc_eng['vowels'] - freq_vc_custom['vowels'])
    language_diffs_vowcon['german'] = abs(freq_vc_ger['vowels'] - freq_vc_custom['vowels'])
    language_diffs_vowcon['polish'] = abs(freq_vc_pol['vowels'] - freq_vc_custom['vowels'])
    print(language_diffs_vowcon)
    print(f'Most similar language (based on vowels/consonants frequency) is: {min(language_diffs_vowcon, key = language_diffs_vowcon.get)}')
    pprint.pprint((freq_table_to_dict(freq1, freq2)))
# %% 3


def longest_common_substring(string1, string2, length1, length2, result):
    if (length1 == 0 or length2 == 0):
        return result
    if (string1[length1 - 1] == string2[length2 - 1]):
        result = longest_common_substring(string1, string2, length1 - 1, length2 - 1, result + 1)
    result = max(result, max(longest_common_substring(string1, string2, length1, length2 - 1, 0),
                             longest_common_substring(string1, string2, length1 - 1, length2, 0)))
    return result


def longest_common_subsequence(string3, string4, length3, length4):
    if length3 == 0 or length4 == 0:
        return 0
    elif string3[length3-1] == string4[length4-1]:
        return 1 + longest_common_subsequence(string3, string4, length3-1, length4-1)
    else:
        return max(longest_common_subsequence(string3, string4, length3, length4-1),
                   longest_common_subsequence(string3, string4, length3-1, length4))


string1 = "konwaliazawalina"
string2 = "zawalina"
string3 = 'apqbcrdsef'
string4 = 'tabucvdewxfyz'
length1 = len(string1)
length2 = len(string2)
length3 = len(string3)
length4 = len(string4)

print(longest_common_substring(string1, string2, length1, length2, 0))
print(longest_common_subsequence(string3, string4, length3, length4))

# %%
