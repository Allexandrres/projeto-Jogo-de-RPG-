import random
import time
import os

# Dados das classes e raças
CLASSES = {
    "guerreiro": {"vida": 100, "ataque": 15, "defesa": 10, "especial": "Golpe Poderoso"},
    "arqueiro": {"vida": 80, "ataque": 20, "defesa": 5, "especial": "Tiro Preciso"},
    "mago": {"vida": 60, "ataque": 25, "defesa": 3, "especial": "Bola de Fogo"}
}

RACAS = ["Humano", "Anão", "Elfo", "Goblin", "Orc", "Dragonato"]

BONUS_RACA = {
    "Humano": {chave: 1 for chave in ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]},
    "Anão": {"forca": 1, "constituicao": 2},
    "Elfo": {"destreza": 2, "inteligencia": 1},
    "Goblin": {"destreza": 2, "forca": -1, "inteligencia": 1},
    "Orc": {"forca": 2, "constituicao": 1, "inteligencia": -1},
    "Dragonato": {"constituicao": 2, "carisma": 1}
}

ITENS = {
    "Poção de Cura": {"tipo": "consumível", "efeito": {"vida": 30}, "descrição": "Recupera 30 pontos de vida"},
    "Poção de Força": {"tipo": "consumível", "efeito": {"ataque": 5}, "descrição": "Aumenta o ataque em 5 por uma batalha"},
    "Armadura de Couro": {"tipo": "equipamento", "efeito": {"defesa": 3}, "descrição": "Aumenta a defesa em 3"},
    "Espada Afiada": {"tipo": "equipamento", "efeito": {"ataque": 5}, "descrição": "Aumenta o ataque em 5"}
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_personagem(nome, classe, raca):
    atributos_base = {
        "forca": random.randint(8, 18),
        "destreza": random.randint(8, 18),
        "constituicao": random.randint(8, 18),
        "inteligencia": random.randint(8, 18),
        "sabedoria": random.randint(8, 18),
        "carisma": random.randint(8, 18)
    }

    # Aplicar bônus de raça
    for atributo, bonus in BONUS_RACA.get(raca, {}).items():
        atributos_base[atributo] += bonus

    personagem = {
        "nome": nome,
        "classe": classe,
        "raca": raca,
        "nivel": 1,
        "experiencia": 0,
        "experiencia_proxnivel": 100,
        "inventario": ["Poção de Cura", "Poção de Cura"],
        "equipamentos": [],
        **CLASSES[classe],
        **atributos_base
    }
    
    # Vida máxima baseada na constituição
    personagem["vida_max"] = personagem["vida"] + (personagem["constituicao"] - 10) * 2
    personagem["vida"] = personagem["vida_max"]
    
    return personagem

def exibir_personagem(personagem):
    limpar_tela()
    print(f"\n{'=' * 40}")
    print(f"{personagem['nome']} - Nível {personagem['nivel']}")
    print(f"Raça: {personagem['raca']} | Classe: {personagem['classe'].capitalize()}")
    print(f"{'=' * 40}")
    print(f"Vida: {personagem['vida']}/{personagem['vida_max']}")
    print(f"Ataque: {personagem['ataque']} | Defesa: {personagem['defesa']}")
    print(f"Especial: {personagem['especial']}")
    print(f"{'=' * 40}")
    print("Atributos:")
    print(f"Força: {personagem['forca']} | Destreza: {personagem['destreza']}")
    print(f"Constituição: {personagem['constituicao']} | Inteligência: {personagem['inteligencia']}")
    print(f"Sabedoria: {personagem['sabedoria']} | Carisma: {personagem['carisma']}")
    print(f"{'=' * 40}")
    print(f"Experiência: {personagem['experiencia']}/{personagem['experiencia_proxnivel']}")
    print(f"{'=' * 40}")
    print("Inventário:")
    if not personagem["inventario"]:
        print("Vazio")
    else:
        for item in personagem["inventario"]:
            print(f"- {item} ({ITENS[item]['descrição']})")
    print(f"{'=' * 40}")
    input("Pressione Enter para continuar...")

def escolher_raca():
    while True:
        limpar_tela()
        print("\n=== Escolha sua Raça ===")
        for i, raca in enumerate(RACAS, 1):
            print(f"{i}. {raca}")
            bonus = BONUS_RACA[raca]
            print("   Bônus:", end=" ")
            for atributo, valor in bonus.items():
                if valor > 0:
                    print(f"+{valor} {atributo.capitalize()}", end=" ")
                else:
                    print(f"{valor} {atributo.capitalize()}", end=" ")
            print()
        
        try:
            escolha = int(input("\nDigite o número da raça escolhida: "))
            if 1 <= escolha <= len(RACAS):
                return RACAS[escolha-1]
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")
        time.sleep(1)

def escolher_classe():
    while True:
        limpar_tela()
        print("\n=== Escolha sua Classe ===")
        for i, (classe, atributos) in enumerate(CLASSES.items(), 1):
            print(f"{i}. {classe.capitalize()}")
            print(f"   Vida: {atributos['vida']} | Ataque: {atributos['ataque']} | Defesa: {atributos['defesa']}")
            print(f"   Habilidade Especial: {atributos['especial']}")
        
        try:
            escolha = int(input("\nDigite o número da classe escolhida: "))
            classes = list(CLASSES.keys())
            if 1 <= escolha <= len(classes):
                return classes[escolha-1]
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")
        time.sleep(1)

def atacar(atacante, defensor, tipo="normal"):
    if tipo == "normal":
        dano_base = atacante["ataque"] - defensor["defesa"]
        variacao = random.randint(-2, 3)
        dano = max(1, dano_base + variacao)
    elif tipo == "especial":
        dano_base = int(atacante["ataque"] * 1.5) - defensor["defesa"]
        variacao = random.randint(0, 5)
        dano = max(3, dano_base + variacao)
    elif tipo == "defesa":
        dano_base = max(1, (atacante["ataque"] // 2) - defensor["defesa"])
        variacao = random.randint(-1, 1)
        dano = max(0, dano_base + variacao)
    
    defensor["vida"] -= dano
    return dano

def usar_item(personagem, item_nome):
    if item_nome in personagem["inventario"]:
        item = ITENS[item_nome]
        personagem["inventario"].remove(item_nome)
        
        if item["tipo"] == "consumível":
            for atributo, valor in item["efeito"].items():
                if atributo == "vida":
                    personagem["vida"] = min(personagem["vida"] + valor, personagem["vida_max"])
                else:
                    personagem[atributo] += valor
            print(f"Você usou {item_nome}!")
            return True
    return False

def exibir_inventario(personagem):
    limpar_tela()
    print("\n=== Inventário ===")
    if not personagem["inventario"]:
        print("Seu inventário está vazio.")
    else:
        for i, item in enumerate(personagem["inventario"], 1):
            print(f"{i}. {item} - {ITENS[item]['descrição']}")
    
    print("\n0. Voltar")
    
    while True:
        try:
            escolha = int(input("\nEscolha um item para usar (ou 0 para voltar): "))
            if escolha == 0:
                return False
            elif 1 <= escolha <= len(personagem["inventario"]):
                item_escolhido = personagem["inventario"][escolha-1]
                return usar_item(personagem, item_escolhido)
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número.")

def verificar_vitoria(jogador, inimigo):
    if jogador["vida"] <= 0:
        return "derrota"
    elif inimigo["vida"] <= 0:
        return "vitoria"
    return None

def ganhar_experiencia(personagem, quantidade):
    personagem["experiencia"] += quantidade
    print(f"Você ganhou {quantidade} pontos de experiência!")
    
    if personagem["experiencia"] >= personagem["experiencia_proxnivel"]:
        personagem["nivel"] += 1
        personagem["experiencia"] -= personagem["experiencia_proxnivel"]
        personagem["experiencia_proxnivel"] = int(personagem["experiencia_proxnivel"] * 1.5)
        
        # Aumentar atributos
        personagem["vida_max"] += 10
        personagem["vida"] = personagem["vida_max"]
        personagem["ataque"] += 2
        personagem["defesa"] += 1
        
        print(f"\nParabéns! Você subiu para o nível {personagem['nivel']}!")
        print("Seus atributos aumentaram!")
        time.sleep(2)

def batalha(jogador, inimigo):
    limpar_tela()
    print(f"\n{'=' * 50}")
    print(f"BATALHA: {jogador['nome']} vs {inimigo['nome']}")
    print(f"{'=' * 50}")
    
    # Chance de encontrar item
    if random.random() < 0.3:
        item_encontrado = random.choice(list(ITENS.keys()))
        jogador["inventario"].append(item_encontrado)
        print(f"Você encontrou um(a) {item_encontrado}!")
    
    defesa_ativa = False
    especial_usado = False
    
    while True:
        # Resetar estado de defesa a cada turno
        if defesa_ativa:
            jogador["defesa"] = jogador["defesa"] / 1.5
            defesa_ativa = False
        
        # Mostrar status
        print(f"\n{jogador['nome']}: HP {jogador['vida']}/{jogador['vida_max']}")
        print(f"{inimigo['nome']}: HP {inimigo['vida']}/{inimigo['vida_max']}")
        
        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Usar Habilidade Especial" + (" (já usado nesta batalha)" if especial_usado else ""))
        print("3. Defender")
        print("4. Usar Item")
        
        try:
            acao = int(input("Digite o número da ação: "))
            
            if acao == 1:  # Atacar
                dano = atacar(jogador, inimigo)
                print(f"\nVocê causou {dano} de dano no inimigo!")
                
            elif acao == 2:  # Habilidade Especial
                if not especial_usado:
                    dano = atacar(jogador, inimigo, "especial")
                    print(f"\nVocê usou {jogador['especial']} e causou {dano} de dano no inimigo!")
                    especial_usado = True
                else:
                    print("\nVocê já usou sua habilidade especial nesta batalha!")
                    continue
                    
            elif acao == 3:  # Defender
                jogador["defesa"] = jogador["defesa"] * 1.5
                defesa_ativa = True
                print("\nVocê está em posição defensiva! Sua defesa aumentou temporariamente.")
                
            elif acao == 4:  # Usar Item
                if exibir_inventario(jogador):
                    pass  # Item foi usado
                else:
                    continue  # Voltou sem usar item
                
            else:
                print("Ação inválida. Tente novamente.")
                continue
                
        except ValueError:
            print("Por favor, digite um número.")
            continue
        
        # Turno do inimigo
        if inimigo["vida"] > 0:
            # IA simples para o inimigo
            acao_inimigo = random.randint(1, 10)
            
            if acao_inimigo <= 7:  # 70% chance de atacar
                dano_tipo = "normal"
                if defesa_ativa:
                    dano_tipo = "defesa"
                dano = atacar(inimigo, jogador, dano_tipo)
                print(f"O inimigo causou {dano} de dano em você!")
                
            elif acao_inimigo <= 9:  # 20% chance de usar especial
                dano = atacar(inimigo, jogador, "especial")
                print(f"O inimigo usou {inimigo['especial']} e causou {dano} de dano em você!")
                
            else:  # 10% chance de defender
                print("O inimigo está se defendendo!")
        
        # Verificar resultado da batalha
        resultado = verificar_vitoria(jogador, inimigo)
        if resultado:
            if resultado == "vitoria":
                print("\nVocê venceu a batalha!")
                # Recompensas
                xp_ganho = random.randint(20, 50) * inimigo["nivel"]
                ganhar_experiencia(jogador, xp_ganho)
                
                #