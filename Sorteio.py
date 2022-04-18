import random
import tkinter
from tkinter import *

import ttkbootstrap
from ttkbootstrap import Style

text: tkinter.Text

def sorteio() -> None:
    pessoas: list[str] = ["Isaac", "João", "Marcus", "Paloma", "Riquelme"]
    grupos: list[int] = list(range(1, 11))
    sorteio: dict = {}
    escolhidos = []
    selecionados = []
    while len(selecionados) != len(grupos):
        for index, pessoa in enumerate(pessoas):
            if pessoa not in escolhidos:
                tema = random.choices(grupos)
                tema2 = random.choices(grupos)
                if tema not in selecionados and tema2 not in selecionados and tema != tema2:
                    sorteio[pessoa] = tema, tema2
                    escolhidos.append(pessoa)
                    selecionados.append(tema)
                    selecionados.append(tema2)
                    sorteio[pessoa] = tema, tema2
    for k, v in sorteio.items():
        text.insert('1.0', f" ☻ {k} pega os temas: {str(v).replace('[', '').replace(']', '').replace('(','').replace(')','')}\n")


def interface(master) -> None:
    global text
    main_container = Frame(master)
    text = Text(main_container, width=40,height=10, font=("Arial", 20))
    text.grid(row=0, column=0, padx=10, pady=5)
    btn = ttkbootstrap.Button(main_container, bootstyle="danger", text="SORTEAR", command=sorteio)
    btn.grid(row=1, column=0, pady=10, padx=20)

    main_container.pack()



if __name__ == '__main__':
    style = Style('darkly')
    master = style.master
    master.title('SORTEIUUUUU')
    interface(master)
    master.geometry("300x250")
    master.mainloop()

