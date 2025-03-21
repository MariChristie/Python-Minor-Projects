import tkinter as tk

#-------------------- Interface inicial --------------------#

janela = tk.Tk()
janela.title("StarrPoker")

visor = tk.Entry(janela, width=20, font=("Arial", 20), justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def adicionar_texto(numero):
    visor.insert(tk.END, numero)

#-------------------- Escolhendo cartas --------------------#


valores_das_cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


#-------------------- Interface de botões --------------------#


botao_jogar = tk.Button(janela, text="Escolher", width=3, height=2, font=("Arial", 15), command=valores_das_cartas)
#botao_limpar.grid(row=1, column=2)


janela.mainloop()
