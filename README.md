# 🍽️ Autoatendimento de Restaurante (Python – Console)

Aplicativo de **autoatendimento via terminal** que lê um **cardápio em .CSV** e permite ao cliente navegar por categorias, adicionar itens ao carrinho e **finalizar o pagamento** (dinheiro, Pix, débito ou crédito).

---

## ✨ Funcionalidades

- **Navegação por categorias** → Bebidas, Lanches e Sobremesas.
- **Adicionar ao carrinho** → Seleção por código + quantidade.
- **Carrinho detalhado** → Agrupa itens, mostra subtotal e **total**.
- **Pagamento** → Dinheiro, **Pix** (com chave simulada), Débito e Crédito.
- **Interface textual** → Menus claros e mensagens de feedback.

---

## 📚 Bibliotecas

- **Pandas** → Faz a leitura do `cardapio.csv` e facilita o filtro por **Categoria**, além do acesso a `Produto` e `Preço`.
