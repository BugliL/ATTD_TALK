from unittest import TestCase

from .document import Colori, Documento, StatoDocumento, TipoDocumento


class ColoreDocumentoShould(TestCase):
    """
    Dato un documento in lavorazione
    quando gli viene associato un colore
    allora il colore associato è il ROSSO
    a meno che il documento sia di tipo "disegno tecnico",
    in tal caso il colore associato è il BLU
    """

    def test_colore_rosso_quando_viene_associato_dato_un_documento_in_lavorazione_non_disegno_tecnico(
        self,
    ):
        documento = Documento(
            protocollo="126",
            tipo=TipoDocumento.DISTINTA_MATERIALI,
            stato=StatoDocumento.IN_LAVORAZIONE,
            firmato=False,
        )
        self.assertEqual(documento.colore(), Colori.ROSSO)
