package barbearia100.View;

public class Agenda extends javax.swing.JFrame {

    public Agenda() {
        initComponents();
    }


    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        panelLeft = new javax.swing.JPanel();
        nameInput = new javax.swing.JTextField();
        horaInput = new javax.swing.JTextField();
        clienteLabel = new javax.swing.JLabel();
        dataInput = new javax.swing.JTextField();
        dataLabel = new javax.swing.JLabel();
        clienteInput = new javax.swing.JTextField();
        valorLabel = new javax.swing.JLabel();
        serviceLabel = new javax.swing.JLabel();
        valorInput = new javax.swing.JComboBox<>();
        servicoInput = new javax.swing.JComboBox<>();
        horaLabel = new javax.swing.JLabel();
        nameLabel = new javax.swing.JLabel();
        buttonAgendar = new javax.swing.JButton();
        panelRight = new javax.swing.JPanel();
        iconAgenda = new javax.swing.JLabel();
        agendamentoTitle = new javax.swing.JLabel();
        tabelaAgenda = new javax.swing.JScrollPane();
        tabelaAgeda = new javax.swing.JTable();
        fundoOpaco = new javax.swing.JLabel();
        fundoLogo = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        panelLeft.setOpaque(false);
        panelLeft.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        nameInput.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        nameInput.setText("Digite seu nome");
        nameInput.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                nameInputActionPerformed(evt);
            }
        });
        panelLeft.add(nameInput, new org.netbeans.lib.awtextra.AbsoluteConstraints(65, 6, -1, -1));

        horaInput.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        horaInput.setText("Digite seu nome");
        panelLeft.add(horaInput, new org.netbeans.lib.awtextra.AbsoluteConstraints(65, 194, 150, 30));

        clienteLabel.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        clienteLabel.setForeground(new java.awt.Color(255, 255, 255));
        clienteLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        clienteLabel.setText("Cliente");
        panelLeft.add(clienteLabel, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 49, -1, -1));

        dataInput.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        dataInput.setText("Digite seu nome");
        dataInput.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                dataInputActionPerformed(evt);
            }
        });
        panelLeft.add(dataInput, new org.netbeans.lib.awtextra.AbsoluteConstraints(65, 157, -1, -1));

        dataLabel.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        dataLabel.setForeground(new java.awt.Color(255, 255, 255));
        dataLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        dataLabel.setText("Data");
        panelLeft.add(dataLabel, new org.netbeans.lib.awtextra.AbsoluteConstraints(2, 160, -1, -1));

        clienteInput.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        clienteInput.setText("Digite seu nome");
        clienteInput.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                clienteInputActionPerformed(evt);
            }
        });
        panelLeft.add(clienteInput, new org.netbeans.lib.awtextra.AbsoluteConstraints(65, 46, -1, -1));

        valorLabel.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        valorLabel.setForeground(new java.awt.Color(255, 255, 255));
        valorLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        valorLabel.setText("Valor");
        panelLeft.add(valorLabel, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 123, -1, -1));

        serviceLabel.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        serviceLabel.setForeground(new java.awt.Color(255, 255, 255));
        serviceLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        serviceLabel.setText("Servço");
        panelLeft.add(serviceLabel, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 86, -1, -1));

        valorInput.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        valorInput.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        valorInput.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                valorInputActionPerformed(evt);
            }
        });
        panelLeft.add(valorInput, new org.netbeans.lib.awtextra.AbsoluteConstraints(65, 120, -1, -1));

        servicoInput.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        servicoInput.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        panelLeft.add(servicoInput, new org.netbeans.lib.awtextra.AbsoluteConstraints(65, 83, -1, -1));

        horaLabel.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        horaLabel.setForeground(new java.awt.Color(255, 255, 255));
        horaLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        horaLabel.setText("Hora");
        panelLeft.add(horaLabel, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 194, -1, -1));

        nameLabel.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        nameLabel.setForeground(new java.awt.Color(255, 255, 255));
        nameLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        nameLabel.setText("Nome");
        panelLeft.add(nameLabel, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 9, -1, -1));

        buttonAgendar.setText("Agendar");
        panelLeft.add(buttonAgendar, new org.netbeans.lib.awtextra.AbsoluteConstraints(51, 287, 124, 40));

        getContentPane().add(panelLeft, new org.netbeans.lib.awtextra.AbsoluteConstraints(110, 60, 230, 350));

        panelRight.setBackground(new java.awt.Color(102, 102, 102));
        panelRight.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        iconAgenda.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        iconAgenda.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/icons/agenda32-icon.png"))); // NOI18N
        panelRight.add(iconAgenda, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 0, 50, 50));

        agendamentoTitle.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        agendamentoTitle.setText("Agendamento");
        panelRight.add(agendamentoTitle, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 10, 170, 30));

        tabelaAgeda.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "Cliente", "Data", "Hora", "Servico"
            }
        ));
        tabelaAgenda.setViewportView(tabelaAgeda);

        panelRight.add(tabelaAgenda, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 60, 210, 270));

        getContentPane().add(panelRight, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 60, 230, 340));

        fundoOpaco.setForeground(new java.awt.Color(255, 255, 255));
        fundoOpaco.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/painel-login.png"))); // NOI18N
        fundoOpaco.setText("jLabel1");
        getContentPane().add(fundoOpaco, new org.netbeans.lib.awtextra.AbsoluteConstraints(50, 50, 570, 370));

        fundoLogo.setBackground(new java.awt.Color(0, 0, 0));
        fundoLogo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/logo1.jpg"))); // NOI18N
        fundoLogo.setVerifyInputWhenFocusTarget(false);
        getContentPane().add(fundoLogo, new org.netbeans.lib.awtextra.AbsoluteConstraints(6, 6, -1, -1));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void valorInputActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_valorInputActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_valorInputActionPerformed

    private void clienteInputActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_clienteInputActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_clienteInputActionPerformed

    private void dataInputActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_dataInputActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_dataInputActionPerformed

    private void nameInputActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_nameInputActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_nameInputActionPerformed

    public static void main(String args[]) {

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Agenda().setVisible(true);
            }
        });
    }
    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel agendamentoTitle;
    private javax.swing.JButton buttonAgendar;
    private javax.swing.JTextField clienteInput;
    private javax.swing.JLabel clienteLabel;
    private javax.swing.JTextField dataInput;
    private javax.swing.JLabel dataLabel;
    private javax.swing.JLabel fundoLogo;
    private javax.swing.JLabel fundoOpaco;
    private javax.swing.JTextField horaInput;
    private javax.swing.JLabel horaLabel;
    private javax.swing.JLabel iconAgenda;
    private javax.swing.JTextField nameInput;
    private javax.swing.JLabel nameLabel;
    private javax.swing.JPanel panelLeft;
    private javax.swing.JPanel panelRight;
    private javax.swing.JLabel serviceLabel;
    private javax.swing.JComboBox<String> servicoInput;
    private javax.swing.JTable tabelaAgeda;
    private javax.swing.JScrollPane tabelaAgenda;
    private javax.swing.JComboBox<String> valorInput;
    private javax.swing.JLabel valorLabel;
    // End of variables declaration//GEN-END:variables
}
