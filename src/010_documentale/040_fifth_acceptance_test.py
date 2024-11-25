from unittest import TestCase

from .document import Colori, Documento, StatoDocumento, TipoDocumento


class ColoreDocumentoShould(TestCase):
    def test_colore_blu_quando_viene_associato_dato_un_documento_in_lavorazione_di_tipo_disegno_tecnico(
        self,
    ):
        documento = Documento(
            protocollo="127",
            tipo=TipoDocumento.DISEGNO_TECNICO,
            stato=StatoDocumento.IN_LAVORAZIONE,
            firmato=False,
        )
        self.assertEqual(documento.colore(), Colori.BLU)
