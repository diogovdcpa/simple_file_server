import os
from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory

UPLOAD_FOLDER = '/root/downloads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>File Server</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-slate-900 to-slate-800 min-h-screen text-gray-200">

    <div class="max-w-5xl mx-auto py-12 px-6">
        
        <div class="mb-10 text-center">
            <h1 class="text-4xl font-bold text-white mb-2">📂 File Server</h1>
            <p class="text-gray-400">Gerencie seus arquivos de forma simples e elegante</p>
        </div>

        <div class="bg-slate-800 shadow-2xl rounded-2xl p-6 border border-slate-700">
            
            <h2 class="text-xl font-semibold mb-6 text-white">Arquivos disponíveis</h2>

            <div class="space-y-4">
                {% for file in files %}
                <div class="flex items-center justify-between bg-slate-900 hover:bg-slate-700 transition rounded-xl px-5 py-4 border border-slate-700">
                    
                    <div class="flex items-center space-x-3">
                        <div class="text-2xl">📄</div>
                        <span class="font-medium text-gray-200">{{ file }}</span>
                    </div>

                    <div class="flex space-x-3">
                        <a href="/download/{{ file }}" 
                           class="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg text-sm font-medium transition">
                           Download
                        </a>

                        <a href="/delete/{{ file }}" 
                           class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg text-sm font-medium transition">
                           Excluir
                        </a>
                    </div>
                </div>
                {% endfor %}

                {% if not files %}
                <div class="text-center text-gray-400 py-10">
                    Nenhum arquivo encontrado.
                </div>
                {% endif %}
            </div>

        </div>

        <div class="mt-10 bg-slate-800 shadow-xl rounded-2xl p-6 border border-slate-700">
            <h2 class="text-xl font-semibold mb-4 text-white">⬆ Upload de novo arquivo</h2>

            <form method="post" action="/upload" enctype="multipart/form-data"
                  class="flex flex-col md:flex-row items-center gap-4">

                <input type="file" name="file" required
                       class="block w-full text-sm text-gray-300
                              file:mr-4 file:py-2 file:px-4
                              file:rounded-lg file:border-0
                              file:text-sm file:font-semibold
                              file:bg-indigo-500 file:text-white
                              hover:file:bg-indigo-600
                              bg-slate-900 border border-slate-700
                              rounded-lg p-2">

                <button type="submit"
                        class="bg-indigo-500 hover:bg-indigo-600 text-white px-6 py-2 rounded-lg font-medium transition w-full md:w-auto">
                    Enviar Arquivo
                </button>
            </form>
        </div>

        <div class="mt-10 text-center text-sm text-gray-500">
            • Flask File Server
        </div>

    </div>

</body>
</html>
"""

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(TEMPLATE, files=files)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
