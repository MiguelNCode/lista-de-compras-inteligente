# 🛒 Lista de Compras Inteligente – Terminal App

Projeto de uma aplicação de terminal feita com Python, que simula uma **lista de compras dinâmica**.  
Você pode adicionar, remover, listar e filtrar produtos por categoria ou valor total.  
Os dados são **salvos localmente** usando arquivos `.json`, o que garante persistência entre execuções.

> 🧠 Criado para treinar lógica, organização de código, JSON, funções lambda e modularização.

## 📦 Funcionalidades

- ✅ Adicionar novos produtos com nome, preço, tipo e quantidade
- ❌ Remover unidades ou produtos inteiros
- 📄 Listar todos os produtos cadastrados com valores totais
- 🔍 Filtrar por:
  - Categoria (Alimentício, Higiene, Bebidas, Outros)
  - Ordem alfabética
  - Preço total (crescente/decrescente)
- 💾 Salvar e ler dados diretamente de um arquivo JSON
- 🧠 Uso de funções `lambda` para ordenações e filtros dinâmicos

## 📁 Estrutura do Projeto

```

📦 lista-de-compras-inteligente
├── lista_de_compras_inteli.py             # Arquivo principal com menu e loop
├── lista_de_compras_inteli_func.py    # Funções de lógica do programa
├── lista_de_compras_inteli_class.py   # Classe Produto
├── lista_de_produtos.json               # Banco de dados local (JSON)
├── README.md                              # Este arquivo
└── LICENSE                                # Licença MIT

````

---

## 🚀 Como Rodar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/lista-de-compras-inteligente.git
````

2. Entre na pasta e execute:

```
cd lista-de-compras-inteligente
python main.py
```

⚠️ Certifique-se de ter o Python instalado (recomendo Python 3.10+)

## 🎓 Aprendizados com esse Projeto

* 🧠 Manipulação de arquivos JSON para armazenar dados
* 🧰 Programação orientada a objetos (classe `Produto`)
* 🔁 Laços de repetição e controle de fluxo com `match`
* 💡 Uso prático de `lambda` com `sorted()` e `filter()`
* 🗂 Modularização real de arquivos Python
* 🧼 Clareza de código, boas práticas e organização
* 💬 Interação via terminal com tratamento básico de erros

## 📜 Licença

Este projeto está sob a Licença MIT.
Sinta-se livre para usar, estudar, modificar – **mas não roube a autoria.** 😉

---

## 💬 Feedback?

Se você tiver sugestões, bugs ou ideias de melhoria, sinta-se à vontade para abrir uma **Issue** ou me chamar no Discord!
