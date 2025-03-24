# 🧠 Emotion Recognition from Natural Images  
### 🖼️ Deep Learning-based Facial Emotion Classification Pipeline  
> End-to-end AI project: From raw data to deployment and explainable insights.

---

## 📌 Project Overview

This project builds a full-stack AI system to classify human facial emotions from natural images using deep learning. The system simulates real-world applications such as:

- Monitoring customer emotions from photos (e.g., social media, reviews)
- Tracking mood in educational or healthcare environments
- Supporting sentiment-aware recommendation systems

The project is designed as a **flagship showcase** for aspiring Data Scientists, featuring a complete ML pipeline with annotation, modeling, evaluation, deployment, and explainability.

---

## 🧠 Problem Statement

> Given a dataset of natural images containing people (Flickr30k), the goal is to detect and classify the dominant facial emotion expressed in each image into one of the following categories:

- 😊 Happy  
- 😢 Sad  
- 😠 Angry  
- 😲 Surprise  
- 😐 Neutral

This is a multi-class image classification task with a real-world edge: data is noisy, expressions are subtle, and images are not studio-quality – making the problem challenging and realistic.

---

## 📂 Dataset

- **Source**: [Flickr30k Dataset](https://shannon.cs.illinois.edu/DenotationGraph/)
- **Size**: ~31,800 JPEG images with accompanying captions
- **Labels**: Emotion annotations generated using the [DeepFace](https://github.com/serengil/deepface) library, including:
  - Dominant emotion
  - Age (estimated)
  - Gender (estimated)
- **Storage**: Images and annotation files are stored on Google Cloud Storage (GCS)

---

## 🧱 Project Architecture / Pipeline

```mermaid
graph TD
    A[Raw Images in GCS] --> B[ETL & Preprocessing]
    B --> C[Emotion Annotation with DeepFace]
    C --> D[Feature Extraction (ResNet50)]
    D --> E[Dataset Creation]
    E --> F[Model Training (MLflow Tracking)]
    F --> G[Evaluation & Explainability (SHAP)]
    G --> H[Deployment on Cloud Run]
    H --> I[Streamlit Dashboard (optional)]
```

---

## 🧼 ETL – Image Preprocessing

Initial preprocessing of ~31k images from Flickr30k:

- Images are resized to 224x224
- Saved to a `processed/` folder on GCS
- Metadata (filename, dimensions, size, etc.) saved in `.csv` and `.parquet`

📒 ETL notebook: [`01_etl_resize.ipynb`](notebooks/01_etl_resize.ipynb)

---

## 📍 Data Annotation – Emotion Tagging via DeepFace

To create emotion labels, we implemented an automated annotation pipeline using [**DeepFace**](https://github.com/serengil/deepface). Each image was analyzed to extract the following metadata:

- `dominant_emotion` 🎭 (e.g., happy, sad, angry, neutral, surprise)
- `age` 🧒🏼 (estimated)
- `gender` 🚻 (estimated)
- `race` 🌍 (estimated)

### ✅ Highlights:
- **Batch-based annotation** for large-scale efficiency  
- **GPU-accelerated** using Colab Pro (GT4) → 10× faster processing  
- **Monitoring enabled**: Pie charts per batch & label drift logs (`label_monitor_log.csv`)  
- **Annotation output** saved in CSV + Parquet formats and pushed to Google Cloud Storage (GCS)

📒 Annotation notebook: [`02_annotate_deepface_batch.ipynb`](notebooks/02_annotate_deepface_batch.ipynb)

---

## 📊 Monitoring & Finalization

A lightweight monitoring module was added to:

- Visualize label distributions across batches
- Detect label drift using CSV logs
- Merge all batch annotations into a final dataset
- Save as `final_emotion_dataset.parquet` and upload to GCS

📒 Monitoring notebook: [`06_data_monitoring_and_finalize.ipynb`](notebooks/06_data_monitoring_and_finalize.ipynb)  
📦 Utilities: [`monitoring_utils.py`](src/monitoring_utils.py)

---

## 📍 Feature Extraction – ResNet50 Embeddings

After annotation, we extract high-level image features using a **pretrained ResNet50** model. Each image is converted into a 2048-dimensional embedding vector representing facial structure, texture, and expression cues.

### 🔧 How it works:
- Images are loaded directly from GCS
- Each image is resized to 224x224 and passed through ResNet50 (avg_pool layer)
- Output vectors are saved as `image_vectors.npy` and uploaded to GCS

### ✅ Highlights:
- 📦 Feature vector dimension: `2048`
- ⚡ Fast inference using GPU (Colab Pro)
- 💾 Features stored in `.npy` format and reused for modeling
- 🔁 Optional integration with t-SNE or clustering later

📒 Feature extraction notebook: [`07_feature_extraction.ipynb`](notebooks/07_feature_extraction.ipynb)

---

## 🛠 Tech Stack

| Layer | Tools & Frameworks |
|------|---------------------|
| Cloud Storage | Google Cloud Storage (GCS) |
| Annotation | DeepFace |
| Feature Extraction | ResNet50 (TensorFlow Keras) |
| Modeling | TensorFlow, Scikit-learn, AutoML (Keras Tuner) |
| Tracking | MLflow |
| Explainability | SHAP |
| Deployment | Flask + Google Cloud Run |
| Dashboard (optional) | Streamlit |
| CI/CD (optional) | GitHub Actions, ArgoCD |

---

## ⚙️ How to Run

1. Clone this repo
2. Set up your GCP credentials and bucket
3. Run the notebooks in order (see `/notebooks`)
4. Train the model and track experiments with MLflow
5. (Optional) Deploy API with Flask on Google Cloud Run

---

## 📊 Results

<!-- TODO: Add model performance metrics, confusion matrix, SHAP plots -->

- Test Accuracy: <!-- fill here -->
- F1-score (macro): <!-- fill here -->
- Confusion Matrix: ✅
- SHAP explanation: ✅

---

## 🎥 Demo

<!-- TODO: Add Streamlit app screenshot or video GIF -->

![Demo Screenshot](path/to/demo_screenshot.png)

---

## 💡 Lessons Learned

- Managing real-world image data is messy – especially with noise and lighting variation.
- Combining transfer learning with emotion estimation yields solid performance.
- SHAP gives excellent insights on model bias and interpretability.

---

## 👨‍💻 Author

**Nguyen Minh Tri**  
_Machine Learning & Data Enthusiast_  
📍 Vietnam → Singapore-ready  
🌐 [LinkedIn](#) | [GitHub](#) | [Email](#)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
