import string
#Importing Numpy by giving alias name as np
import numpy as np

"""The task of this Function is takes the text and make operations like removing all unnecessary Symbols like 
   punctuation and after converts it into lowercase string"""
def preprocess_text(text):
    """
    Preprocesses the text by removing punctuation and converting it to lowercase.
    """
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    return text

def calculate_similarity(text1, text2):
    """
    The task of this Function is to Calculates the similarity between two texts using the Levenshtein distance algorithm.
    Returns a similarity score between 0 and 1, where 1 indicates identical texts.
    """
    m = len(text1)
    n = len(text2)

    if m == 0 or n == 0:
        return 0

    # Initialize a matrix to store the Levenshtein distances
    distances = np.zeros((m+1, n+1))

    for i in range(m+1):
        distances[i][0] = i

    for j in range(n+1):
        distances[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                distances[i][j] = min(distances[i-1][j] + 1,    # Deletion
                                      distances[i][j-1] + 1,    # Insertion
                                      distances[i-1][j-1] + 1)  # Substitution

    max_distance = max(m, n)
    similarity = 1 - (distances[m][n] / max_distance)
    return similarity

def check_plagiarism(text1, text2, threshold=0.8):
    """
    Checks if two texts are plagiarized based on a similarity threshold.
    Returns True if the texts are plagiarized, False otherwise.
    """
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)

    similarity = calculate_similarity(processed_text1, processed_text2)

    if similarity >= threshold:
        return True
    else:
        return False

# Input texts from user
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

is_plagiarized = check_plagiarism(text1, text2)

if is_plagiarized:
    print("Texts are plagiarized.")
else:
    print("Texts are not plagiarized.")
