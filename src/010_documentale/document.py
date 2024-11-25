from dataclasses import dataclass
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
