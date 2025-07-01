# 🔥 Fire-Wheather-Predictor

A machine learning web application that predicts the **Fire Weather Index (FWI)** using meteorological data. Built using **Flask**, with a **Ridge Regression** model selected after cross-validation. Ready for deployment on **AWS Elastic Beanstalk**.

---

## 📌 Features

- Accepts multiple weather input features via a simple web form  
- Uses `StandardScaler` + `Ridge Regression` for prediction  
- Clean and minimal frontend using HTML + Jinja2 templating  
- Scalable and cloud-deployable using AWS Elastic Beanstalk  

---

## 📊 Input Features

The model expects the following 9 features:

- `Temperature` (°C)  
- `RH` – Relative Humidity (%)  
- `Ws` – Wind Speed (km/h)  
- `Rain` (mm)  
- `FFMC` – Fine Fuel Moisture Code  
- `DMC` – Duff Moisture Code  
- `ISI` – Initial Spread Index  
- `Classes` – Fire class encoding  
- `Region` – Categorical region encoding  

---

## 🚀 Tech Stack

| Layer        | Tool                          |
|--------------|-------------------------------|
| ML Model     | Ridge Regression (`sklearn`)  |
| Preprocessing| StandardScaler                |
| Backend      | Flask                         |
| Frontend     | HTML + CSS (Jinja2)           |
| Deployment   | AWS Elastic Beanstalk (planned) |
| Language     | Python                        |

---

## 🧪 How to Run Locally

1. **Clone the repo:**

    ```bash
    git clone https://github.com/<your-username>/Fire-Wheather-Predictor.git
    cd Fire-Wheather-Predictor
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app:**

    ```bash
    python application.py
    ```

4. **Open your browser at:**

    [http://127.0.0.1:5000/predictdata](http://127.0.0.1:5000/predictdata)

---

✅ Don’t forget to replace `<your-username>` with your actual GitHub username in the clone URL.
