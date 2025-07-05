from flask import Flask, render_template, request
import sqlite3
import os
import csv

app = Flask(__name__)

DB_PATH = 'vulndump.db'
CSV_PATH = 'VulnDump_Vectors.csv'

# ------------------ DB INIT ------------------
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''CREATE TABLE attack_library (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        target_type TEXT,
                        subtype TEXT,
                        phase TEXT,
                        tool TEXT,
                        command TEXT,
                        notes TEXT
                    )''')

        # Load data from CSV if exists
        if os.path.exists(CSV_PATH):
            with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                data = [(row['target_type'], row['subtype'], row['phase'], row['tool'], row['command'], row['notes']) for row in reader]
                c.executemany('''INSERT INTO attack_library (target_type, subtype, phase, tool, command, notes)
                                 VALUES (?, ?, ?, ?, ?, ?)''', data)

        conn.commit()
        conn.close()

# ------------------ ROUTES ------------------
@app.route('/')
def index():
    target = request.args.get('target_type', '')
    phase = request.args.get('phase', '')
    subtype = request.args.get('subtype', '')
    search_query = request.args.get('q', '')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    query = "SELECT * FROM attack_library WHERE 1=1"
    params = []

    if target:
        query += " AND target_type = ?"
        params.append(target)
    if phase:
        query += " AND phase = ?"
        params.append(phase)
    if subtype:
        query += " AND subtype = ?"
        params.append(subtype)
    if search_query:
        query += " AND (LOWER(tool) LIKE ? OR LOWER(notes) LIKE ?)"
        params.extend([f"%{search_query.lower()}%", f"%{search_query.lower()}%"])


    c.execute(query, params)
    entries = c.fetchall()

    if target:
        c.execute("SELECT DISTINCT subtype FROM attack_library WHERE target_type=?", (target,))
        all_subtypes = [row[0] for row in c.fetchall()]
    else:
        c.execute("SELECT DISTINCT subtype FROM attack_library")
        all_subtypes = [row[0] for row in c.fetchall()]

    conn.close()
    return render_template('index.html', entries=entries, 
                           target_type=target, phase=phase, 
                           subtype=subtype, subtypes=all_subtypes,
                           q=search_query)

@app.route('/entry/<int:entry_id>')
def entry_detail(entry_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM attack_library WHERE id = ?", (entry_id,))
    entry = c.fetchone()
    conn.close()
    return render_template('entry_detail.html', entry=entry)

# ------------------ MAIN ------------------
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

