from datetime import date

from core.expense import Expense
from core.in_memory_expense_repository import InMemoryExpenseRepository


def create_expense(id=1, title="Test", amount=10):
    return Expense(
        id=id, title=title, amount=amount, description="", expense_date=date.today()
    )


def test_save_new_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense()
    repo.save(expense)
    expenses = repo.list_all()
    assert len(expenses) == 1
    assert expenses[0].id == 1


def test_save_updates_existing_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense()

    repo.save(expense)

    updated = create_expense(id=1, title="Updated", amount=20)
    repo.save(updated)

    expenses = repo.list_all()
    assert len(expenses) == 1
    assert expenses[0].title == "Updated"
    assert expenses[0].amount == 20


def test_remove_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense()
    repo.save(expense)
    repo.remove(expense_id=1)
    assert repo.list_all() == []


def test_list_all_returns_copy():
    repo = InMemoryExpenseRepository()
    repo.save(create_expense())
    expenses = repo.list_all()
    expenses.clear()
    assert len(repo.list_all()) == 1


def test_get_by_id_returns_expense():
    """
    Prueba que el método repo.get_by_id() retorna el gasto correcto cuando existe un gasto con el id buscado.
    """
    repo = InMemoryExpenseRepository()
    gasto_esperado = create_expense(id=5, title="Gasto Buscado", amount=50)
    repo.save(gasto_esperado)

    resultado = repo.get_by_id(5)

    assert resultado is not None
    assert resultado.id == 5
    assert resultado.title == "Gasto Buscado"
    assert resultado.amount == 50


def test_get_by_id_returns_none_if_not_found():
    """
    Prueba que el método repo.get_by_id() retorna None cuando se consulta un id que no corresponde a ningún gasto guardado.
    """
    repo = InMemoryExpenseRepository()
    repo.save(create_expense(id=1)) # Guardamos uno con ID 1 por si acaso

    resultado = repo.get_by_id(999) # Buscamos uno que no existe

    assert resultado is None