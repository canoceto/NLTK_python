import nltk
from nltk.corpus import sentiwordnet as swn, stopwords


def classi(text):
    dictionary = dict()
    english_stops = set(stopwords.words('english'))
    sentences = nltk.sent_tokenize(text, language='english')
    for sentence in sentences:
        tokens = nltk.word_tokenize(
            sentence)  # "May 22nd is the best day of the year")  # for tokenization, row is line of a file in which tweets are saved.
        word = [word for word in tokens if word not in english_stops]
        tagged = nltk.pos_tag(tokens)  # for POSTagging
        pscore = 0
        nscore = 0
        polAdjetivo = 0
        polSustantivo = 0
        polVerbo = 0
        polAdvervio = 0
        for i in range(0, len(tagged)):
            if 'NN' in tagged[i][1]:

                # pscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0],'n'), 'n'))[0]).pos_score()  # positive score of a word
                # nscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0],'n'), 'n'))[0]).neg_score()  # negative score of a word

                pscore += (list(swn.senti_synsets(tagged[i][0], 'n'))[0]).pos_score()  # positive score of a word
                nscore += (list(swn.senti_synsets(tagged[i][0], 'n'))[0]).neg_score()  # negative score of a word
                polSustantivo += pscore - nscore
            elif 'VB' in tagged[i][1]:
                # pscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0],'v'), 'v'))[0]).pos_score()
                # nscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0],'v'), 'v'))[0]).neg_score()

                pscore += (list(swn.senti_synsets(tagged[i][0], 'v'))[0]).pos_score()
                nscore += (list(swn.senti_synsets(tagged[i][0], 'v'))[0]).neg_score()
                polVerbo += pscore - nscore
            elif 'JJ' in tagged[i][1]:
                # pscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0], 'a'), 'a'))[0]).pos_score()
                # nscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0], 'a'), 'a'))[0]).neg_score()

                pscore += (list(swn.senti_synsets(tagged[i][0], 'a'))[0]).pos_score()
                nscore += (list(swn.senti_synsets(tagged[i][0], 'a'))[0]).neg_score()
                polAdjetivo += pscore - nscore
            elif 'RB' in tagged[i][1]:
                # pscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0], 'r'), 'r'))[0]).pos_score()
                # nscore += (list(swn.senti_synsets(nltk.WordNetLemmatizer.lemmatize(tagged[i][0], 'r'), 'r'))[0]).neg_score()

                pscore += (list(swn.senti_synsets(tagged[i][0], 'r'))[0]).pos_score()
                nscore += (list(swn.senti_synsets(tagged[i][0], 'r'))[0]).neg_score()
                polAdvervio += pscore - nscore

        result = 0.4 * polAdjetivo + 0.3 * polSustantivo + 0.2 * polVerbo + 0.1 * polAdvervio
        if result > 0:
            dictionary[sentence] = 'POS'
            print("positivo = {} ".format(result))
        elif result < 0:
            dictionary[sentence] = 'NEG'
            print("negativo= {} ".format(result))
        else:
            dictionary[sentence] = 'NEU'
            print("neutral")

    return dictionary
