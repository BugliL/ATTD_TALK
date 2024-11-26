Feature: Versionamento documenti
  Come utente del sistema documentale 
  Voglio salvare una nuova versione di un documento 
  Per tenere traccia delle modifiche effettuate

  Scenario: Caricamento di una nuova versione di un documento
    Given il documento "Contratto.docx" ha la versione 1.0
    When viene caricata una nuova versione del "Contratto.docx"
    Then il sistema aggiorna il documento alla versione 1.1
    And il sistema aggiorna lo storico versioni del "Contratto.docx"

  Scenario: Visualizzazione storico versioni
    Given il documento "Contratto.docx" con tre versioni salvate
    Then il sistema mostra le versioni 1.0, 1.1, 1.2 con data e autore delle modifiche