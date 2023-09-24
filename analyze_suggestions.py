import spacy
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained word embedding model (e.g., spaCy's large English model)
nlp = spacy.load("en_core_web_lg")

# Assuming you have the standardized phrases defined as in the previous example
standardized_phrases = ["Optimal performance", 
                        "Utilise resources",
                        'Enhance productivity',
                        'Conduct an analysis',
                        'Maintain a high standard',
                        'Implement best practices',
                        'Ensure compliance',
                        'Streamline operations',
                        'Foster innovation',
                        'Drive growth',
                        'Leverage synergies',
                        'Demonstrate leadership',
                        'Exercise due diligence',
                        'Maximize stakeholder value',
                        'Prioritise tasks',
                        'Facilitate collaboration',
                        'Monitor performance metrics',
                        'Execute strategies',
                        'Gauge effectiveness',
                        "Champion change"
                        ]

# Sample text to analyze
input_text = "In today's meeting, we discussed a variety of issues affecting our department. The weather was unusually sunny, a pleasant backdrop to our serious discussions. We came to the consensus that we need to do better in terms of performance. Sally brought doughnuts, which lightened the mood. It's important to make good use of what we have at our disposal. During the coffee break, we talked about the upcoming company picnic. We should aim to be more efficient and look for ways to be more creative in our daily tasks. Growth is essential for our future, but equally important is building strong relationships with our team members. As a reminder, the annual staff survey is due next Friday. Lastly, we agreed that we must take time to look over our plans carefully and consider all angles before moving forward. On a side note, David mentioned that his cat is recovering well from surgery."

def get_most_similar_phrase(input_phrase, standardized_phrases):
    # Calculate word embeddings for the input phrase
    input_embedding = nlp(input_phrase).vector

    most_similar_phrase = None
    highest_similarity = -1  # Initialize with a low value

    for phrase in standardized_phrases:
        # Calculate word embeddings for the standardized phrase
        phrase_embedding = nlp(phrase).vector

        # Calculate cosine similarity between the input and standardized phrase embeddings
        similarity = cosine_similarity([input_embedding], [phrase_embedding])[0][0]

        # Check if the similarity is higher than the current highest similarity
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_phrase = phrase

    return most_similar_phrase, highest_similarity

# Analyze the input text and provide suggestions
def analyze_text(input_text, standardized_phrases):
    suggestions = []

    # Split the input text into sentences
    sentences = input_text.split('. ')

    for sentence in sentences:
        # Initialize variables for tracking the best suggestion within each sentence
        best_suggestion = None
        highest_similarity = -1

        for phrase in standardized_phrases:
            # Find the most similar phrase in the sentence
            similar_phrase, similarity = get_most_similar_phrase(sentence, [phrase])
            
            # Check if this suggestion has a higher similarity than the previous best
            if similarity > highest_similarity:
                best_suggestion = (sentence, similar_phrase, similarity)
                highest_similarity = similarity

        # Add the best suggestion for this sentence to the list
        if best_suggestion is not None:
            suggestions.append(best_suggestion)

    return suggestions