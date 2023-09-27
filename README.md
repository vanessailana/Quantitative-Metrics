# Quantitative-Metrics


1. **Data Preparation**: Replace the provided `input_file.csv` with your CSV file. Ensure that your CSV file contains two columns: one for reference sentences and one for generated sentences.

2. **Run the Script**: Execute the `meteor.py` script with this command, replacing `input_file.csv` and `output_file.csv` with your file names:

    ```shell
    python meteor.py input_file.csv output_file.csv
    ```

### ROUGE Score Evaluation

To calculate ROUGE-L scores:

1. **Data Preparation**: Replace the provided `input_file.csv` with your CSV file. Ensure that your CSV file contains two columns: one for reference sentences and one for generated sentences.

2. **Run the Script**: Execute the `rouge.py` script with this command, replacing `input_file.csv` and `output_file.csv` with your file names:

    ```shell
    python rouge.py input_file.csv output_file.csv
    ```

## Requirements

- Python 3.x
- NLTK (Natural Language Toolkit) for BLEU and METEOR score calculations.
- ROUGE Python package for ROUGE score calculations.

## Usage

1. Clone this repository to your local machine:

    ```shell
    git clone https://github.com/your-username/text-summarization-evaluation.git
    ```

2. Install the required Python packages:

    ```shell
    pip install -r requirements.txt
    ```

3. Replace `input_file.csv` with your CSV file, ensuring it follows the specified format.

4. Run the desired evaluation script using the provided commands.

5. View the results in the output CSV file, which will contain columns for reference sentences, generated sentences, and evaluation scores.

## Notes

- These scripts are provided as examples and can be customized for specific evaluation needs or metrics.

