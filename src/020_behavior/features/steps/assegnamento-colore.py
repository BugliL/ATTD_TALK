from behave import given, then
from document import Colori, Documento, StatoDocumento, TipoDocumento


@given("documento di tipo distinta materiale")
def step_given_documento_distinta_materiale(context):
    context.documento = Documento(
        tipo=TipoDocumento.DISTINTA_MATERIALI,
        stato=StatoDocumento.INVIATO,
        protocollo="125",
        firmato=False,
    )


@given("documento in stato di lavorazione, firmato")
def step_given_documento_in_lavorazione(context):
    context.documento = Documento(
        tipo=TipoDocumento.FATTURA,
        stato=StatoDocumento.IN_LAVORAZIONE,
        protocollo="125",
        firmato=True,
    )


@then("il colore associato è il {colore}")
def step_then_colore_associato(context, colore):
    assert (
        context.documento.colore() == Colori[colore]
    ), f"Expected {colore}, got {context.documento.colore()}"
