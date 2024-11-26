from datetime import datetime

from behave import given, then, when
from document import GestoreDocumenti


@given('il documento "{nome}" ha la versione {versione}')
def step_given_documento_con_versione(context, nome, versione):
    context.gestore = GestoreDocumenti()
    context.gestore.aggiungi_documento(nome, versione, autore="Mario Rossi")


@when('viene caricata una nuova versione del "{nome}"')
def step_when_nuova_versione(context, nome):
    context.gestore.nuova_versione(nome, autore="Mario Rossi")


@then("il sistema aggiorna il documento alla versione {nuova_versione}")
def step_then_versione_aggiornata(context, nuova_versione):
    documento = context.gestore.storico_versioni("Contratto.docx")
    ultima_versione = documento[-1].numero
    assert (
        ultima_versione == nuova_versione
    ), f"Versione attesa: {nuova_versione}, versione effettiva: {ultima_versione}"


@then('il sistema aggiorna lo storico versioni del "{nome}"')
def step_then_storico_aggiornato(context, nome):
    documento = context.gestore.storico_versioni(nome)
    assert len(documento) > 1


@given('il documento "{nome}" con tre versioni salvate')
def step_given_documento_tre_versioni(context, nome):
    context.gestore = GestoreDocumenti()
    context.gestore.aggiungi_documento(nome, "1.0", autore="Mario Rossi")
    context.gestore.nuova_versione(nome, autore="Luigi Bianchi")
    context.gestore.nuova_versione(nome, autore="Anna Verdi")


@then("il sistema mostra le versioni {versioni} con data e autore delle modifiche")
def step_then_mostra_versioni(context, versioni):
    versioni_attese = versioni.split(", ")
    storico = context.gestore.storico_versioni("Contratto.docx")
    versioni_effettive = [v.numero for v in storico]

    # Confronta le versioni attese con quelle effettive
    assert (
        versioni_effettive == versioni_attese
    ), f"Versioni attese: {versioni_attese}, versioni effettive: {versioni_effettive}"

    # Controlla che ogni versione abbia una data e un autore
    for versione in storico:
        assert isinstance(versione.data, datetime)
        assert versione.autore

    for versione in storico:
        assert isinstance(versione.data, datetime)
        assert versione.autore
        assert versione.autore
