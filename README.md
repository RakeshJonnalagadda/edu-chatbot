# Study Buddy AI 🤖

An AI-powered educational chatbot built using Flask and Groq API.
It helps students understand concepts clearly with simple explanations and examples.

---

## 🚀 Features

* AI chatbot focused on education
* Fast responses using Groq (LLaMA 3)
* Clean web interface (ChatGPT-style)
* Supports DBMS, SQL, and core subjects

---

## 🛠️ Tech Stack

* Python (Flask)
* Groq API (LLaMA 3)
* HTML, CSS, JavaScript
* AWS EC2 (Ubuntu)

---

## 📦 Project Setup (Step-by-Step)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/RakeshJonnalagadda/edu-chatbot.git
cd edu-chatbot
```

---

### 2️⃣ Install Python & Create Virtual Environment

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install flask groq python-dotenv
```

---

### 4️⃣ Add API Key

Create `.env` file:

```bash
nano .env
```

Add:

```env
GROQ_API_KEY=your_api_key_here
```

Save:

```
CTRL + X → Y → Enter
```

---

### 5️⃣ Run Application

```bash
python app.py
```

---

### 6️⃣ Open in Browser

* Local machine:

```
http://localhost:5002
```

* AWS EC2:

```
http://your-ec2-public-ip:5002
```

---

## 🧪 Example Questions

* What is SQL?
* Explain DBMS normalization
* What is a primary key?
* What is database?

---

## 📁 Project Structure

```
edu-chatbot/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
```

---

## ⚠️ Important Notes

* Do NOT share your `.env` file
* Do NOT push API keys to GitHub
* Use model:

  ```
  llama-3.1-8b-instant
  ```

---

## 🧠 Troubleshooting

### Port already in use

```bash
sudo pkill -f python
```

### Module not found

```bash
pip install flask groq python-dotenv
```

### API issues

```bash
cat .env
```

---

## 🚀 Future Improvements

* Add chat memory
* Improve UI design
* Add authentication system
* Deploy with Nginx + domain
* Add CI/CD pipeline

---

## 👨‍💻 Author

Rakesh Jonnalagadda

---

## ⭐ Support

If you like this project, give it a star ⭐ on GitHub!
