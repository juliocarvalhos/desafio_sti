from main import popula,cr_aluno,cr_curso
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    list_aluno, list_disciplinas, list_notas = popula()
    cr_aluno(list_aluno, list_disciplinas, list_notas)
    cursos = cr_curso(list_disciplinas, list_notas)
    
    alunos = []
    for aluno in list_aluno:
        alunos.append((aluno.matricula,aluno.cr))
    return render_template('lista.html', alunos = alunos, cursos = cursos)

if __name__ == "__main__":
	app.run(debug=True)

