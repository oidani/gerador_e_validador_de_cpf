import random
import os
import time


def verifica_cpf_inserido(cpf):
    """Retorna True se CPF tiver 11 números e se não forem todos iguais."""
    return len(cpf) == 11 and cpf.isdigit() and cpf.count(cpf[0]) != 11


def calcula_dv(cpf, c):
    """Calcula e retorna dígito verificador do CPF."""
    lista_validacao_dv = []

    for i in range(0, c-1):
        lista_validacao_dv.append(int(cpf[i]) * c)
        c -= 1

    soma_validacao_dv = sum(lista_validacao_dv)
    calculo_dv = soma_validacao_dv % 11

    return 0 if calculo_dv < 2 else 11 - calculo_dv


def compara_dv(cpf, primeiro_dv, segundo_dv):
    """Valida se dígitos verificadores calculados são iguais aos inseridos."""
    return "válido" if primeiro_dv == int(cpf[9]) and segundo_dv == int(cpf[10]) else "inválido"


def converte_cpf(cpf):
    """Realiza conversão e retorna CPF com os separadores ponto e hífen."""
    cpf_convertido = ""

    for i in range(len(cpf)):

        if i in (3, 6):
            cpf_convertido += "." + str(cpf[i])
        elif i == 9:
            cpf_convertido += "-" + str(cpf[i])
        else:
            cpf_convertido += str(cpf[i])

    return cpf_convertido


def verifica_uf(digito_uf):
    """Verifica e retorna UF com base no nono dígito do CPF."""
    dict_uf = {"0": "RS",
               "1": "DF, GO, MS, TO",
               "2": "PA, AM, AC, AM, RO, RR",
               "3": "CE, MA, PI",
               "4": "PE, RN, PB, AL",
               "5": "BA, SE",
               "6": "MG",
               "7": "RJ, ES",
               "8": "SP",
               "9": "PR, SC"}

    return dict_uf[digito_uf]


def gera_cpf():
    """Gera e retorna CPF completo numa lista."""
    cpf = [random.randint(0, 9) for i in range(9)]
    cpf.append(calcula_dv(cpf, 10))
    cpf.append(calcula_dv(cpf, 11))

    return cpf


def limpa_tela():
    """Limpa tela com base no Sistema Operacional utilizado."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    """Solicita informações ao usuário e retorna saída na tela."""
    print("\nGERADOR E VALIDADOR DE CPF")
    print("\nO que você deseja:\n1. Gerar um CPF válido\n2. Validar um CPF\nOBS: para sair, pressione qualquer outra tecla")
    escolha = input("\nEscolha: ")

    if escolha in ("1", "2"):
        limpa_tela()
        if escolha == "1":
            cpf = gera_cpf()

            while cpf.count(cpf[0]) == 11:
                cpf = gera_cpf()

            print("ESCOLHA: 1 - GERAR CPF\n")
            situacao = "válido"
            uf = verifica_uf(str(cpf[8]))
        else:
            print("ESCOLHA: 2 - VALIDAR CPF\n")
            cpf = input("Insira o CPF para validação (apenas números): ")

            print()
            if verifica_cpf_inserido(cpf):
                primeiro_dv = calcula_dv(cpf, 10)
                segundo_dv = calcula_dv(cpf, 11)
                situacao = compara_dv(cpf, primeiro_dv, segundo_dv)
                uf = verifica_uf(str(cpf[8]))
            else:
                situacao = uf = "inválido"

        print(f"CPF      : { converte_cpf(cpf) }")
        print(f"SITUAÇÃO : { situacao }")
        print(f"UF       : { uf }")
        print()
    else:
        print("\nO programa será finalizado.\n")
        time.sleep(2)


if __name__ == "__main__":
    main()
