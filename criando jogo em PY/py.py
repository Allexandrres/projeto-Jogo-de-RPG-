import random

def criar_personagem(nome, classe, raca):
    atributos = {
        "guerreiro": {"vida": 100, "ataque": 15, "defesa": 10},
        "arqueiro": {"vida": 80, "ataque": 20, "defesa": 5},
        "mago": {"vida": 60, "ataque": 25, "defesa": 3}
    }
    
    fichas = {
        "forca": random.randint(8, 18),
        "destreza": random.randint(8, 18),
        "constituicao": random.randint(8, 18),
        "inteligencia": random.randint(8, 18),
        "sabedoria": random.randint(8, 18),
        "carisma": random.randint(8, 18)
    }

    if raca == "Humano":
        fichas = {chave: valor + 1 for chave, valor in fichas.items()}
    elif raca == "Anão":
        fichas["forca"] += 1
        fichas["constituicao"] += 1
    elif raca == "Elfo":
        fichas["destreza"] += 1
        fichas["inteligencia"] += 1
    elif raca == "Goblin":
        fichas["destreza"] += 2
    elif raca == "Orc":
        fichas["forca"] += 2
    elif raca == "Dragonato":
        fichas["constituicao"] += 2

    return {
        "nome": nome,
        "classe": classe,
        "raca": raca,
        "vida": atributos[classe]["vida"],
        "ataque": atributos[classe]["ataque"],
        "defesa": atributos[classe]["defesa"],
        **fichas
    }

def escolher_raca():
    racas = ["Humano", "Anão", "Elfo", "Goblin", "Orc", "Dragonato"]
    raca = ""
    while raca not in racas:
        raca = input(f"Escolha sua raça ({', '.join(racas)}): ").capitalize()
    return raca

def atacar(atacante, defensor):
    dano = max(0, atacante["ataque"] - defensor["defesa"] + random.randint(-2, 2))
    defensor["vida"] -= dano
    return dano

def verificar_vitoria(jogador, inimigo):
    if jogador["vida"] <= 0:
        return "Você perdeu!"
    elif inimigo["vida"] <= 0:
        return "Você venceu!"
    return None

def jogar():
    nome = input("Digite o nome do seu personagem: ")
    classe = ""
    while classe not in ["guerreiro", "arqueiro", "mago"]:
        classe = input("Escolha sua classe (guerreiro, arqueiro, mago): ").lower()

    raca = escolher_raca()
    
    jogador = criar_personagem(nome, classe, raca)
    inimigo = criar_personagem("Inimigo", random.choice(["guerreiro", "arqueiro", "mago"]), random.choice(["Humano", "Anão", "Elfo", "Goblin", "Orc", "Dragonato"]))

    print(f"Seu personagem: {jogador}")
    print(f"Inimigo: {inimigo}")

    while True:
        acao = ""
        while acao not in ["atacar"]:
            acao = input("Digite sua ação (atacar): ").lower()

        if acao == "atacar":
            dano = atacar(jogador, inimigo)
            print(f"Você causou {dano} de dano no inimigo!")

        if inimigo["vida"] > 0:
            dano = atacar(inimigo, jogador)
            print(f"O inimigo causou {dano} de dano em você!")

        resultado = verificar_vitoria(jogador, inimigo)
        if resultado:
            print(resultado)
            break

jogar()
