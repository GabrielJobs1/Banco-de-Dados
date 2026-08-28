import os
class Carro:
    
    def __init__(self,placa="",nome="",modelo="",valor=0.0):
        self.placa = placa
        self.nome = nome
        self.modelo = modelo
        self.valor = valor
        



def inserir(c):
    arquivo_novo = (not os.path.exists("Lista.txt") or os.path.getsize("Lista.txt") == 0)
    
    with open("Lista.txt","a", encoding ="utf-8") as ptr:
        
        if arquivo_novo:
            ptr.write(f"{'PLACA':<10} | {'NOME':<15} | {'MODELO':<15} | {'VALOR':>10}\n")
            ptr.write("-" * 58 + "\n")
        
        ptr.write(f"{c.placa:<10} | {c.nome:<15} | {c.modelo:<15} | {c.valor:>10.0f}\n")



def deletar(placa_busca):
    try:
        with open("Lista.txt","r", encoding="utf-8") as ptr:
            linhas = ptr.readlines()
        removido = False;
        
        with open("Lista.txt","w",encoding="utf-8") as ptr:
            for linha in linhas:
                if placa_busca.upper() in linha.upper():
                    removido = True
                else:
                    ptr.write(linha)
        
        if removido:
            print(f"\n Veículo com placa '{placa_busca}' removido da lista com sucesso!!")
        else:
            print(f"\n Placa '{placa_busca}' não encontrada!")
            
    except FileNotFoundError:
        print(f"O Arquivo Lista.txt não existe!")
    
    
def Consultar():
    try:
        with open("Lista.txt","r",encoding="utf-8") as ptr:
            conteudo = ptr.read()
        
        if conteudo.strip():
            print(conteudo)
        else:
            print("\n A lista de veículos está vazia.")
    
    except FileNotFoundError:
        print("\n O arquivo Lista.txt ainda não existe.")

    
def buscarVeiculo(buscar_veiculo):
    try:
        with open("Lista.txt","r", encoding="utf-8") as ptr:
            linhas = ptr.readlines()
            
        encontrado = False
        
        for linha in linhas:
            if "PLACA" in linha or "---" in linha:
                continue
            
            if buscar_veiculo.upper() in linha.upper():
                if not encontrado:
                    print(f"{'PLACA':<10} | {'NOME':<15} | {'MODELO':<15} | {'VALOR':>10}")
                    print("-"*58)
                    encontrado = True
                print(linha.strip())
                
        if not encontrado:
            print(f"\nVeículo com a placa '{buscar_veiculo}' não foi encontrado!")
        else:
            print("\n")
                
    except FileNotFoundError:
        print("\n O arquivo Lista.txt não foi encontrado!")
    
    
c = Carro()
while True:
    print("\n" + "=" * 25)
    print("    SISTEMA DE CARROS    ")
    print("=" * 25)
    print("1 - Cadastrar Novo Carro")
    print("2 - Remover veículo da Lista")
    print("3 - Consultar Lista")
    print("4 - Buscar por placa")
    print("5 - Sair do Sistema")

    opcao = input("\nDigite a opção desejada: ")

    match opcao:
        case "1":
            print("\n--- CADASTRO DE VEÍCULO ---")
            c.placa = input("Qual a placa do carro? ")
            c.nome = input("Qual o nome do carro? ")
            c.modelo = input("Qual é o modelo do carro? ")
            c.valor = float(input("Qual é o valor do carro? "))
            
            inserir(c)
        case "2":
            placa_busca = input("Qual a placa do veículo a ser removido? ")
            deletar(placa_busca)
        case "3":
            Consultar();
        case "4":
            buscar_veiculo = input("Qual a placa do veículo que você deseja consultar? ")
            buscarVeiculo(buscar_veiculo)
        case "5":
            print("\nEncerrando...")
            break
        
        case _:
            print("\nOpção inválida!")
