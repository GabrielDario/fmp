public class ListaDeAlunos {

    private Aluno[] alunos;
    private int quantidade;

    public ListaDeAlunos(int tamanho) {
        alunos = new Aluno[tamanho];
        quantidade = 0;
    }

    public boolean adicionarAluno(Aluno aluno) {

        if (quantidade < alunos.length) {
            alunos[quantidade] = aluno;
            quantidade++;

            return true;
        }

        return false;
    }

    public Aluno verificarAluno(int codigo) {

        for (int i = 0; i < quantidade; i++) {

            if (alunos[i].getCodigo() == codigo) {
                return alunos[i];
            }
        }

        return null;
    }

    public void exibirLista() {

        if (quantidade == 0) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }

        for (int i = 0; i < quantidade; i++) {

            System.out.println("----------------------");
            alunos[i].exibeDados();
        }
    }

    public void listarAlunosDoCurso(Curso curso) {

    for (int i = 0; i < quantidade; i++) {

        if (alunos[i].getCurso() == curso) {

            System.out.println(
                "- " + alunos[i].getNome()
            );
        }
    }
}
}