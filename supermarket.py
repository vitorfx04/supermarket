import json
import hashlib
import os

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_CARRINHOS = "carrinhos.json"

produtos = {
    1: {"nome": "Arroz", "preco": 5.99},
    2: {"nome": "Feijão", "preco": 4.79},
    3: {"nome": "Macarrão", "preco": 2.49},
    4: {"nome": "Carne", "preco": 25.90}
}

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        try:
            with open(ARQUIVO_USUARIOS, "r") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de usuários.")
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def registrar_usuario(usuarios):
    print("\n--- Registro de Novo Usuário ---")
    user = input("Digite seu nome de usuário: ").strip()
    if not user:
        print("Nome de usuário não pode estar vazio!")
        return

    if user in usuarios:
        print("Usuário já existe! Tente outro nome.")
        return

    user_confirm = input("Confirme seu nome de usuário: ").strip()
    if user != user_confirm:
        print("Os nomes de usuário não coincidem!")
        return

    senha = input("Digite sua senha: ").strip()
    senha_confirm = input("Confirme sua senha: ").strip()

    if not senha or senha != senha_confirm:
        print("As senhas não coincidem ou estão vazias!")
        return

    email = input("Digite seu e-mail: ").strip()
    nome = input("Digite seu nome completo: ").strip()

    while True:
        nivel = input("Digite o nível de acesso (admin/usuario): ").strip().lower()
        if nivel in ["admin", "usuario"]:
            break
        
        print("Nível inválido! Digite 'admin' ou 'usuario'.")

    usuarios[user] = {
        "senha": gerar_hash(senha),
        "email": email,
        "nome": nome,
        "nivel": nivel
    }

    salvar_usuarios(usuarios)
    print("✅ Usuário cadastrado com sucesso!")

def editar_perfil(usuarios, usuario_logado):
    user_data = usuarios[usuario_logado]
    print("\n--- Editar Perfil ---")

    print(f"Nome atual: {user_data['nome']}")
    novo_nome = input("Novo nome (pressione Enter para manter): ").strip()

    if novo_nome:
        user_data['nome'] = novo_nome

    print(f"E-mail atual: {user_data['email']}")
    novo_email = input("Novo e-mail (pressione Enter para manter): ").strip()

    if novo_email:
        user_data['email'] = novo_email

    alterar_senha = input("Deseja alterar a senha? (s/n): ").strip().lower()
    
    if alterar_senha == "s":
        senha_atual = input("Digite sua senha atual: ").strip()
        if gerar_hash(senha_atual) == user_data['senha']:
            nova_senha = input("Nova senha: ").strip()
            confirmar = input("Confirme a nova senha: ").strip()
            if nova_senha == confirmar:
                user_data['senha'] = gerar_hash(nova_senha)
                print("✅ Senha atualizada.")
            else:
                print("❌ As senhas não coincidem.")
        else:
            print("❌ Senha atual incorreta.")

    usuarios[usuario_logado] = user_data
    salvar_usuarios(usuarios)
    print("✅ Perfil atualizado com sucesso!")

def painel_admin(usuario):
    print(f"\n🔐 Painel do Admin ({usuario})")
    print("1 - Editar meu perfil")
    print("2 - Acessar supermercado")
    print("3 - Voltar ao menu")

    opc = input("Escolha uma opção: ").strip()
    if opc == "1":
        editar_perfil(usuarios, usuario)
    elif opc == "2":
        sistema_supermercado(usuario)
    elif opc == "3":
        return
    else:
        print("Opção inválida.")

def painel_usuario(usuario):
    print(f"\n👤 Painel do Usuário ({usuario})")
    print("1 - Editar perfil")
    print("2 - Acessar supermercado")
    print("3 - Voltar ao menu")

    opc = input("Escolha uma opção: ").strip()
    if opc == "1":
        editar_perfil(usuarios, usuario)
    elif opc == "2":
        sistema_supermercado(usuario)
    elif opc == "3":
        return
    else:
        print("Opção inválida.")

def login(usuarios):
    print("\n--- Login ---")
    user = input("Digite seu nome de usuário: ").strip()

    if user not in usuarios:
        print("Usuário não encontrado!")
        return

    tentativas = 3
    while tentativas > 0:
        senha = input("Digite sua senha: ").strip()
        if usuarios[user]["senha"] == gerar_hash(senha):
            nivel = usuarios[user]["nivel"]
            print(f"✅ Login bem-sucedido! Bem-vindo(a), {usuarios[user]['nome']} ({nivel})")

            if nivel == "admin":
                painel_admin(user)
            else:
                painel_usuario(user)
            return
        else:
            tentativas -= 1
            print(f"Senha incorreta! Tentativas restantes: {tentativas}")
    print("⚠️ Muitas tentativas. Tente novamente mais tarde.")

def menu():
    global usuarios
    usuarios = carregar_usuarios()

    while True:
        print("\n--- MENU ---")
        print("1 - Registrar")
        print("2 - Login")
        print("3 - Sair")
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            registrar_usuario(usuarios)
        elif opc == "2":
            login(usuarios)
        elif opc == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

def carregar_carrinho(user_id):
    if os.path.exists(ARQUIVO_CARRINHOS):
        with open(ARQUIVO_CARRINHOS, "r") as f:
            dados = json.load(f)
            return dados.get(user_id, {})
    return {}

def salvar_carrinho(user_id, carrinho):
    if os.path.exists(ARQUIVO_CARRINHOS):
        with open(ARQUIVO_CARRINHOS, "r") as f:
            dados = json.load(f)
    else:
        dados = {}
    dados[user_id] = carrinho
    with open(ARQUIVO_CARRINHOS, "w") as f:
        json.dump(dados, f, indent=4)

def mostrar_carrinho(carrinho):
    total = 0
    print("\nSeu carrinho:")
    for produto_id, qtd in carrinho.items():
        produto = produtos[int(produto_id)]
        subtotal = produto["preco"] * qtd
        print(f"{produto['nome']} - {qtd}x - R${subtotal:.2f}")
        total += subtotal
    print(f"Total: R${total:.2f}")

def finalizar_compra(user_id):
    carrinho = carregar_carrinho(user_id)
    if not carrinho:
        print("Carrinho vazio.")
        return
    mostrar_carrinho(carrinho)
    print("✅ Compra finalizada!")
    salvar_carrinho(user_id, {})  # usado para limpar o carrinho

def sistema_supermercado(user_id):
    carrinho = carregar_carrinho(user_id)
    print(f"\n🛒 Bem-vindo ao Supermercado, {user_id}!")

    if carrinho:
        print("Você tem itens salvos no carrinho:")
        mostrar_carrinho(carrinho)

    while True:
        print("\nProdutos disponíveis:")
        for id_prod, dados in produtos.items():
            print(f"{id_prod} - {dados['nome']} - R${dados['preco']:.2f}")
        print("0 - Finalizar compra")
        print("-1 - Sair e salvar carrinho")

        try:
            escolha = int(input("Escolha o ID do produto: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if escolha == 0:
            finalizar_compra(user_id)
            break

        elif escolha == -1:
            salvar_carrinho(user_id, carrinho)
            print("🛒 Carrinho salvo. Até a próxima!")
            break

        elif escolha in produtos:
            try:
                qtd = int(input(f"Quantas unidades de {produtos[escolha]['nome']}? "))
                if qtd <= 0:
                    print("Quantidade inválida.")
                    continue
                carrinho[str(escolha)] = carrinho.get(str(escolha), 0) + qtd
                print(f"{qtd}x {produtos[escolha]['nome']} adicionado(s) ao carrinho.")
            except ValueError:
                print("Digite uma quantidade válida.")
        else:
            print("Produto inválido.")

        salvar_carrinho(user_id, carrinho)

if __name__ == "__main__":
    menu()
