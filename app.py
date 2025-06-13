from flask import Flask, render_template, request, send_file
from cs_to_vs_snippet import create_vs_snippet
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    cs_code = request.form.get('cs_code', '')
    title = request.form.get('title', '')
    description = request.form.get('description', '')
    shortcut = request.form.get('shortcut', '')
    
    snippet_xml = create_vs_snippet(cs_code, title, description, shortcut)
    
    # 儲存檔案
    filename = f"{shortcut}.snippet"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(snippet_xml)
    
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 