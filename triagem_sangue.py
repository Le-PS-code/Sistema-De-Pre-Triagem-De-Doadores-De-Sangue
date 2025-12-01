def main():
    print("--- SISTEMA DE PRÉ-TRIAGEM DE DOADORES DE SANGUE ---")
    print("Responda as perguntas abaixo para verificar sua aptidão básica.\n")

    # Coleta de Dados do Usuário
    # O input coleta os dados digitados pelo usuário
    nome = input("Digite seu nome completo: ")
    
    try:
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso (em kg): "))
    except ValueError:
        print("\n[ERRO] Por favor, digite apenas números para idade e peso.")
        return

    # Perguntas de Sim/Não (Lógica Booleana)
    print("\nResponda com 'S' para Sim ou 'N' para Não:")
    
    sentindo_bem = input("Sente-se bem de saúde hoje? ").upper()
    dormiu_bem = input("Dormiu pelo menos 6 horas nas últimas 24h? ").upper()
    bebeu_alcool = input("Ingeriu bebida alcoólica nas últimas 12h? ").upper()
    tatuagem_recente = input("Fez tatuagem ou piercing nos últimos 12 meses? ").upper()

    # Processamento / Validação das Regras (Baseado em normas da ANVISA)
    # Variável de controle (flag) que começa verdadeira e Lista de motivos vazia
    apto = True
    motivos_inaptidao = []

    # Regra 1: Idade (16 a 69 anos)
    if idade < 16 or idade > 69:
        apto = False
        motivos_inaptidao.append(f"Idade ({idade} anos) fora da faixa permitida (16-69).")

    # Regra 2: Peso (Mínimo 50kg)
    if peso < 50:
        apto = False
        motivos_inaptidao.append(f"Peso ({peso}kg) abaixo do mínimo exigido (50kg).")

    # Regra 3: Estado de saúde e descanso
    if sentindo_bem != 'S':
        apto = False
        motivos_inaptidao.append("Não está se sentindo bem de saúde.")
    
    if dormiu_bem != 'S':
        apto = False
        motivos_inaptidao.append("Não dormiu o mínimo de 6 horas.")

    # Regra 4: Impedimentos temporários (Álcool e Tatuagem)
    if bebeu_alcool == 'S':
        apto = False
        motivos_inaptidao.append("Ingestão de álcool recente (últimas 12h).")
        
    if tatuagem_recente == 'S':
        apto = False
        motivos_inaptidao.append("Tatuagem/Piercing recente (últimos 12 meses).")

    # Saída de Resultados
    print("\n" + "="*40)
    print(f"RESULTADO DA TRIAGEM PARA: {nome.upper()}")
    
    if apto:
        print("STATUS: APTO PARA TRIAGEM CLÍNICA")
        print("Dirija-se ao balcão de atendimento com seu documento oficial.")
    else:
        print("STATUS: INAPTO TEMPORARIAMENTE OU DEFINITIVAMENTE")
        
        # Verifica a quantidade de motivos para decidir entre singular e plural
        if len(motivos_inaptidao) == 1:
            print("Motivo identificado:")
        else:
            print("Motivos identificados:")
            
        for motivo in motivos_inaptidao:
            print(f"- {motivo}")
            
    print("="*40)
    print("Nota: Este software é uma ferramenta de pré-triagem e não substitui a avaliação médica presencial.")

# Executa o programa
if __name__ == "__main__":
    main()
