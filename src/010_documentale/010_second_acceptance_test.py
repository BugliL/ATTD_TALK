from unittest import TestCase

from .document import Colori, Documento, StatoDocumento, TipoDocumento


class ColoreDocumentoShould(TestCase):
    """
    Dato un documento firmato digitalmente, di qualsiasi tipo, non in stato in lavorazione
    quando gli viene associato un colore
    allora il colore associato è il VERDE
    """

    def test_colore_verde_quando_viene_associato_dato_un_documento_firmato_digitalmente(
        self,
    ):
        documento = Documento(
            protocollo="124",
            tipo=TipoDocumento.DISTINTA_MATERIALI,
            stato=StatoDocumento.INVIATO,
            firmato=True,
        )
        self.assertEqual(documento.colore(), Colori.VERDE)
