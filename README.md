# emotion-recognition-pipeline
---

```markdown
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

<!-- TODO: Add setup instructions, Colab link, requirements.txt -->

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
```

---

## ✅ Hướng dẫn sử dụng
- Bạn hãy:
  - **Copy toàn bộ nội dung trên vào file `README.md` trong repo GitHub**
  - Cập nhật các phần `<!-- TODO -->` khi có kết quả.
  - Thêm ảnh minh họa, metric thật khi hoàn tất từng giai đoạn.
- Đừng quên gắn sao ⭐ nếu bạn muốn người khác tìm được project của bạn sau này.

---

Bạn có muốn mình:
- ✅ Viết thêm template `requirements.txt`?
- ✅ Viết luôn 1 notebook mẫu đầu tiên `01_etl_images_gcs.ipynb` để bạn bắt tay làm?

Bạn chọn bước tiếp theo nhé! Mình theo bạn tới cùng 🚀
