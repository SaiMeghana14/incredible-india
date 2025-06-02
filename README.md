# 🇮🇳 Incredible India – Cultural Explorer 🌏

A Streamlit web app that showcases India's rich cultural heritage – festivals, food, monuments, and more – powered by **Snowflake** as the backend and hosted on **Streamlit Cloud**.

<br/>

## 🔥 Live Demo

🔗 [Click here to try the live app](https://your-streamlit-cloud-url)  
(*replace with your actual URL*)

<br/>

## 🎯 Features

- 🌐 Explore India's diverse states and their culture
- 🏛️ Monuments, 🎉 Festivals, 🍲 Food – all in one app
- 📡 Real-time data fetched from **Snowflake**
- 🧑‍💻 Beginner-friendly, hosted entirely online
- 🪄 Easy to extend – just add rows to the Snowflake table!

<br/>

## 📦 Tech Stack

| Tool       | Role                    |
|------------|-------------------------|
| Streamlit  | Frontend Web UI         |
| Snowflake  | Cloud Database Backend  |
| GitHub     | Version Control         |
| Streamlit Cloud | App Deployment     |

<br/>

## 🚀 Setup Instructions

### 🔧 Local Setup (Optional)

> If you're a beginner, skip this and go to the **Deploy to Streamlit Cloud** section below.

1. Install Python 3.10+  
2. Install dependencies:
   ```bash
   pip install streamlit snowflake-connector-python
   ```

3. Add your Snowflake credentials to `.streamlit/secrets.toml`:
   ```toml
   [snowflake]
   user = "your_username"
   password = "your_password"
   account = "your_account.region"
   warehouse = "COMPUTE_WH"
   database = "INDIA_CULTURE"
   schema = "PUBLIC"
   ```

4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

---

### ☁️ Deploy to Streamlit Cloud (Recommended)

1. **Fork or Clone** this repo to your GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New App"**
4. Select your repo and set the main file as `streamlit_app.py`
5. Add your Snowflake secrets under **Settings → Secrets**:
   ```toml
   [snowflake]
   user = "your_username"
   password = "your_password"
   account = "your_account.region"
   warehouse = "COMPUTE_WH"
   database = "INDIA_CULTURE"
   schema = "PUBLIC"
   ```
6. Click **Deploy** 🚀

---

## 🗃️ Snowflake Table Schema

```sql
CREATE OR REPLACE TABLE explorer (
  state STRING,
  category STRING,
  name STRING,
  description STRING,
  image_url STRING
);
```

### 🧪 Sample Data

```sql
INSERT INTO explorer VALUES
('Tamil Nadu', 'Festival', 'Pongal', 'A harvest festival.', 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Pongal_Festival_Tamil_Nadu.jpg'),
('Rajasthan', 'Food', 'Dal Baati Churma', 'Traditional dish.', 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Dal-Bati-Churma.jpg'),
('Uttar Pradesh', 'Monument', 'Taj Mahal', 'Mughal architecture.', 'https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg');
```

---

## ✨ Screenshots

> Add here later if needed (or use markdown image tags)

---

## 💡 Ideas for Extensions

- Add a search bar by culture type or keyword
- Add maps or regional filters
- Upload CSV to update the Snowflake table dynamically

---

## 🙋‍♀️ Who Can Use This?

- 🇮🇳 Indian cultural enthusiasts
- 🧑‍🎓 Hackathon beginners learning Streamlit + Snowflake
- 🖥️ Web devs wanting to demo a data-driven app

---

## 📄 License

MIT License © 2025 [Sai Meghana]

---

## 🌟 Made with ❤️ for the **Snowflake Our Hero Hackathon 2025**
