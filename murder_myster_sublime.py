murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."


def get_average_sentence_length(text):
    # replace punctuation
    no_excl = text.replace("!", ".")
    text_neu = no_excl.replace("?", ".")

    # print(text_neu)
    paragraph_split = text_neu.split(". ")
    # print(paragraph_split)
    paragraph = []
    sentences_in_par = []
    words = []
    word_count = []
    ASL = 0

    for elements in paragraph_split:
        # print(elements)
        paragraph.append(elements)

    for sentences in paragraph:
        sentences_in_par.append(sentences)

    for i in range(len(sentences_in_par)):
        words.append(sentences_in_par[i].split(" "))

    for i in range(len(words)):
        word_count.append(len(words[i]))

    sum = 0
    for nums in word_count:
        # print(words)
        sum += nums
        # print(sum)
        ASL = sum / (len(word_count))

    return print(ASL)


get_average_sentence_length(murder_note)
