# Import the necessary libraries
from nltk.translate.meteor_score import single_meteor_score
from nltk.tokenize import word_tokenize
import csv
import nltk
import sys 

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Open the CSV file containing generated and reference sentences
with open(sys.argv[1]) as csv_file:
    # Create a CSV reader to parse the file, specifying the delimiter (',')
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Skip the header row (if it exists) as it contains column names
    header = next(csv_reader, None)
    
    # Open an output CSV file for writing the results, specifying newline='' to avoid extra line breaks
    with open(sys.argv[2], mode='w', newline='') as output_file:
        # Create a CSV writer for the output file, specifying the delimiter (',')
        output = csv.writer(output_file, delimiter=',')
        
        # Write the header row for the output file
        output.writerow(['reference', 'generated', 'METEOR Score'])  # Header row
        
        # Iterate through each row in the input CSV
        for row in csv_reader:
            # Check if the row has at least two columns for reference and generated sentences
            if len(row) >= 2:
                # Extract the reference sentence from the first column
                reference_sentence = row[0]
                
                # Extract the generated sentence from the second column
                generated_sentence = row[1]
                
                # Tokenize both reference and generated sentences into words
                reference_tokens = word_tokenize(reference_sentence)
                generated_tokens = word_tokenize(generated_sentence)
                
                # Calculate the METEOR score for the generated sentence compared to the reference sentence
                meteor_score = single_meteor_score(reference_tokens, generated_tokens)
                
                # Write the reference sentence, generated sentence, and METEOR score to the output CSV
                output.writerow([reference_sentence, generated_sentence, meteor_score])
