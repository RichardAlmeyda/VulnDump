**VulnDump**
VulnDump is an extensible vulnerability & exploitation knowledgebase web application, built with Flask, designed for pentesters, CTF players, and security researchers. It allows you to search, filter, and explore hundreds of real attack vectors, post-exploitation techniques, enumeration commands, and payloads by target type, technology, or phase.

![img77](https://i.ibb.co/S7Pcpvp7/Screenshot-2025-07-05-180150.png)

Features

🔎 Fast, Filtered Search: Find techniques by target (e.g., WordPress, Joomla), phase (Recon, Exploitation, Persistence, etc), tool, or keywords.

📝 Rich Knowledgebase: 300+ real-world commands and techniques for web apps, networks, post-exploitation, enumeration, and more.

🌐 Simple Web UI: Clean interface, supports search term highlighting and quick filter reset.

🗂️ Extensible CSV Backend: Easily update, expand, or automate the technique database using a simple CSV file.

🖱️ Technique Details: Click any entry for detailed usage info and copy-paste ready commands.

🛠️ Self-hosted: Easily run locally or on a cloud host like PythonAnywhere.

================
Demo
You can see a live demo here:
https://vulndump.pythonanywhere.com/

===============
Getting Started

Prerequisites Python 3.8+ , Flask , (Optional) A PythonAnywhere account for cloud deployment or any cloud
==============
**Installation**

--> git clone https://github.com/yourusername/VulnDump.git

--> cd VulnDump

--> pip install -r requirements.txt

**Running Locally**

python app.py
Open http://localhost:5000 in your browser.

============

**Usage**
Use the dropdowns to filter by Target Type, Subtype (e.g., CMS), and Phase.

Use the search box to find any command, tool, or keyword.

Click “Reset Filters” to clear all selections and show everything.

Click on any entry for detailed command syntax and notes.

Data Structure
The app reads its data from a CSV file with the following columns:

==================
...
Update VulnDump_Vectors.csv to expand the database.
On first run, the CSV will be imported to an SQLite DB automatically.

Customization
Add Techniques: Edit or append to VulnDump_Vectors.csv.

UI: Customize templates/index.html and static/style.css for your preferred look.

Deployment: Works on PythonAnywhere, local Linux, or any Flask-compatible host.
=================

License
MIT License.
© 2025 by RichardAlmeyda




