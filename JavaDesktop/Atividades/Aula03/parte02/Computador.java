public class Computador {
    private String modelo;
    private double capacidadeProcessador; 
    private double memoriaRam;         
    private double discoEnrigido;     

    public Computador(String modelo, double capacidadeProcessador, double memoriaRam, double discoEnrigido) {
        this.modelo = modelo;
        this.capacidadeProcessador = capacidadeProcessador;
        this.memoriaRam = memoriaRam;
        this.discoEnrigido = discoEnrigido;
    }

    public double getCapacidadeProcessador() {
        return capacidadeProcessador;
    }

    public void setCapacidadeProcessador(double capacidadeProcessador) {
        this.capacidadeProcessador = capacidadeProcessador;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public double getMemoriaRam() {
        return memoriaRam;
    }

    public void setMemoriaRam(double memoriaRam) {
        this.memoriaRam = memoriaRam;
    }

    public double getDiscoEnrigido() {
        return discoEnrigido;
    }

    public void setDiscoEnrigido(double discoEnrigido) {
        this.discoEnrigido = discoEnrigido;
    }
}