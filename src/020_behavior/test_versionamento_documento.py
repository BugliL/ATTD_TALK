import unittest

from .document import GestoreDocumenti


class TestGestoreDocumenti(unittest.TestCase):

    def setUp(self):
        """Setup eseguito prima di ogni test"""
        self.gestore = GestoreDocumenti()

    def test_crea_versione_iniziale_documento_when_aggiungi_documento_called(self):
        """Test che il metodo aggiunga correttamente un documento"""
        self.gestore.aggiungi_documento("Contratto.docx", "1.0", "Mario Rossi")

        # Verifica che il documento sia stato aggiunto correttamente
        documenti = self.gestore.storico_versioni("Contratto.docx")
        self.assertEqual(len(documenti), 1)
        self.assertEqual(documenti[0].numero, "1.0")
        self.assertEqual(documenti[0].autore, "Mario Rossi")

    def test_aggiorna_versione_when_nuova_version_called_with_correct_data(self):
        """Test che il metodo aggiunga una nuova versione a un documento esistente"""
        self.gestore.aggiungi_documento("Contratto.docx", "1.0", "Mario Rossi")
        self.gestore.nuova_versione("Contratto.docx", "Luigi Bianchi")

        # Verifica che sia stata aggiunta una nuova versione
        documenti = self.gestore.storico_versioni("Contratto.docx")
        self.assertEqual(len(documenti), 2)
        self.assertEqual(documenti[-1].numero, "1.1")  # La versione dovrebbe essere 1.1
        self.assertEqual(documenti[-1].autore, "Luigi Bianchi")

    def test_nuova_versione_documento_non_esistente(self):
        """Test che sollevi un'eccezione se si cerca di aggiungere una versione a un documento inesistente"""
        with self.assertRaises(ValueError):
            self.gestore.nuova_versione("Contratto.docx", "Luigi Bianchi")

    def test_return_versioni_documento_when_storico_versioni_called_with_document(self):
        """Test che ritorni lo storico delle versioni di un documento"""
        self.gestore.aggiungi_documento("Contratto.docx", "1.0", "Mario Rossi")
        self.gestore.nuova_versione("Contratto.docx", "Luigi Bianchi")

        documenti = self.gestore.storico_versioni("Contratto.docx")

        # Verifica che lo storico contenga entrambe le versioni
        self.assertEqual(len(documenti), 2)
        self.assertEqual(documenti[0].numero, "1.0")
        self.assertEqual(documenti[1].numero, "1.1")
