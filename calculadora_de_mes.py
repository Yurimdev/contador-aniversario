from datetime import date

hoje = date.today()

aniversario = input("Qual seu aniversário? (dd/mm): ")
dia, mes = map(int, aniversario.split('/'))

aniversario_ano = date(hoje.year, mes, dia)
if hoje > aniversario_ano:
    print("Já passaram", (hoje - aniversario_ano).days, "dias do seu aniversário.")
elif hoje == aniversario_ano:
    print("Parabéns! Hoje é seu aniversário!")
else:
    print("Seu aniversário é daqui", (aniversario_ano - hoje).days, "dias.")