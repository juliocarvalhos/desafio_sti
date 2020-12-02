#Classe aluno
class aluno:
    def __init__(self, matricula):
        self.__matricula = matricula
        self.__cr = 0
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def cr(self):
        return self.__cr
    
    @cr.setter
    def cr(self, cr):
        self.__cr = cr
        
        
#Classe disciplina
class disciplina:
    def __init__(self, cod_disciplina, cod_curso, carga_horaria):
        self.__cod_disciplina = cod_disciplina
        self.__cod_curso = cod_curso
        self.__carga_horaria = carga_horaria
        
    @property
    def cod_disciplina(self):
        return self.__cod_disciplina
    
    @property
    def cod_curso(self):
        return self.__cod_curso
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria

#Classe notas
class notas:
    def __init__(self, aluno, disciplina, ano_semestre, nota):
        self.aluno = aluno
        self.disciplina = disciplina
        self.ano_semestre = ano_semestre
        self.nota = nota

import pandas as pd

url_notas = 'https://raw.githubusercontent.com/sti-uff/trabalhe-conosco/master/datasets/notas.csv'
df_notas = pd.read_csv(url_notas)

#Função para criar os objetos de cada classe de acordo com o conjunto de dados
def popula():
    #Cria objetos aluno
    matriculas = df_notas['MATRICULA'].drop_duplicates()
    list_aluno = []
    for mat in matriculas:
        list_aluno.append(aluno(mat))

    #Cria objetos disciplina
    disciplinas = df_notas.drop_duplicates(subset=['COD_DISCIPLINA'])
    list_disciplinas = []
    for index, row in disciplinas.iterrows():
        list_disciplinas.append(disciplina(row['COD_DISCIPLINA'], row['COD_CURSO'], row['CARGA_HORARIA']))

    #Cria objetos notas
    list_notas = []
    for index, row in df_notas.iterrows():

        for list in list_aluno:
            if row['MATRICULA'] == list.matricula:
                aux_aluno = list


        for list in list_disciplinas:
            if row['COD_DISCIPLINA'] == list.cod_disciplina:
                aux_disc = list


        list_notas.append(notas(aux_aluno, aux_disc, row['ANO_SEMESTRE'], row['NOTA']))
    return list_aluno, list_disciplinas, list_notas

#Função pra calcular e printar o cr dos alunos
def cr_aluno(list_aluno, list_disciplinas, list_notas):
    print('------- O CR dos alunos é: --------')
    for list_a in list_aluno:
        soma_cr_aluno = 0
        soma_carga = 0
        for list_n in list_notas:
            if list_a == list_n.aluno:
                for list_d in list_disciplinas:
                    if list_d == list_n.disciplina:
                        soma_cr_aluno += (list_n.nota * list_d.carga_horaria)
                        soma_carga += list_d.carga_horaria
                        list_a.cr = round(soma_cr_aluno/soma_carga)
        print(str(list_a.matricula)+ '  -  ' +str(list_a.cr))
    print('-----------------------------------')

#Função pra calcular e printar a media dos cursos
def cr_curso(list_disciplinas, list_notas):
    cursos = []
    for list_d in list_disciplinas:
        cursos.append(list_d.cod_curso)

    cursos_sem_duplicatas = [*dict.fromkeys(cursos)]
    cursos_ordem = sorted(cursos_sem_duplicatas)

    print('----- Média de CR dos cursos ------')
    list_cr_curso = []
    for list_c in cursos_ordem:
        soma_cr_curso = 0
        qtd_alunos = 0
        for list_n in list_notas:
            if list_c == list_n.disciplina.cod_curso:
                soma_cr_curso += list_n.aluno.cr
                qtd_alunos += 1
        list_cr_curso.append((list_c, round(soma_cr_curso/qtd_alunos)))

    for list in list_cr_curso:
        print(str(list[0]) + ' - ' + str(list[1]))
    print('-----------------------------------')

    return list_cr_curso

def main():
    list_aluno, list_disciplinas, list_notas = popula()
    cr_aluno(list_aluno, list_disciplinas, list_notas)
    cr_curso(list_disciplinas, list_notas)
    
if __name__ == "__main__":
    main()