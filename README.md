<div align="center">

# User Sentiment Analysis
# 🎭

### A small Persian review classifier

A Python script that cleans Persian movie reviews with hazm, trains a Naive Bayes model, and labels a new review as positive or negative.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![hazm](https://img.shields.io/badge/hazm-Persian%20NLP-1ABC9C?style=for-the-badge)](https://github.com/roshan-research/hazm)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/license/mit)
![Open Source](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📧 Email](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Why This Project?](#-why-this-project)
- [Key Features](#-key-features)
- [Pipeline](#-pipeline)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Installation](#-installation)
- [Usage](#️-usage)
- [Notes](#-notes)
- [FAQ](#-faq)
- [Contact](#-contact)
- [License](#-license)
- [Support](#-support)

---

# 📖 About

**User Sentiment Analysis** is a small Persian text classifier.

`code.py` reads `IMDB_Dataset_Persian.xlsx`, normalizes each review with hazm, removes stop words, stems the tokens, and turns the text into word counts. A Multinomial Naive Bayes model is trained on that matrix and then used to label new Persian reviews.

The labels in the sheet are `positive`, `negative`, and `neutral`. The script treats only `positive` as class 1. Everything else, including `neutral`, becomes class 0.

> **Tagline:** *A small Persian movie-review classifier using hazm and scikit-learn.*

---

# 🚀 Why This Project?

Persian text needs its own cleanup before a bag-of-words model can see it.

This script keeps that path short:

- Load an Excel sheet of reviews
- Normalize, tokenize, and stem with hazm
- Count words with scikit-learn
- Train, score, and try new sentences

It is a study classifier, not a production sentiment service. The broader course notebooks live in [AI and Machine Learning Training](https://github.com/sadra-hatami/AI-ML-Training).

---

# ✨ Key Features

- 📄 Excel input: `IMDB_Dataset_Persian.xlsx`
- 🧹 Persian normalization, tokenization, and stemming
- 🚫 Stop-word removal
- 🔢 Count vectors, up to 5000 features
- 🧪 Train and test split
- 📊 Accuracy, confusion matrix, and classification report
- 💬 A function for a new Persian review

---

# 🔁 Pipeline

```text
IMDB_Dataset_Persian.xlsx
 └─ code.py
     ├─ hazm normalize / tokenize / stem
     ├─ CountVectorizer
     └─ MultinomialNB
         └─ مثبت or منفی
```

The Excel path in the script is `./IMDB_Dataset_Persian.xlsx`, so the sheet must sit next to `code.py`.

---

# 📁 Project Structure

```text
User-Sentiment-Analysis/
├── code.py
├── IMDB_Dataset_Persian.xlsx
└── README.md
```

Columns used: `review` and `sentiment`.

---

# 🛠️ Technologies

- Python 3.8+
- pandas
- hazm
- scikit-learn
- openpyxl, for reading `.xlsx`

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/User-Sentiment-Analysis.git
cd User-Sentiment-Analysis
pip install pandas scikit-learn hazm openpyxl
```

---

# ▶️ Usage

```bash
python code.py
```

The script prints a few cleaned rows, the test metrics, and a label for each sample review at the bottom of the file.

---

# 📝 Notes

- The sheet in this repository is a tiny sample, about ten reviews. The score is a demo, not a measured result.
- `neutral` is grouped with the non-positive class.
- Run the script from the repository folder so `./IMDB_Dataset_Persian.xlsx` resolves.
- Do not put a personal absolute path back into `code.py`.

---

# ❓ FAQ

### Is the script connected to the Excel file?

Yes. It loads `./IMDB_Dataset_Persian.xlsx`, and that file is in the repository root.

### Does it detect three classes?

No. Training is binary: positive versus not positive.

### Does it need a GPU?

No.

---

# 📬 Contact

**Developer:**

### Sadra Hatami

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If this classifier is useful as a study sample, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
