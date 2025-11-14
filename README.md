
# Financial Data Extractor

This project builds a **Financial Data Extraction** system that converts unstructured financial paragraphs into structured metrics.  
It extracts key values such as **Actual Revenue, Expected Revenue, Actual EPS, and Expected EPS** using **LangChain, Groq, and Llama-3.3-70B**, and presents them in a clean table using **Streamlit**.

---

## 📸 Live Demo (Optional)

*If you deploy the Streamlit app, you can add the link here.*  
Example:

**Live App:** https://your-streamlit-app-url.streamlit.app/

---

## 🖥️ Streamlit Interface

*(Add your interface image here if needed)*  
Example:

![App Screenshot](https://github.com/yourusername/yourrepo/blob/main/screenshot.png)

---

## 📌 Project Objective

To design a simple, accurate, and user-friendly system that:

- Extracts **revenue (actual & estimated)** and **EPS (actual & estimated)** from any financial report text  
- Uses **LLM-based text understanding** to analyze financial paragraphs  
- Converts unstructured text into **clean tabular output**  
- Provides a minimal **Streamlit UI** suitable for financial analysts and researchers

---

## ⚙️ Working Methodology & Steps Performed

### **1. Text Input (Streamlit UI)**

- Users paste any financial paragraph into a text box.
- Clicking **Extract** sends the text to the backend.
- Basic validation prevents empty input.

---

### **2. Prompt Construction (LangChain)**

A structured prompt instructs the model to extract four keys:

- `revenue_actual`
- `revenue_expected`
- `eps_actual`
- `eps_expected`

The prompt enforces:

- Strict JSON format  
- Units required (billion, million, etc.)  
- No text aside from JSON  

---

### **3. LLM Processing (Groq: Llama-3.3-70B)**

- The prompt and user text are processed by Groq’s high-speed Llama-3.3-70B.
- The model identifies revenue/EPS values from the paragraph.
- The model returns the information in JSON format.

---

### **4. JSON Parsing & Validation**

Using LangChain’s `JsonOutputParser`:

- Ensures the model's response is valid JSON.
- Extracts the required keys safely.
- Raises a user-friendly error if JSON is invalid:
  - “Context too big, Unable to parse.”

---

### **5. Output Formatting (Pandas + Streamlit)**

- Extracted values are structured into a pandas DataFrame:

```
Measure | Estimated | Actual
Revenue | value     | value
EPS     | value     | value
```

- Streamlit displays the table in an easy-to-read format.

---

## 🗂️ Project Structure

```
financial-data-ex/
│
├── main.py                # Streamlit UI
├── data_extractor.py      # LLM extraction logic
├── requirements.txt       # Dependencies
├── .env                   # Groq API key (not included in repo)
└── README.md
```

---

## 🔧 Installation & Setup

### **1. Clone the repository**
```
git clone https://github.com/prabalpkd/financial-data-ex
cd financial-data-ex
```

### **2. Install dependencies**
```
pip install -r requirements.txt
```

### **3. Configure API key**
Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

```
streamlit run main.py
```

Open in your browser:

```
http://localhost:8501
```

---

## 📝 Example Input

```
Apple reported revenue of $102.47 billion for the quarter, beating analyst expectations of $102.24 billion. 
EPS came in at 1.85 compared to an expected 1.77.
```

### **Output**

| Measure | Estimated | Actual |
|---------|-----------|--------|
| Revenue | 102.24B   | 102.47B |
| EPS     | 1.77      | 1.85    |

---

## 📥 Inputs

- Any financial paragraph such as:  
  - Earnings reports  
  - Quarterly summaries  
  - Financial news articles  
  - Company announcements  

---

## 📤 Outputs

- Actual Revenue  
- Expected Revenue  
- Actual EPS  
- Expected EPS  
- A structured results table  

---

## 🚀 Future Enhancements

- Extraction for more financial metrics (Net Income, Operating Income, Margins)
- Support for PDF uploads  
- Batch processing  
- Charts comparing actual vs. expected values  
- Caching for repeated extraction  

---

## 👤 Author

**Prabal Kumar Deka**
