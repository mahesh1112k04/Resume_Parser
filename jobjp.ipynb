import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Prepare the job description and candidate profiles
job_description = "We are looking for a candidate with strong communication skills, experience in project management, and proficiency in Python programming."
candidate_profiles = [
    ("John", "John is a highly skilled communicator with a background in project management. He is also proficient in Python programming."),
    ("Sarah", "Sarah has excellent communication skills and has successfully managed multiple projects. She is familiar with Python programming."),
    ("Michael", "Michael is a software developer with expertise in Python programming, but he lacks experience in project management."),
]

# Tokenize the job description
job_tokens = word_tokenize(job_description)

# Remove stopwords from the job description tokens
stop_words = set(stopwords.words("english"))
job_tokens = [token.lower() for token in job_tokens if token.lower() not in stop_words]

# Compare job description with candidate profiles
best_candidate = None
best_score = 0

for candidate_name, candidate_profile in candidate_profiles:
    # Tokenize and remove stopwords from candidate profiles
    candidate_tokens = word_tokenize(candidate_profile)
    candidate_tokens = [token.lower() for token in candidate_tokens if token.lower() not in stop_words]

    # Calculate the matching score between job description and candidate profile
    match_score = len(set(job_tokens).intersection(candidate_tokens))

    if match_score > best_score:
        best_candidate = candidate_name
        best_score = match_score

# Print the best candidate
print("Best candidate for the job:", best_candidate)
