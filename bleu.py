# Import the necessary libraries
from nltk.translate.bleu_score import sentence_bleu
import csv
import sys 

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
        output.writerow(['original', 'generated', 'BLEU Score'])  # Header row
        
        # Iterate through each row in the input CSV
        for row in csv_reader:
            # Check if the row has at least two columns for reference and generated sentences
            if len(row) >= 2:
                # Extract the reference sentence from the first column
                reference_sentence = row[0]
                
                # Extract the generated sentence from the second column
                generated_sentence = row[1]
                
                # Calculate the BLEU score for the generated sentence compared to the reference sentence
                bleu_score = sentence_bleu([reference_sentence], generated_sentence)
              
                # Write the original/reference sentence, generated sentence, and BLEU score to the output CSV
                output.writerow([reference_sentence, generated_sentence, bleu_score])
