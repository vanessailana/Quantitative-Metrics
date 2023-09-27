from rouge_score import rouge_scorer
import csv
import sys 
scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True, split_summaries=True)

# Lists to store ROUGE-L scores and corresponding reference and generated messages
rouge_scores = []
reference_messages = []
generated_messages = []

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        reference = row[0]  # Assuming the first column is the reference sentence
        candidate = row[1]  # Assuming the second column is the generated sentence
        
        # Calculate ROUGE-L score for the candidate sentence against the reference sentence
        rouge = scorer.score(candidate, reference)['rougeL'].fmeasure
        rouge_scores.append(rouge)
        
        # Store reference and generated messages
        reference_messages.append(reference)
        generated_messages.append(candidate)

# Calculate the average ROUGE-L score
if rouge_scores:
    average_rouge_score = sum(rouge_scores) / len(rouge_scores)
    print(f'Average ROUGE-L Score: {average_rouge_score}')
else:
    print('No ROUGE-L scores calculated.')

# Write data to a new CSV file
with open(sys.argv[2], mode='w', newline='') as output_file:
    output = csv.writer(output_file, delimiter=',')
    
    # Write header row
    output.writerow(['Reference Message', 'Generated Message', 'ROUGE-L Score'])
    
    # Write data rows
    for reference, generated, score in zip(reference_messages, generated_messages, rouge_scores):
        output.writerow([reference, generated, score])

