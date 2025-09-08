# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built with **Python, Streamlit, and Machine Learning**.  
It recommends similar movies based on user selection using pre-computed similarity scores.

---
## 🌍 Live Demo
🔗 https://movierecommendationsystem-bs8jrrhvtfzcw3wjqt5kun.streamlit.app/
---

## 🚀 Features
- Recommends top similar movies based on content similarity.
- Content-based recommendation using text similarity.
- Preprocessing of Netflix dataset (cleaning, handling missing values).
- TF–IDF Vectorization for feature extraction.
- Cosine similarity for recommendation.
- Jupyter Notebook implementation for easy experimentation.
- Uses **TMDB API** and **OMDB API** to fetch posters.

---

## 🛠️ Tech Stack
- Python 🐍
- **Pandas** (data handling)
- **NumPy** (numerical computation)
- **Scikit-learn** (TF–IDF & cosine similarity)
- **Pickle** (to load model files)
- **Jupyter Notebook** (experimentation & visualization)
- **Streamlit** (for frontend deployment)
- **TMDB & OMDB APIs** (for posters & movie data)

---

## 📂 Project Structure
Movie_Recommendation_system/
│── app.py # Main Streamlit app
│── movie_dict.pkl # Dictionary of movies
│── similarity.pkl # Precomputed similarity matrix (stored via Git LFS)
│── requirements.txt # Python dependencies
│── README.md # Project documentation

---


---

## ⚙️ Setup Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Movie_Recommendation_system.git
cd Movie_Recommendation_system
pip install -r requirements.txt
streamlit run app.py
```

----

🔑 API Keys Setup (for TMDB & OMDB)

This project uses Streamlit Secrets to store API keys securely.

- In Streamlit Cloud, go to App → Settings → Secrets.

- Add your keys in TOML format:
```
API_KEY = "0361c880dff8292ad595e26765c54f45"
OMDB_KEY = "62c1f87c"
```
- In app.py, access them as:
  ```
  import streamlit as st

  API_KEY = st.secrets["API_KEY"]
  OMDB_KEY = st.secrets["OMDB_KEY"]
  ```

---

👨‍💻 Author

Gaurav Sinha

  
