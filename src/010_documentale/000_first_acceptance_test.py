from unittest import TestCase

from .document import Colori, Documento, StatoDocumento, TipoDocumento


class ColoreDocumentoShould(TestCase):
    """
    Dato un documento
        firmato digitalmente,
        di qualsiasi tipo,
        in stato di lavorazione
    quando gli viene associato un colore
    allora il colore associato e' il ROSSO
    """

    def test_colore_rosso_quando_viene_associato_dato_un_documento_firmato_digitalmente_in_stato_di_lavorazione(
        self,
    ):
        documento = Documento(
            protocollo="123",
            tipo=TipoDocumento.DISTINTA_MATERIALI,
            stato=StatoDocumento.IN_LAVORAZIONE,
            firmato=True,
        )
        self.assertEqual(documento.colore(), Colori.ROSSO)
