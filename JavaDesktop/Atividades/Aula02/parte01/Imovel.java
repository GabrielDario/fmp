public class Imovel {
    String local;
    int metrosQuadrados;

    public int getMetrosQuadrados() {
        return metrosQuadrados;
    }
    public void setMetrosQuadrados(int metrosQuadrados) {
        this.metrosQuadrados = metrosQuadrados;
    }
    public Imovel(String local, int metrosQuadrados) {
        this.local = local;
        this.metrosQuadrados = metrosQuadrados;
    }
    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }



    public void apresentar() {
        System.out.println("local: " + local + ", Metros Quadrados: " + metrosQuadrados);
    }

}