# 📄 Resume Matcher

A simple Streamlit web app that compares your **resume (PDF)** with a **job description** and shows how well your skills match. It gives a skill-match percentage, a match rating, and lists of **matched** and **missing** skills so you know what to add or improve.
---

## 🚀 Features

- Upload your resume in **PDF** format
- Paste any job description
- Skill match percentage with a progress bar
- Match rating: **Strong**, **Average** or **Weak**
- Shows **matched skills** and **missing skills**
- Accurate whole-word skill detection using regex (e.g. `java` will not match `javascript`)

## 🧠 How It Works

1. The text is extracted from the uploaded PDF resume using **PyPDF2**.
2. The resume and job description are converted to lowercase.
3. The app checks which skills from a predefined skill list appear in each text.
4. **Skill Match %** = (skills found in both) ÷ (skills required in the job description) × 100
5. The result is shown with a rating:

| Skill Match | Result |
|-------------|--------|
| 70% and above | ✅ Strong Match |
| 40% – 69% | ⚠️ Average Match |
| Below 40% | ❌ Weak Match |

The app also calculates TF-IDF + cosine similarity between the resume and job description for overall text similarity.

## 🛠️ Tech Stack

- **Python**
- **Streamlit**: web interface
- **PyPDF2**: PDF text extraction
- **scikit-learn**: TF-IDF and cosine similarity
- **re (regex)**: skill matching

## 🎯 Skills Currently Supported

`python`, `java`, `sql`, `machine learning`, `data analysis`, `html`, `css`, `git`, `django`, `flask`, `pandas`, `numpy`, `aws`, `excel`, `power bi`, `tableau`, `mysql`, `c++`, `react`, `communication`, `teamwork`, `problem solving`

You can add more by editing the `skills` list in `app.py`.

## 📂 Project Structure

```
resume-matcher/
│
├── app.py              # Main Streamlit application
└── README.md
```

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/resume-matcher.git
cd resume-matcher

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

**requirements.txt**

```
streamlit
PyPDF2
scikit-learn
```

## ▶️ Usage

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser, then:

1. Upload your resume (PDF)
2. Paste the job description
3. Click **Match Resume with Job Description**
4. View your skill match, rating, and missing skills

## 📊 Example Output

```
Skill Match: 75%
Strong Match

Matched Skills: python, sql, pandas
Missing Skills: aws
```

## 📸 Screenshots

Add your screenshots here:

```
![Home](screenshots/home.png)
![Result](screenshots/result.png)
```

## ⚠️ Limitations

- Works only with text-based PDFs (scanned/image PDFs are not supported)
- Only detects skills from the predefined list

## 🔮 Future Improvements

- Show the overall TF-IDF similarity score in the results
- Support DOCX and TXT resumes
- Automatically extract skills using NLP (spaCy)
- Semantic matching with Sentence Transformers / BERT
- Rank multiple resumes against one job description
- Deploy online using Streamlit Cloud

## 🤝 Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push the branch (`git push origin feature-name`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License.

## 👤 Author

**Your Name**
- GitHub: [@K.Manoharan](https://github.com/your-username)
- LinkedIn: [K.Manoharan]linkedin.com/in/manoharan-k-9928b1418)

---

⭐ If you like this project, give it a star!
