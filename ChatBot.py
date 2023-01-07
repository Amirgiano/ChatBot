import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:  #If one of these are true
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Ciao!', ['ciao', 'ehi', 'hey', 'ehy', 'ehilà', 'buongiorno', 'buonasera'], single_response=True)
    response('Io sto bene e tu?', ['come', 'stai', 'va'], required_words=['come'])
    response('Prego!', ['grazie','ringrazio'], single_response=True)
    response('Anch\'io ti amo!', ['io', 'ti', 'amo'], required_words=['ti', 'amo'])
    response('"Ao ma chi te insegnate ste parolacce?"', ['cazzo'], required_words=['cazzo'])
    

    # Longer responses
    response(long.R_1, ['mal', 'testa', 'gola infiammata', 'mal di gola','naso chiuso', 'stanchezza', 'febbre', '37', '37.1','37.2', '37.3','37.4','37.5','starnuto','starnutisco','starnutire'], required_words=['starnuto','starnutisco','starnutire'])
    response(long.R_2, ['mal', 'testa', 'gola infiammata', 'mal di gola','naso chiuso', 'stanchezza', 'febbre', '37.5', '37.6','37.7', '37.8','37.9','38', 'gusto', 'gusto','gusto','respirare', 'respiratorio', 'respiratorie'], required_words=[])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while get_response != "Stop":
    print('Ciao sono un Bot, raccontami le difficolt\'a che hai cosi cerco di diagnosare se hai il covid o raffreddore')
    print('Bot: ' + get_response(input('Tu: ')))
    