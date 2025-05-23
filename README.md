# Swear-Words-Replacement-Suggestion-System

This project proposes a novel profanity detection and replacement system that enhances user interaction by encouraging respectful communication in online reviews and chats. Offensive words are detected and replaced with category-specific rhyming or amusing alternatives, improving mental well-being for customer service representatives and fostering a kinder online environment.

📖 Published in Springer LNNS Series:  
[Swear Words Replacement Suggestion System – Springer](https://link.springer.com/chapter/10.1007/978-981-16-5655-2_26)

## Features

- Detects offensive language in text input using a trained LSTM deep learning model.
- Replaces detected swear words with contextually related, harmless alternatives.
- Supports multiple product categories (e.g., Food, Clothes, Transport).
- Includes a user-friendly web interface built with HTML/CSS/JS & Python (CGI).
- Achieves high classification accuracy (up to 94.25%) using Glove embeddings + RNN.

## Dataset

- Aggregated from Twitter, Wikipedia, and YouTube comments.
- Balanced between offensive and non-offensive content.
- Category-specific replacement words defined for common profanity.

| Source     | Offensive (%) | Total Samples |
|------------|----------------|----------------|
| Twitter    | 83.2%          | 24,783         |
| Wikipedia  | 10.2%          | 159,571        |
| Combined   | 20.0%          | 184,354        |

## Architecture

- **Preprocessing**: tokenization, lemmatization, stopword removal, and vectorization (CountVectorizer).
- **Models Used**:
  - Linear SVM
  - Random Forest
  - RNN (LSTM) with Glove word embeddings

### Accuracy Comparison

| Model         | 70:30 Split | 80:20 Split |
|---------------|-------------|-------------|
| Linear SVM    | 70.08%      | 79.93%      |
| Random Forest | 93.4%       | 93.45%      |
| RNN (LSTM)    | 93.37%      | **94.25%**  |

## Download Required Files:
Due to GitHub's file size limit, two required files (variables and embedding) are not included in this repository.

Please download them from the following Google Drive link:

 [Download Variables and Embedding Files](https://drive.google.com/drive/folders/1XMKZ896eRKD3mbY1E44zEEiKpthPUaXE?usp=share_link)

After downloading:

- Place the two variables file in the models/model_2/variables directory.
- Place embedding file in models/ directory.
- Ensure their names remain exactly:
variables
embedding
- These files are required for running the prediction model and generating replacement suggestions.

## Usage Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/swear-word-replacement.git
cd swear-word-replacement
```

### 2. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Launch Web Interface

Use XAMPP or another CGI-compatible server to host the Python CGI scripts.

### 4. Try it Out

- Enter a user review with possible offensive content.
- Choose a product category (Food, Clothing, etc.).
- Offensive words will be detected and replaced in real time.

## Example

**Input:**  
> "This fucking service is so shit."

**Output:**  
> "This fruiting service is so shiitake."

## Technologies Used

- Python, LSTM, Random Forest, Scikit-learn
- Glove Word Embedding
- HTML/CSS/JS for GUI
- XAMPP + CGI for web deployment

## Future Work

- Extend support for regional languages (e.g., Hindi, Tamil).
- Implement offensiveness scoring metric.
- Integrate with messaging/chat platforms.

## Citation

If you use this work, please cite the original Springer publication:

```bibtex
@inproceedings{naveen2021swear,
  title={Swear Words Replacement Suggestion System},
  author={Naveen, S and Singh, Mayank and Karthika, S},
  booktitle={Advances in Intelligent Systems and Computing},
  year={2021},
  publisher={Springer},
  doi={10.1007/978-981-16-5655-2_26}
}
```

## License

This project is licensed under the MIT License.
