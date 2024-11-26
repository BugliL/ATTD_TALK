Feature: Assegnazione colore documento

  Scenario: Assegnamento colore documento distinta materiale
    Given documento di tipo distinta materiale
    Then il colore associato è il GIALLO

  Scenario: Assegnamento colore documento in lavorazione
    Given documento in stato di lavorazione, firmato
    Then il colore associato è il ROSSO