Feature: Gestión de gastos
  Como estudiante
  Quiero registrar mis gastos
  Para controlar cuánto dinero gasto

  Scenario: Crear un gasto y comprobar cual es el total que llevo gastado
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    Then el total de dinero gastado debe ser 5 euros

  Scenario: Eliminar un gasto y comprobar cual es el total que llevo gastado
    Given un gestor con un gasto de 5 euros
    When elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear y eliminar un gasto y comprobar que no he gastado dinero
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear dos gastos diferentes y comprobar que el total que llevo gastado es la suma de ambos
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And añado un gasto de 10 euros llamado Comida
    Then el total de dinero gastado debe ser 15 euros

  Scenario: Crear tres gastos diferentes que sumen 30 euros hace que el total sean 30 euros
    Given un gestor de gastos vacío
    When añado un gasto de 10 euros llamado Libros
    And añado un gasto de 15 euros llamado Comida
    And añado un gasto de 5 euros llamado Transporte
    Then el total de dinero gastado debe ser 30 euros

  Scenario: Crear tres gastos de 10, 30, 30 euros y elimino el ultimo gasto la suma son 40 euros
    Given un gestor de gastos vacío
    When añado un gasto de 10 euros llamado A
    And añado un gasto de 30 euros llamado B
    And añado un gasto de 30 euros llamado C
    And elimino el gasto con id 3
    Then el total de dinero gastado debe ser 40 euros

  # --- BONUS: 3 TESTS ADICIONALES (VERIFICACIÓN ESTRICTA POR SERVICIO) ---

  Scenario: Bonus 1 - Verificación estricta de actualización de importe
    Given un gestor con un gasto de 20 euros
    When actualizo el gasto con id 1 para que cueste 50 euros
    Then el total de dinero gastado debe ser 50 euros

  Scenario: Bonus 2 - Verificación de integridad tras intento de borrado fallido
    Given un gestor con un gasto de 15 euros llamado "Cena"
    When elimino el gasto con id 999
    Then el total de dinero gastado debe ser 15 euros
    And el gasto con id 1 debe aparecer en el servicio como "Cena"

  Scenario: Bonus 3 - Verificación estricta de cambio de nombre
    Given un gestor con un gasto de 20 euros llamado "Cine"
    When actualizo el título del gasto con id 1 a "Teatro"
    Then el gasto con id 1 debe aparecer en el servicio como "Teatro"