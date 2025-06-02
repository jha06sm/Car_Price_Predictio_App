# 🚗 Car Price Prediction App

This is a web application built using **Streamlit** and a **Random Forest Regressor** model that predicts the selling price of a used car based on various features like company, year, kilometers driven, and fuel type.

---

## 🔍 Features

- Predict the price of a used car using machine learning
- Cleaned and preprocessed dataset from **Quikr Cars**
- Interactive UI with dropdowns and numeric inputs
- Visualizes feature importance
- Deployable via [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧠 Model Details

- **Algorithm**: Random Forest Regressor  
- **Training Features**:
  - `company`
  - `year`
  - `kms_driven`
  - `fuel_type`
  - `age`
- **Target**: `Price`

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Train the model (optional if model.pkl is provided)
bash
Copy
Edit
python train_model.py
4. Run the app
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
car-price-predictor/
│
├── quikr_car.csv           # Raw dataset
├── app.py                  # Streamlit application
├── train_model.py          # Model training script
├── model.pkl               # Trained ML model
├── company_encoder.pkl     # Label encoder for company
├── fuel_type_encoder.pkl   # Label encoder for fuel_type
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
🔧 Dependencies
nginx
Copy
Edit
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
joblib
You can install them with:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Deployment
You can deploy this app on Streamlit Cloud:

Push the project to a GitHub repository.

Go to streamlit.io/cloud and sign in.

Click "New App" and link your GitHub repo.

Select app.py as the main file and deploy.

📧 Contact
Created by Satyam Jha
Feel free to reach out or contribute to the project!










