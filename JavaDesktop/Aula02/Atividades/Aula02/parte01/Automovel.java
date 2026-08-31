public class Automovel {
    String marca;
    int ano;

    public Automovel(String marca, int ano) {
        this.marca = marca;
        this.ano = ano;
    }


    public String getMarca() {
        return marca;
    }
    
    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAno() {
        return ano;
    }
    
    public void setAno(int ano) {
        this.ano = ano;
    }

        public void apresentar() {
            System.out.println("Marca: " + marca + ", Ano " + ano);
        }
  
}