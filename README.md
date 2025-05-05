🛒 Sistema de Supermercado com Login em Python
Este projeto é um sistema de supermercado em terminal, desenvolvido em Python, com suporte a múltiplos usuários, autenticação, níveis de acesso (usuário e administrador), carrinho de compras e persistência de dados usando arquivos JSON.

📋 Funcionalidades
Registro de novos usuários com validação e armazenamento seguro (hash de senha)

Login com autenticação e controle de tentativas

Perfis com edição de nome, e-mail e senha

Níveis de acesso: admin e usuario

Acesso a um sistema de compras com carrinho persistente

Finalização de compra e exibição do total

Salvamento automático dos dados dos usuários e carrinhos

🧱 Estrutura dos Arquivos
usuarios.json: Armazena informações dos usuários (nome, e-mail, senha hash, nível de acesso)

carrinhos.json: Armazena os carrinhos de compras de cada usuário

O código principal gerencia toda a lógica de fluxo, autenticação e compras

🛠 Tecnologias Usadas
Python 3

Módulos padrão:

json – para manipulação de arquivos de dados

hashlib – para hashing seguro de senhas

os – para verificação de existência de arquivos

▶️ Como Executar
Certifique-se de ter o Python 3 instalado.

Clone este repositório ou copie o código para um arquivo chamado, por exemplo, supermercado.py.

Execute com:

bash
Copiar
Editar
python supermercado.py
🧪 Funcionalidade dos Usuários
Registrar: Cria um novo usuário com nome, e-mail, senha e nível.

Login: Acessa o painel apropriado com base no nível (admin ou usuario).

Painel do Admin: Acesso ao supermercado e edição do próprio perfil.

Painel do Usuário: Idêntico ao admin, mas sem funcionalidades de gerenciamento adicionais (ainda não implementadas no código atual).

🛍️ Sistema de Compras
Produtos fixos no dicionário produtos

Adição de itens ao carrinho

Persistência dos itens entre sessões

Finalização de compras com resumo e limpeza automática do carrinho

📦 Exemplo de Produtos
ID	Produto	Preço (R$)
1	Arroz	5.99
2	Feijão	4.79
3	Macarrão	2.49
4	Carne	25.90

🔒 Segurança
As senhas dos usuários são armazenadas de forma segura com o algoritmo SHA-256

Validação de senha atual antes de permitir alterações

📌 Notas Finais
Esse sistema é ideal para aprendizado de conceitos básicos e intermediários de Python, como leitura e escrita de arquivos, estrutura condicional, funções e segurança básica.

Pode ser facilmente expandido com mais funcionalidades, como banco de dados real, interface gráfica, autenticação com e-mail, etc.
