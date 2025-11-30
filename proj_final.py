from pathlib import Path

veiculoExemplo = {
    "ano": 1998,
    "placa": "AAA-8888",
    "modelo": "Gol",
    "aluguelDia": 89.9
}



y = 's'
NUM_VEICULOS = 5

def escreveArquivoVeiculos(frota: list[dict]):
    caminho = Path("veiculos.txt")

    with caminho.open("w", encoding="utf-8") as arq:
        for v in frota:
            linha = f"{v['ano']};{v['placa']};{v['modelo']};{v['aluguelDia']}\n"
            arq.write(linha)

    print("Arquivo salvo com sucesso.")

def preencheInfoVeiculo():

    ano = int(input('ano do veículo '))
    placa = str(input('placa ')).upper()
    modelo = str(input('modelo '))
    aluguelDia = float(input('aluguelDia '))

    veiculo = {
    "ano": ano,
    "placa": placa,
    "modelo": modelo,
    "aluguelDia": aluguelDia
    }

    return veiculo

def leArquivoVeiculos() -> list[dict]:
    caminho = Path("veiculos.txt")

    if not caminho.exists():
        print("Arquivo de veículos não encontrado.")
        return []

    frota = []
    with caminho.open("r", encoding="utf-8") as arq:
        for linha in arq:
            ano, placa, modelo, aluguel = linha.strip().split(";")
            frota.append({
                "ano": int(ano),
                "placa": placa,
                "modelo": modelo,
                "aluguelDia": float(aluguel)
            })

    print("Arquivo carregado com sucesso.")
    return frota

def atualizaVeiculo(frota: list[dict], placa: str):
    indice = consultaVeiculo(frota, placa)

    if indice == -1:
        print("Veículo não encontrado.")
        return

    veiculo = frota[indice]

    print("Digite os novos dados (pressione Enter para manter o valor atual):")

    novo_modelo = input(f"Modelo [{veiculo['modelo']}]: ")
    novo_ano = input(f"Ano [{veiculo['ano']}]: ")
    novo_aluguel = input(f"Aluguel/dia [{veiculo['aluguelDia']}]: ")

    if novo_modelo.strip():
        veiculo["modelo"] = novo_modelo
    if novo_ano.strip():
        veiculo["ano"] = int(novo_ano)
    if novo_aluguel.strip():
        veiculo["aluguelDia"] = float(novo_aluguel)

    print("Veículo atualizado com sucesso.")

def imprimeVeiculo(veiculo: dict):
    print("----- Dados do veículo -----")
    print(f"Modelo     : {veiculo.get('modelo')}")
    print(f"Placa      : {veiculo.get('placa')}")
    print(f"Ano        : {veiculo.get('ano')}")
    aluguelDia = veiculo.get("aluguelDia")

    if aluguelDia is None:
        print("Aluguel/Dia: não informado")
    else:
        print(f"Aluguel/Dia: R$ {aluguelDia:.2f}")


def calculaPrecoTotal(frota: list[dict]) -> float:
    total = 0.0
    for i in frota:
        total += float(i.get("aluguelDia"))
    return total



def consultaVeiculo(frota: list[dict], placa: str) -> int:
    placa = placa.strip().upper()
    for i, v in enumerate(frota):
        if v.get("placa", "").upper() == placa:
            return i
    return -1



def main():

    frota= []
    global y
    while y == 's':
        print(
    '''
    1. Cadastra veículo
    2. Consulta veículo
    3. Preço total da frota
    4. Mais novo ao preço de
    5. Sair    
    6. Salvar veículos em arquivo
    7. Carregar veículos do arquivo
    8. Atualizar veículo
    ''')

        x =int(input('o que você gostaria de fazer '))
        if x == 1:
            if len(frota) >= NUM_VEICULOS:
                print("Limite de veículos atingido.")
            else:
                novo = preencheInfoVeiculo()
                frota.append(novo)
                print("Veículo cadastrado com sucesso.")
        if x == 2:
            placa = input("Digite a placa: ")
            indice = consultaVeiculo(frota, placa)
            if indice == -1:
                print("Veículo não encontrado.")
            else:
                imprimeVeiculo(frota[indice]) 
        if x == 3:
            total = calculaPrecoTotal(frota)
            print(f"Preço total da frota por 1 dia: R$ {total:.2f}")
        if x == 4:
            valor = float(input("Mostrar veículos com aluguel menor que: "))
            mais_novo = None

            for v in frota:
                if v["aluguelDia"] < valor:
                    if (mais_novo is None) or (v["ano"] > mais_novo["ano"]):
                        mais_novo = v

            if mais_novo is None:
                print("Nenhum veículo atende ao valor informado.")
            else:
                imprimeVeiculo(mais_novo)
        if x == 5:
            print('obrigado!')
            break
        if x == 6:
            escreveArquivoVeiculos(frota)

        if x == 7:
            frota = leArquivoVeiculos()

        if x == 8:
            placa = input("Placa do veículo a atualizar: ")
            atualizaVeiculo(frota, placa)

        
        y = str(input('Continuar [s/n] '))
 
    



if __name__ == '__main__':
    main()
   

    
            

    