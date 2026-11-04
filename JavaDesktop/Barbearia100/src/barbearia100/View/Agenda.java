package barbearia100.View;

public class Agenda extends javax.swing.JFrame {

    public Agenda() {
        iniciarComponentes();
    }

    private void iniciarComponentes() {
        // Declaração dos componentes da tela de agendamento
        BlackBackground = new javax.swing.JPanel();
        TituloAgendamento = new javax.swing.JLabel();

        LabelCliente = new javax.swing.JLabel();
        txtCliente = new javax.swing.JTextField();

        LabelServico = new javax.swing.JLabel();
        txtServico = new javax.swing.JTextField();

        LabelDataHora = new javax.swing.JLabel();
        txtDataHora = new javax.swing.JTextField();

        BtnAgendar = new javax.swing.JButton();

        fundoLogo = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Barbearia 100 - Agendamento");

        // Painel central com fundo preto (igual ao de login)
        BlackBackground.setBackground(new java.awt.Color(0, 0, 0));

        // Título "Agendamento"
        TituloAgendamento.setFont(new java.awt.Font("Segoe UI", 1, 24)); // NOI18N
        TituloAgendamento.setForeground(new java.awt.Color(255, 255, 255));
        TituloAgendamento.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        TituloAgendamento.setText("Agendamento");

        // Rótulo e Campo: Cliente (com ícone opcional)
        LabelCliente.setFont(new java.awt.Font("Segoe UI", 0, 16));
        LabelCliente.setForeground(new java.awt.Color(255, 255, 255));
        LabelCliente.setText("Cliente");
        // Opcional: Adicionando ícone de cliente que você tem na pasta icons
        LabelCliente.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/icons/cliente-32.png")));

        txtCliente.setText("Nome do cliente");

        // Rótulo e Campo: Serviço
        LabelServico.setFont(new java.awt.Font("Segoe UI", 0, 16));
        LabelServico.setForeground(new java.awt.Color(255, 255, 255));
        LabelServico.setText("Serviço");
        LabelServico.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/icons/tesoura32.png")));

        txtServico.setText("Ex: Corte / Barba");

        // Rótulo e Campo: Data e Hora
        LabelDataHora.setFont(new java.awt.Font("Segoe UI", 0, 16));
        LabelDataHora.setForeground(new java.awt.Color(255, 255, 255));
        LabelDataHora.setText("Data e Hora");
        LabelDataHora.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/icons/agenda32-icon.png")));

        txtDataHora.setText("DD/MM/AAAA HH:MM");

        // Botão Confirmar Agendamento (seguindo o padrão amarelo do botão Logar)
        BtnAgendar.setBackground(new java.awt.Color(255, 255, 102));
        BtnAgendar.setFont(new java.awt.Font("Segoe UI", 1, 14));
        BtnAgendar.setText("Confirmar Agendamento");

        // Organização do Layout interno do painel (GroupLayout)
        javax.swing.GroupLayout BlackBackgroundLayout = new javax.swing.GroupLayout(BlackBackground);
        BlackBackground.setLayout(BlackBackgroundLayout);
        BlackBackgroundLayout.setHorizontalGroup(
                BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(BlackBackgroundLayout.createSequentialGroup()
                                .addGap(30, 30, 30)
                                .addGroup(BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                        .addComponent(TituloAgendamento, javax.swing.GroupLayout.DEFAULT_SIZE, 260, Short.MAX_VALUE)
                                        .addComponent(LabelCliente)
                                        .addComponent(txtCliente)
                                        .addComponent(LabelServico)
                                        .addComponent(txtServico)
                                        .addComponent(LabelDataHora)
                                        .addComponent(txtDataHora)
                                        .addComponent(BtnAgendar, javax.swing.GroupLayout.DEFAULT_SIZE, 260, Short.MAX_VALUE))
                                .addContainerGap(30, Short.MAX_VALUE))
        );
        BlackBackgroundLayout.setVerticalGroup(
                BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(BlackBackgroundLayout.createSequentialGroup()
                                .addGap(20, 20, 20)
                                .addComponent(TituloAgendamento, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(LabelCliente)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtCliente, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(12, 12, 12)
                                .addComponent(LabelServico)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtServico, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(12, 12, 12)
                                .addComponent(LabelDataHora)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtDataHora, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(24, 24, 24)
                                .addComponent(BtnAgendar, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addContainerGap(30, Short.MAX_VALUE))
        );

     fundoLogo.setBackground(new java.awt.Color(0, 0, 0));
        fundoLogo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/logo1.jpg"))); // NOI18N
        fundoLogo.setVerifyInputWhenFocusTarget(false);

        pack();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 712, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 479, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    public static void main(String args[]) {

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Agenda().setVisible(true);
            }
        });
    }
    private javax.swing.JPanel BlackBackground;
    private javax.swing.JLabel TituloAgendamento;

    private javax.swing.JLabel LabelCliente;
    private javax.swing.JTextField txtCliente;

    private javax.swing.JLabel LabelServico;
    private javax.swing.JTextField txtServico;

    private javax.swing.JLabel LabelDataHora;
    private javax.swing.JTextField txtDataHora;

    private javax.swing.JButton BtnAgendar;

    private javax.swing.JLabel fundoLogo;

    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
}
