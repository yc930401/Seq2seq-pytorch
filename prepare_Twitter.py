import re

file_1 = open('data/Twitter/twitter_ids.tuning tweet.txt', 'r', encoding='utf8')
file_2 = open('data/Twitter/processed_Twitter.txt', 'w', encoding='utf8')
file_3 = open('data/Twitter/processed_Twitter_reverse.txt', 'w', encoding='utf8')
file_4 = open('data/Twitter/twitter_ids.validation tweet.txt', 'r', encoding='utf8')


def prepare_data(file_1, file_2, file_3):
    i = 1
    context_1 = '' # context
    context_2 = '' # context
    question = '' # previous line as question
    answer = '' # read one line as answer
    output_question = '' # question with concatenated context
    while i <= 100000:
        i += 1
        data = file_1.readline().split('\t')
        if len(data) >= 4:
            answer = data[3].strip()
            answer = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", answer).split())
            if len(answer) <=2:
                continue
        if len(data) < 4:
            context_1 = ''
            context_2 = ''
            question = ''
            answer = ''
            output_question = ''
            continue
        if question != '':
            if context_1 != '':
                if context_2 != '':
                    output_question = context_2 + ' ' + context_1 + question
                else:
                    output_question = context_1 + question
            else:
                output_question = question
            file_2.write(output_question + '\t' + answer + '\n')
            file_3.write(answer + '\t' + question + '\n')
        else:
            pass
        #context_2 = context_1 # disable to use only one context
        context_1 = question
        question = answer

prepare_data(file_1, file_2, file_3)
prepare_data(file_4, file_2, file_3)

file_1.close()
file_2.close()
file_3.close()
