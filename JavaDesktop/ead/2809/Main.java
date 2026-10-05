import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        ListaDeAlunos listaAlunos = new ListaDeAlunos(100);
        Curso[] cursos = new Curso[50];
        int quantidadeCursos = 0;

        int opcao;

        do {

            System.out.println("\n================================");
            System.out.println("       SISTEMA ACADÊMICO");
            System.out.println("================================");
            System.out.println("1 - Cadastrar aluno");
            System.out.println("2 - Cadastrar aluno bolsista");
            System.out.println("3 - Listar alunos");
            System.out.println("4 - Cadastrar cursos");
            System.out.println("5 - listar cursos");
            System.out.println("6 - Associar aluno a curso");
            System.out.println("7 - Listar curso com aluno");
            System.out.println("8 - Lançar notas");
            System.out.println("9 - Consultar notas");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {

                case 1:
                    cadastrarAluno(scanner, listaAlunos);
                    break;

                case 2:
                    cadastrarBolsista(scanner, listaAlunos);
                    break;

                case 3:
                    listaAlunos.exibirLista();
                    break;

                case 4:
                    quantidadeCursos = cadastrarCurso(
                            scanner,
                            cursos,
                            quantidadeCursos);
                    break;

                case 5:
                    listarApenasCursos(cursos, quantidadeCursos);
                    break;

                case 6:
                    associarAlunoCurso(
                            scanner,
                            listaAlunos,
                            cursos,
                            quantidadeCursos);
                    break;
                case 7:
                    listarCursos(
                            cursos,
                            quantidadeCursos,
                            listaAlunos);
                    break;
                case 8:
                    lancarNotas(scanner, listaAlunos);
                    break;

                case 9:
                    consultarNotas(scanner, listaAlunos);
                    break;

                case 0:
                    System.out.println("Sistema encerrado.");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }

        } while (opcao != 0);

        scanner.close();
    }

    public static void cadastrarAluno(Scanner scanner, ListaDeAlunos listaAlunos) {

        System.out.println("\n=== CADASTRAR ALUNO ===");

        System.out.print("Código: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Nome: ");
        String nome = scanner.nextLine();

        System.out.print("Data de nascimento: ");
        String dataNascimento = scanner.nextLine();

        System.out.print("E-mail: ");
        String email = scanner.nextLine();

        System.out.print("Senha: ");
        String senha = scanner.nextLine();

        Aluno aluno = new Aluno(
                codigo,
                nome,
                dataNascimento,
                email,
                senha);

        if (listaAlunos.adicionarAluno(aluno)) {
            System.out.println("Aluno cadastrado com sucesso!");
        } else {
            System.out.println("Não foi possível cadastrar o aluno.");
        }
    }

    public static void cadastrarBolsista(
            Scanner scanner,
            ListaDeAlunos listaAlunos) {

        System.out.println("\n=== CADASTRAR ALUNO BOLSISTA ===");

        System.out.print("Código: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Nome: ");
        String nome = scanner.nextLine();

        System.out.print("Data de nascimento: ");
        String dataNascimento = scanner.nextLine();

        System.out.print("E-mail: ");
        String email = scanner.nextLine();

        System.out.print("Senha: ");
        String senha = scanner.nextLine();

        System.out.print("Tipo de bolsa: ");
        String tipoBolsa = scanner.nextLine();

        AlunoBolsista bolsista = new AlunoBolsista(
                codigo,
                nome,
                dataNascimento,
                email,
                senha,
                tipoBolsa);

        if (listaAlunos.adicionarAluno(bolsista)) {
            System.out.println("Aluno bolsista cadastrado com sucesso!");
        } else {
            System.out.println("Não foi possível cadastrar o bolsista.");
        }
    }

    public static int cadastrarCurso(
            Scanner scanner,
            Curso[] cursos,
            int quantidadeCursos) {

        System.out.println("\n=== CADASTRAR CURSO ===");

        if (quantidadeCursos >= cursos.length) {
            System.out.println("Limite de cursos atingido.");
            return quantidadeCursos;
        }

        System.out.print("Código do curso: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Nome do curso: ");
        String nome = scanner.nextLine();

        System.out.print("Duração em semestres: ");
        int duracao = scanner.nextInt();
        scanner.nextLine();

        Curso curso = new Curso(codigo, nome, duracao);

        cursos[quantidadeCursos] = curso;
        quantidadeCursos++;

        System.out.println("Curso cadastrado com sucesso!");

        return quantidadeCursos;
    }

    public static void associarAlunoCurso(
            Scanner scanner,
            ListaDeAlunos listaAlunos,
            Curso[] cursos,
            int quantidadeCursos) {

        System.out.println("\n=== ASSOCIAR ALUNO AO CURSO ===");

        System.out.print("Código do aluno: ");
        int codigoAluno = scanner.nextInt();

        Aluno aluno = listaAlunos.verificarAluno(codigoAluno);

        if (aluno == null) {
            System.out.println("Aluno não encontrado.");
            return;
        }

        System.out.print("Código do curso: ");
        int codigoCurso = scanner.nextInt();

        Curso cursoEncontrado = null;

        for (int i = 0; i < quantidadeCursos; i++) {

            if (cursos[i].getCodigo() == codigoCurso) {
                cursoEncontrado = cursos[i];
                break;
            }
        }

        if (cursoEncontrado == null) {
            System.out.println("Curso não encontrado.");
            return;
        }

        aluno.setCurso(cursoEncontrado);

        System.out.println("Aluno associado ao curso com sucesso!");
    }

    public static void listarApenasCursos(
            Curso[] cursos,
            int quantidadeCursos) {

        System.out.println("\n=== CURSOS CADASTRADOS ===");

        if (quantidadeCursos == 0) {
            System.out.println("Nenhum curso cadastrado.");
            return;
        }

        for (int i = 0; i < quantidadeCursos; i++) {

            System.out.println("--------------------------");
            cursos[i].exibeDados();
        }
    }

    public static void listarCursos(
            Curso[] cursos,
            int quantidadeCursos,
            ListaDeAlunos listaAlunos) {

        System.out.println("\n=== CURSOS CADASTRADOS ===");

        if (quantidadeCursos == 0) {
            System.out.println("Nenhum curso cadastrado.");
            return;
        }

        for (int i = 0; i < quantidadeCursos; i++) {

            System.out.println("--------------------------");

            cursos[i].exibeDados();

            System.out.println("Alunos matriculados:");

            listaAlunos.listarAlunosDoCurso(cursos[i]);
        }
    }

    public static void lancarNotas(
            Scanner scanner,
            ListaDeAlunos listaAlunos) {

        System.out.println("\n=== LANÇAR NOTAS ===");

        System.out.print("Código do aluno: ");
        int codigo = scanner.nextInt();

        Aluno aluno = listaAlunos.verificarAluno(codigo);

        if (aluno == null) {
            System.out.println("Aluno não encontrado.");
            return;
        }

        for (int i = 0; i < 3; i++) {

            System.out.print(
                    "Digite a nota " + (i + 1) + ": ");

            double nota = scanner.nextDouble();

            aluno.lancarNota(i, nota);
        }

        System.out.println("Notas lançadas com sucesso!");
    }

    public static void consultarNotas(
            Scanner scanner,
            ListaDeAlunos listaAlunos) {

        System.out.println("\n=== CONSULTAR NOTAS ===");

        System.out.print("Código do aluno: ");
        int codigo = scanner.nextInt();

        Aluno aluno = listaAlunos.verificarAluno(codigo);

        if (aluno == null) {
            System.out.println("Aluno não encontrado.");
            return;
        }

        aluno.exibirNotas();
    }
}