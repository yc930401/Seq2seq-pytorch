file_1 = open('data/OpenSubtitles/OpenSubtitles2016.en', 'r')
file_2 = open('data/OpenSubtitles/processed_OpenSubtitles.txt', 'w')
file_3 = open('data/OpenSubtitles/processed_OpenSubtitles_reverse.txt', 'w')
i = 1

context_1 = '' # context
context_2 = '' # context
question = '' # previous line as question
answer = '' # read one line as answer
output_question = '' # question with concatenated context
while i <= 100000:
    i += 1
    answer = file_1.readline().strip()
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

file_1.close()
file_2.close()
file_3.close()


