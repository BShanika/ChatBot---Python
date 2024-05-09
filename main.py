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
    if has_required_words or single_response:
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
    response('Hello!', ['hello', 'hi', 'hey'], single_response=True)
    response('I\'m a chatbot', ['who', 'are', 'you'], required_words=['who'])
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('It\'s great!', ['I\'m', 'fine'], required_words=['fine'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('How can I help you?', ['help', 'want'], single_response=True)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_FEEL, ['How', 'you', 'feelings'], required_words=['you', 'feelings'])
    response(long.R_HOBBY, ['tell', 'your', 'hobbies'], required_words=['your', 'hobbies'])
    response(long.R_SMILE, ['what', 'make', 'you', 'smile'], required_words=['you', 'smile'])
    response(long.R_TRAVEL, ['have', 'you', 'traveled', 'anywhere'], required_words=['you', 'traveled'])
    response(long.R_GOAL, ['goals', 'goal', 'aspirations'], single_response=True)
    response(long.R_SUGGEST, ['do', 'you', 'have', 'plans', 'weekend', 'getaway'], required_words=['plans', 'weekend'])
    response(long.R_ADDVEN, ['I\'m ', 'up', 'adventurous'], required_words=['adventurous'])
    response(long.R_RELAX, ['I\'m', 'inclined', 'relaxing'], required_words=['relaxing'])
    response(long.R_RECOMMEND, ['Any', 'mountain', 'range', 'you\'d', 'recommend'], required_words=['mountain'])
    response(long.R_CABIN, ['cozy', 'cabin', 'woods'], single_response=True)
    response(long.R_LAKE, ['I\'d', 'like', 'lake'], required_words=['lake'])
    response(long.R_FOREST, ['surround', 'forest', 'trail'], single_response=True)
    response(long.R_BEACH, ['I\'d', 'like', 'beach', 'destinations'], required_words=['beach'])
    response(long.R_TROP, ['I\'m', 'leaning', 'tropical'], required_words=['tropical'])
    response(long.R_HOME, ['I\'d', 'like', 'lake'], required_words=['home','closer'])
    response(long.R_THANK, ['thanks', 'for', 'recommendations'], required_words=['thanks', 'for'])
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
while True:
    print('Bot: ' + get_response(input('You: ')))