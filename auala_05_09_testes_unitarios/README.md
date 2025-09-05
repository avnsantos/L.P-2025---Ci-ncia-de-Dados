# Projeto da Aula de Testes Unitários em Python

aula de Testes Unitários do dia 05/09/2025. O objetivo é demonstrar como criar e executar uma suíte de testes para uma função Python usando a biblioteca padrão `unittest`.

## Estrutura dos Arquivos

* `modulo.py`: Contém a lógica de negócio. Neste caso, uma função recursiva `fatorial(num)` que calcula o fatorial de um número.
* `test_modulo.py`: Contém a suíte de testes. É responsável por importar o `modulo.py` e verificar se a função `fatorial` se comporta como o esperado em diferentes cenários.

## Como Usar

### Pré-requisitos

* Python 3.x

### Executando os Testes

1.  Clone este repositório para a sua máquina local.
2.  Abra um terminal e navegue até a pasta do projeto.
3.  Execute o seguinte comando para rodar a suíte de testes:

    ```sh
    python test_modulo.py
    ```

    Para uma saída mais detalhada (verbose), use:
    ```sh
    python test_modulo.py -v
    ```

### Entendendo a Saída

Ao executar os testes, você verá um resumo dos resultados. Cada `.` (ponto) representa um teste que passou. Se um teste falhar, você verá um `F`; se ocorrer um erro inesperado, verá um `E`. No final, um relatório indicará o número total de testes executados e se todos passaram.

## Conceitos Abordados

* **Recursão:** A função `fatorial` é implementada de forma recursiva.
* **Testes Unitários:** Uso da biblioteca `unittest`.
* **Suíte de Testes:** Criação de uma classe que herda de `unittest.TestCase`.
* **Métodos de Asserção:**
    * `self.assertEqual()`: Para verificar igualdade exata.
    * `self.assertRaises()`: Para verificar se uma função levanta o erro esperado.
    * `self.assertAlmostEqual()`: Para comparar números de ponto flutuante com uma precisão definida.
* **Técnicas de Teste (mencionadas em aula):**
    * Partição de Classes de Equivalência.
    * Análise de Valor Limite (Boundary Value Analysis).
