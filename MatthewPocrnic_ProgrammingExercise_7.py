# Import the 're' module for working with regular expressions

import re

def split_into_sentences(text):
    """
    Breaks a paragraph into individual sentences.
    This method tries to handle common sentence-ending punctuation while avoiding issues with things like decimals or abbreviations.
    """
    # This regex looks for sentence-ending punctuation followed by a space and a capital letter or end of text
    sentence_pattern = r'[A-Z0-9].*?[.!?](?=\s[A-Z0-9]|$)'
    
    # Find all matches in the input text using the pattern
    sentences = re.findall(sentence_pattern, text, flags=re.DOTALL | re.MULTILINE)
    
    return sentences  

def print_sentences(sentences):
    """
    Displays each sentence on its own line and shows how many were found.
    """
    # Loop through the list and number each sentence
    for i, sentence in enumerate(sentences, 1):
        # Print the sentence with leading/trailing spaces removed
        print(f"{i}: {sentence.strip()}")  

    # Print the total count
    print(f"\nTotal number of sentences: {len(sentences)}")  

def main():
    """
    Main function that takes user input and processes it.
    """
    # Prompt the user to input a paragraph, split the paragraph into sentences and print each sentence and the total count
    paragraph = input("Please enter a paragraph of text:\n")  
    sentences = split_into_sentences(paragraph) 
    print_sentences(sentences)  

if __name__ == "__main__":
    main()
