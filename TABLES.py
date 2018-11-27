def ngram_creator(text_lst):
    ngrams = []
    for i in range(len(text_lst)-1):
        ngrams.append((text_lst[i], text_lst[i+1]))

    return ngrams


NGE = ngram_creator(['what', 'in', 'the', 'world', 'is', 'going', 'on'])
print(NGE)


def frequency_comparison(table1,table2):
    appearances = 0
    mutual_appearances = 0

    for key1,value1 in table1.items():
        for key2,value2 in table2.items():
            if key1 == key2:
                if value1 < value2():
                    mutual_appearances += value1
                    appearances += value2
            if key1 not in table2.keys():


                mutual_appearances += value2
                appearances += value1

