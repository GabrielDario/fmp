
public class Professor extends Usuario{
    private String areaAtuacao;
    
    public Professor(int mat, String nom,String log, String sen) {
        super(mat,nom,log,sen);
    }

    public String getAreaDeAtuacao() {
        return areaAtuacao;
    }
    
     public void setAreaDeAtuacao() {
        this.areaAtuacao = areaAtuacao;
    }
    
    public void exibeDados(){
        System.out.println("");
        System.out.println("Dados do professor: ");
        super.exibeDados();
        
        if(areaAtuacao !=null && !areaAtuacao.isEmpty()) {
                System.out.println("Área de atuação: " + areaAtuacao);
            }

    }
}