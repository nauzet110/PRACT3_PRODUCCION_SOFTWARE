from datetime import date
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from core.expense_service import ExpenseService
from core.in_memory_expense_repository import InMemoryExpenseRepository

scenarios("./expense_management.feature")

@pytest.fixture
def context():
    repo = InMemoryExpenseRepository()
    service = ExpenseService(repo)
    return {"service": service}

@given(parsers.parse("un gestor de gastos vacío"))
def empty_manager(context):
    pass

@given(parsers.parse("un gestor con un gasto de {amount:d} euros"))
def manager_with_one_expense(context, amount):
    context["service"].create_expense(
        title="Gasto inicial", amount=amount, description="", expense_date=date.today()
    )

@given(parsers.parse('un gestor con un gasto de {amount:d} euros llamado "{title}"'))
def manager_with_specific_expense(context, amount, title):
    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=date.today()
    )

@when(parsers.parse("añado un gasto de {amount:d} euros llamado {title}"))
def add_expense(context, amount, title):
    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=date.today()
    )

@when(parsers.parse("elimino el gasto con id {expense_id:d}"))
def remove_expense(context, expense_id):
    context["service"].remove_expense(expense_id)

@when(parsers.parse("actualizo el gasto con id {expense_id:d} para que cueste {amount:d} euros"))
def update_expense_amount(context, expense_id, amount):
    context["service"].update_expense(expense_id=expense_id, amount=amount)

@when(parsers.parse('actualizo el título del gasto con id {expense_id:d} a "{title}"'))
def update_expense_title(context, expense_id, title):
    context["service"].update_expense(expense_id=expense_id, title=title)

@then(parsers.parse("el total de dinero gastado debe ser {total:d} euros"))
def check_total(context, total):
    # Si el total real no es igual al esperado, el test falla aquí
    assert context["service"].total_amount() == float(total)

@then(parsers.parse("debe haber {expenses:d} gastos registrados"))
def check_expenses_length(context, expenses):
    # Comprobación estricta de la cantidad de elementos devueltos por el servicio
    assert len(context["service"].list_expenses()) == expenses

@then(parsers.parse('el gasto con id {expense_id:d} debe aparecer en el servicio como "{title}"'))
def check_expense_title_via_service(context, expense_id, title):
    # Buscamos el gasto y verificamos su nombre. Si es distinto, el test falla.
    gastos = context["service"].list_expenses()
    gasto = next((g for g in gastos if g.id == expense_id), None)

    assert gasto is not None, f"No se encontró el gasto con ID {expense_id}"
    assert gasto.title == title, f"Se esperaba '{title}' pero se encontró '{gasto.title}'"