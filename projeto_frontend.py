from abc import ABC, abstractclassmethod
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Classes de animais
class Animal(ABC):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @abstractclassmethod
    def mostrar(self):
        pass

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade


class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte

    def setPorte(self, porte):
        self.__porte = porte

    def getPorte(self):
        return self.__porte

    def mostrar(self):
        return f"O cachorro {self.getNome()}, de {self.getIdade()} anos, do porte: {self.getPorte()} foi adicionado!"


class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def setRaca(self, raca):
        self.__raca = raca

    def getRaca(self):
        return self.__raca

    def mostrar(self):
        return f"O gato {self.getNome()}, de {self.getIdade()} anos, da raça: {self.getRaca()} foi adicionado!"


# Variáveis e funções globais
lista = []

def salvar(animal):
    lista.append(animal)

def atualizarListbox():
    listbox.delete(0, tk.END)  # Limpa a listbox
    for animal in lista:
        listbox.insert(tk.END, animal.mostrar())  # Adiciona cada animal na listbox

def cadastrarAnimal():
    nome = entryNome.get()
    idade = entryIdade.get()
    porte_raca = entryPorte.get()
    tipo = varTipo.get()  # Obtém o tipo selecionado

    if tipo == "Cachorro":
        c = Cachorro(nome, idade, porte_raca)
        salvar(c)
    elif tipo == "Gato":
        g = Gato(nome, idade, porte_raca)
        salvar(g)

    messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso!")


# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Animal")
janela.geometry("800x600")

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

# Tab Cadastro
tab1 = ttk.Frame(janelinha)
tab1.grid_rowconfigure(5, weight=1)
tab1.grid_columnconfigure(1, weight=1)
janelinha.add(tab1, text="Cadastro")

# Tab Lista
tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(1, weight=1)
tab2.grid_columnconfigure(0, weight=1)
janelinha.add(tab2, text="Lista")

# Widgets de Cadastro
tk.Label(tab1, text="Nome:", font=("", 25)).grid(row=0, column=0, sticky="w", padx=10)
entryNome = tk.Entry(tab1, font=("", 25))
entryNome.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Idade:", font=("", 25)).grid(row=1, column=0, sticky="w", padx=10)
entryIdade = tk.Entry(tab1, font=("", 25))
entryIdade.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Porte/Raça:", font=("", 25)).grid(row=2, column=0, sticky="w", padx=10)
entryPorte = tk.Entry(tab1, font=("", 25))
entryPorte.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo:", font=("", 25)).grid(row=3, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Cachorro")
tk.Radiobutton(tab1, text="Cachorro", font=("", 25), variable=varTipo, value="Cachorro").grid(row=3, column=1, sticky="w", padx=10, pady=5)
tk.Radiobutton(tab1, text="Gato", font=("", 25), variable=varTipo, value="Gato").grid(row=3, column=1, sticky="e", padx=10, pady=5)

tk.Button(tab1, text="Cadastrar", font=("", 25), command=cadastrarAnimal).grid(row=4, columnspan=2)

# Widgets de Lista
listbox = tk.Listbox(tab2, font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizarListbox).grid(row=1, column=0)

# Loop da Janela
janela.mainloop()
