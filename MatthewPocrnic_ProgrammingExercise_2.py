# The list of 30 common spam words and phrases
spam_keywords = [
    "free", "winner", "click here", "cash", "prize", "guarantee",
    "congratulations", "act now", "limited time", "urgent", "special promotion",
    "risk-free", "buy now", "order now", "win", "winner!", "credit card",
    "call now", "don't delete", "instant", "cheap", "bargain", "earn money",
    "extra income", "miracle", "promise", "100% free", "trial", "amazing", "no obligation"
]

# This is the function to calculate the spam score
def calculate_spam_score(message, spam_words):
    message_lower = message.lower()
    score = 0
    found = {}

    for word in spam_words:
        occurrences = message_lower.count(word)
        if occurrences:
            found[word] = occurrences
            score += occurrences

    return score, found

# This is the function to classify the likelihood of spam
def classify_spam(score):
    if score == 0:
        return "Not Spam"
    if score <= 2:
        return "Low likelihood of spam"
    if score <= 5:
        return "Moderate likelihood of spam"
    return "High likelihood of spam"

# Main application
def main():
    print("Spam Detector")
    print("=" * 20)

    message = input("Enter your email message:\n")

    score, found = calculate_spam_score(message, spam_keywords)
    classification = classify_spam(score)

    print("\nResults")
    print("-" * 20)
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood: {classification}")

    if found:
        print("\nDetected spam words/phrases:")
        for word, count in found.items():
            print(f"'{word}': {count} time(s)")
    else:
        print("\nNo spam indicators found.")

# Run application
if __name__ == "__main__":
    main()
