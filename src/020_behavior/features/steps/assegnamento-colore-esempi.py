import random

from behave import given, then
from document import Colori, Documento, StatoDocumento, TipoDocumento


@given("documento di tipo {tipo}, nello stato {stato}, firmato {firmato}")
def step_given_documento_distinta_materiale(context, tipo, stato, firmato):

    tipo = TipoDocumento[tipo] if tipo != "ANY" else random.choice(list(TipoDocumento))

    stato = (
        StatoDocumento[stato] if stato != "ANY" else random.choice(list(StatoDocumento))
    )

    firmato = (
        bool(firmato == "True") if firmato != "ANY" else random.choice([True, False])
    )

    context.documento = Documento(
        tipo=tipo, stato=stato, protocollo="125", firmato=firmato
    )


@then("il colore associato è {colore}")
def step_then_colore_associato(context, colore):
    assert context.documento.colore() == Colori[colore]
