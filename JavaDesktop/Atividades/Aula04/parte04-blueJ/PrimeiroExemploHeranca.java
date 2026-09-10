import java.util.ArrayList;
import java.util.List;

public class PrimeiroExemploHeranca {
    public static void main(String args[]) {

        Aluno aluno = new Aluno(
            Teclado.leInt("Informe a matricula do aluno: "),
            Teclado.leString("Informe o nome do aluno: "),
            Teclado.leString("Informe o login do aluno: "),
            Teclado.leString("Informe a senha do aluno: ")
        );
        aluno.setAv1(Teclado.leDouble("Informe a nota da AV1: "));
        aluno.setAv2(Teclado.leDouble("Informe a nota da AV2: "));

        Professor professor = new Professor(
            Teclado.leInt("Informe a matricula do professor: "),
            Teclado.leString("Informe o nome do Professor: "),
            Teclado.leString("Informe o login do Professor: "),
            Teclado.leString("Informe a senha do Professor: "),
            Teclado.leString("Informe a área de atuação do Professor: ")
        );


        List<Usuario> listaUsuarios = new ArrayList<>();
        listaUsuarios.add(aluno);
        listaUsuarios.add(professor);

        System.out.println("\n=================================");
        System.out.println("EXIBINDO DADOS (USANDO POLIMORFISMO)");
        System.out.println("=================================");

        for (Usuario u : listaUsuarios) {
        
            u.exibeDados();

            boolean logado = u.autenticar(u.getLogin(), u.getSenha());
            System.out.println("Status de Autenticação: " + (logado ? "Sucesso" : "Falha"));
        }
    }
}