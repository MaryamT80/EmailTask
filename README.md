# 📩 Email Simulator

## 🚀 Overview  
This is a simple **Email Simulator** written in Python. It allows you to simulate reading and managing emails through a menu-driven interface.

---

## 🌟 Features  
✅ Create and store sample emails in an inbox  
✅ List all available emails  
✅ Read emails and mark them as read  
✅ View only unread emails  

---

## 🏗️ Structure  
The program defines an `Email` class with the following attributes:  
- **email_address** – Sender's email address  
- **subject_line** – Email subject  
- **email_content** – Content of the email  
- **has_been_read** – Status indicating whether the email has been read  

---

## 💻 How to Run  
1. **Clone the repository**:  
```bash
git clone https://github.com/your-username/your-repo.git
```

2. **Navigate to the project directory**:  
```bash
cd your-repo
```

3. **Run the program**:  
```bash
python email.py
```

---

## 📖 Usage  
When you run the program, the following menu will appear:  
```
Email Simulator Menu:
1. Read an email
2. View unread emails
3. Quit application
```
- **Read an email** – Select an email by its index to read and mark it as read.  
- **View unread emails** – Display a list of unread emails.  
- **Quit application** – Exit the simulator.  

---

## ✨ Example  
**Sample Output:**  
```
Inbox:
0 Welcome to HyperionDev!
1 Great work on the bootcamp!
2 Your excellent marks!

Enter the index of the email you want to read: 1

From: user2@example.com
Subject: Great work on the bootcamp!
Content: Keep up the excellent progress!
Email from user2@example.com marked as read.
```

---

## 📝 License  
This project is licensed under the **MIT License**.
