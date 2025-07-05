<p align="center">
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-webapp-grey?logo=flask"></a>
  <img src="https://img.shields.io/badge/WEB%20APP-black?style=flat-square">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg"></a>
</p>

# 🚩 VulnDump

**VulnDump** is an extensible vulnerability & exploitation knowledgebase web application, built with Flask, designed for pentesters, CTF players, red teamers, and security researchers.

> **Quickly search, filter, and explore hundreds of real attack vectors, enumeration commands, payloads, and post-exploitation techniques by target, tech stack, or attack phase.**

![Screenshot](https://i.ibb.co/S7Pcpvp7/Screenshot-2025-07-05-180150.png)

---

## ✨ Features

- **🔎 Fast, Filtered Search:**  
  Find techniques by target (e.g. WordPress, Joomla), phase (Recon, Exploitation, Persistence, etc), tool, or keyword.

- **📝 Rich Knowledgebase:**  
  300+ real-world commands & attack vectors for web, network, post-exploitation, enumeration, and more.

- **🌐 Simple Web UI:**  
  Clean, intuitive interface with search term highlighting and instant filter reset.

- **🗂️ Extensible CSV Backend:**  
  Easily expand or update the technique database by editing a single CSV file.

- **🖱️ Command Details:**  
  Click any entry for full usage info and copy-paste ready commands.

- **🛠️ Self-Hosted:**  
  Run locally or on the cloud (PythonAnywhere, etc). Lightweight and easy to deploy.

---

## 🚀 Live Demo

See it in action:  
**[https://vulndump.pythonanywhere.com/](https://vulndump.pythonanywhere.com/)**

---

## ⚡ Getting Started

### **Prerequisites**
- Python 3.8+  
- Flask

### **Installation**
```bash
git clone https://github.com/yourusername/VulnDump.git
cd VulnDump
pip install -r requirements.txt
