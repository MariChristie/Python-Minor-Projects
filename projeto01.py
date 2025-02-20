
import tkinter as tk


janela = tk.Tk()
janela.title("Calculadora")

visor = tk.Entry(janela, width=20, font=("Arial", 20), justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def adicionar_texto(numero):
    visor.insert(tk.END, numero)

def calcular_resultado():
    try:
        expressao = visor.get()
        if "/0" in expressao:
            raise ZeroDivisionError
        resultado = eval (expressao)
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro: Divisão por -")
    except:
        visor.delete(0,tk.END)
        visor.insert(tk.END, "Erro")

def limpar_visor():
    visor.delete(0, tk.END)

def apagar():
    texto = visor.get()  
    visor.delete(0, tk.END)  
    visor.insert(tk.END, texto[:-1])

botoes = []
for i in range(10):
        botao = tk.Button(janela, text=str(i), width=5, height=2, font=("Arial", 15),
                    command=lambda num=i: adicionar_texto(num))
        botoes.append(botao)

for i in range(1,10):
    botoes[i].grid(row=(2 + (i - 1) // 3), column=(i - 1)%3)

botoes[0].grid(row=5, column=1)

operadores = ["+", "-", "*", "/",]
for i, operador in enumerate(operadores):
    botao = tk.Button(janela, text=operador, width=5, height=2, font=("Arial", 15), 
                      command=lambda op=operador: adicionar_texto(op))
    botao.grid(row=i + 1, column=3)

for i in range(1,10):
    botoes[i].grid(row=(2 + (i - 1) // 3), column=(i - 1)%3)

botao_limpar = tk.Button(janela, text="C", width=3, height=2, font=("Arial", 15), command=limpar_visor)
botao_limpar.grid(row=1, column=2)

botao_igual = tk.Button(janela, text="⌫", width=5, height=2, font=("Arial", 15), command=apagar)
botao_igual.grid(row=1, column=1)

botao_igual = tk.Button(janela, text="=", width=5, height=2, font=("Arial", 15), command=calcular_resultado)
botao_igual.grid(row=5, column=3)

botao_igual = tk.Button(janela, text=".", width=5, height=2, font=("Arial", 15), command=calcular_resultado)
botao_igual.grid(row=1, column=0)


janela.mainloop()


