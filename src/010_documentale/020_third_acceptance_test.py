from unittest import TestCase

from .document import Colori, Documento, StatoDocumento, TipoDocumento


class ColoreDocumentoShould(TestCase):
    """
    Dato un documento di tipo "distinta materiale"
    quando gli viene associato un colore
    allora il colore associato è il GIALLO
    """

    def test_colore_giallo_quando_viene_associato_dato_un_documento_di_tipo_distinta_materiale(
        self,
    ):
        documento = Documento(
            protocollo="125",
            tipo=TipoDocumento.DISTINTA_MATERIALI,
            stato=StatoDocumento.INVIATO,
            firmato=False,
        )
        self.assertEqual(documento.colore(), Colori.GIALLO)
