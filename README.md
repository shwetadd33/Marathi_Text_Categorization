# Marathi News Categorization

This project focuses on the automatic categorization of Marathi news articles using machine learning techniques, primarily the K-Nearest Neighbors (K-NN) algorithm with various distance measures. The system classifies articles into categories like sports, politics, entertainment, editorial, and local news, facilitating easy and quick access for users.

## Introduction

With the rise in online information, text categorization has become essential for managing and organizing large amounts of text data. This project addresses the unique challenges posed by categorizing Marathi news articles, given the limited existing research on non-English texts. The proposed solution involves gathering online news data, pre-processing it, and applying K-NN with TF-IDF weighting for text classification.

## Prerequisites

1. Python
2. [PyCharm IDE](https://www.jetbrains.com/pycharm/download) (Professional free trial available)
3. Internet connection (for crawling news articles)

Refer to [this YouTube playlist](https://www.youtube.com/watch?v=HBxCHonP6Ro&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_) for working with PyCharm.

## Setup Instructions

### Clean Up

Remove the following files and folders to streamline your workspace:
- Folders: `eco_dupli`, `TextTest_eco_new`, `TextTest_ecod`, `TextTest_en_newt`, `TextTest_entd`, `TextTest_sprtd`
- Files: `Deciding_Kvalue.py`, `dict.txt`, `output_old.txt`, `readword.py`, `testnewsarticles.txt`, `tfidf.py`

### Project Files

#### Training and Testing Data
The following files contain the logic for collecting training and testing data by scraping news articles from [eSakal](https://www.esakal.com/):
- `economy_train_data.py`: Training data for economy category
- `entertain_train_data.py`: Training data for entertainment category
- `sport_train_data.py`: Training data for sports category
- `test_news_data.py`: Testing data with a mix of all categories

**Folders**:
- `Text`: 3500 training samples for sports
- `TextEconomy`: 3500 training samples for economy
- `TextEnter`: 3500 training samples for entertainment
- `TextTest`: 1750 mixed-category testing samples

#### Tokenization and Pre-processing
- `noun.txt`, `adjective.txt`, `adverb.txt`, `verb.txt`: Dictionaries for Marathi nouns, adjectives, adverbs, and verbs
- `stopword.txt`: List of Marathi stopwords for removing unimportant words during pre-processing

### Running the Experiment

To execute the final categorization experiment, run any of the following Python files based on your preferred distance measure:

| File | Distance Measure |
| --- | --- |
| `finalprediction.py` | Euclidean |
| `finalprediChebyshev.py` | Chebyshev |
| `finalprediCosine.py` | Cosine |
| `finalprediJaccard.py` | Jaccard |
| `finalprediManhatt.py` | Manhattan |

**Workflow**:
1. Run `finalprediction.py` or any other file based on the desired distance measure.
2. The script calls `testnews.py` (for calculating TF and TF-IDF vectors) and `Common_IDF_Cal.py` (for creating the final IDF vector).
3. Each training and testing sample undergoes TF-IDF processing to prepare for K-NN classification.

### K-NN Classification

The experiment is conducted with different values of K (3, 10, and √total training samples) to determine the optimal K for the classification. Other files follow a similar structure but implement different distance measures.

For additional information on distance measures and TF-IDF, refer to:
- [TF-IDF for Document Ranking](https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089)
- [K-NN Distance Measures](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)

---

Happy categorizing!

## NOTE : For more detailed description of the project please refer - readme.docx file from the project repository 
