forbidder_words = {"игнорируй"}
def check (answer):
    answer_lower = answer.lower()
    for word in forbidder_words:
        if word in answer_lower:
            return 1
    return 0
