
package barbearia100.View;


public class Login extends javax.swing.JFrame {
    
    private static final java.util.logging.Logger logger = java.util.logging.Logger.getLogger(Login.class.getName());

    public Login() {
        initComponents();
    }

   
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        BlackBackground = new javax.swing.JPanel();
        Usuario = new javax.swing.JLabel();
        Login1 = new javax.swing.JLabel();
        Senha = new javax.swing.JLabel();
        login = new javax.swing.JTextField();
        senha = new javax.swing.JTextField();
        Logar = new javax.swing.JButton();
        fundoLogo = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        BlackBackground.setBackground(new java.awt.Color(0, 0, 0));

        Usuario.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        Usuario.setForeground(new java.awt.Color(255, 255, 255));
        Usuario.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        Usuario.setText("Usuario");

        Login1.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        Login1.setForeground(new java.awt.Color(255, 255, 255));
        Login1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        Login1.setText("Login");

        Senha.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        Senha.setForeground(new java.awt.Color(255, 255, 255));
        Senha.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        Senha.setText("Senha");

        login.setText("Insira seu usuario");

        senha.setText("Insira sua senha");
        senha.addActionListener(this::senhaActionPerformed);

        Logar.setBackground(new java.awt.Color(255, 255, 102));
        Logar.setText("Logar");

        javax.swing.GroupLayout BlackBackgroundLayout = new javax.swing.GroupLayout(BlackBackground);
        BlackBackground.setLayout(BlackBackgroundLayout);
        BlackBackgroundLayout.setHorizontalGroup(
            BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(Usuario, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addComponent(Senha, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addGroup(BlackBackgroundLayout.createSequentialGroup()
                .addGroup(BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(BlackBackgroundLayout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(Login1, javax.swing.GroupLayout.DEFAULT_SIZE, 222, Short.MAX_VALUE))
                    .addGroup(BlackBackgroundLayout.createSequentialGroup()
                        .addGroup(BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(BlackBackgroundLayout.createSequentialGroup()
                                .addGap(68, 68, 68)
                                .addComponent(senha, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(BlackBackgroundLayout.createSequentialGroup()
                                .addGap(65, 65, 65)
                                .addComponent(login, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, BlackBackgroundLayout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(Logar)
                .addGap(78, 78, 78))
        );
        BlackBackgroundLayout.setVerticalGroup(
            BlackBackgroundLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(BlackBackgroundLayout.createSequentialGroup()
                .addGap(28, 28, 28)
                .addComponent(Login1, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(Usuario, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(login, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(Senha, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(senha, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(Logar)
                .addContainerGap(21, Short.MAX_VALUE))
        );

        fundoLogo.setBackground(new java.awt.Color(0, 0, 0));
        fundoLogo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/barbearia100/View/imagens/logo1.jpg"))); // NOI18N
        fundoLogo.setVerifyInputWhenFocusTarget(false);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(30, 30, 30)
                .addComponent(fundoLogo))
            .addGroup(layout.createSequentialGroup()
                .addGap(270, 270, 270)
                .addComponent(BlackBackground, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(fundoLogo)
            .addGroup(layout.createSequentialGroup()
                .addGap(120, 120, 120)
                .addComponent(BlackBackground, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void senhaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_senhaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_senhaActionPerformed

   
    public static void main(String args[]) {
 
        java.awt.EventQueue.invokeLater(() -> new Login().setVisible(true));
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel BlackBackground;
    private javax.swing.JButton Logar;
    private javax.swing.JLabel Login1;
    private javax.swing.JLabel Senha;
    private javax.swing.JLabel Usuario;
    private javax.swing.JLabel fundoLogo;
    private javax.swing.JTextField login;
    private javax.swing.JTextField senha;
    // End of variables declaration//GEN-END:variables
}
