from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TipoDocumento(Enum):
    DISTINTA_MATERIALI = "DISTINTA_MATERIALI"
    ORDINE_ACQUISTO = "ORDINE_ACQUISTO"
    FATTURA = "FATTURA"
    DISEGNO_TECNICO = "DISEGNO_TECNICO"


class StatoDocumento(Enum):
    IN_BOZZA = "IN_BOZZA"
    INVIATO = "INVIATO"
    ACCETTATO = "ACCETTATO"
    IN_LAVORAZIONE = "IN_LAVORAZIONE"


class Colori(Enum):
    ROSSO = "ROSSO"
    VERDE = "VERDE"
    GIALLO = "GIALLO"
    BLU = "BLU"


@dataclass
class Documento:
    protocollo: str
    tipo: TipoDocumento
    stato: StatoDocumento
    firmato: bool

    def colore(self) -> Colori:
        if self.firmato and self.stato == StatoDocumento.IN_LAVORAZIONE:
            return Colori.ROSSO

        if (
            self.tipo == TipoDocumento.DISEGNO_TECNICO
            and self.stato == StatoDocumento.IN_LAVORAZIONE
        ):
            return Colori.BLU

        if self.tipo == TipoDocumento.DISTINTA_MATERIALI:
            return Colori.GIALLO


@dataclass
class Versione:
    numero: str
    data: datetime
    autore: str


class GestoreDocumenti:
    def __init__(self):
        self.documenti = {}

    def aggiungi_documento(self, nome, versione_iniziale, autore):
        versione = Versione(
            numero=versione_iniziale,
            data=datetime.now(),
            autore=autore,
        )
        self.documenti[nome] = [versione]

    def nuova_versione(self, nome, autore):
        storico = self.documenti.get(nome)
        if not storico:
            raise ValueError("Documento non trovato")

        # Ottieni l'ultima versione e calcola la nuova
        ultima_versione = storico[-1]
        nuova_versione_num = f"{float(ultima_versione.numero) + 0.1:.1f}"
        nuova_versione = Versione(
            numero=nuova_versione_num,
            data=datetime.now(),
            autore=autore,
        )
        storico.append(nuova_versione)

    def storico_versioni(self, nome):
        return self.documenti.get(nome, [])
