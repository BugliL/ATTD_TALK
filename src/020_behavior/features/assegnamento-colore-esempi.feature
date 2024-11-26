Feature: Asssegnazione colore documento

  Scenario Outline: Assegnamento colore documento
    Given documento di tipo <tipo>, nello stato <stato>, firmato <firmato>
    Then il colore associato è <colore>

    Examples:
      | tipo               | stato           | firmato | colore |
      | DISTINTA_MATERIALI | ANY             | ANY     | GIALLO |
      | FATTURA            | IN_LAVORAZIONE  | True    | ROSSO  |