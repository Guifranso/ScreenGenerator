import tkinter as tk
from tkinter import filedialog
import subprocess
from Tela import Tela
import os

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "script.ps1")

def on_submit():
    pasta_rota = folder_entry.get()
    tela = Tela(
        componente_label.get(), 
        numero_label.get(), 
        funcao_label.get(), 
        sistema_label.get(), 
        url_label.get()
    )
    if pasta_rota == "" or tela.nome == "":
        label.config(text="Por favor, preencha todos os campos", fg="red")
    else:
        subprocess.run([
            "powershell.exe", script_path, 
            "-pasta_rota", pasta_rota, 
            "-tela_nome", tela.nome, 
            "-tela_numero", tela.numero,
            "-tela_funcao", tela.funcao,
            "-tela_sistema", tela.sistema,
            "-tela_url", tela.url
        ])
        label.config(text="Arquivos criados com sucesso!", fg="green")

def browse_folder():
    pasta_rota = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, pasta_rota)

root = tk.Tk()
root.geometry("450x320")
root.configure(bg="white")
root.title("Criar Pasta e Arquivos")

folder_label = tk.Label(root, text="Caminho da pasta:", bg="white")
folder_label.pack()
folder_entry = tk.Entry(root, bd=1, relief="solid", width=60)
folder_entry.pack()
folder_button = tk.Button(root, text="Procurar", command=browse_folder, bg="#009688", fg="white", borderwidth=0, width=51)
folder_button.pack()

componente_label = tk.Label(root, text="Componente da tela:", bg="white")
componente_label.pack()
componente_label = tk.Entry(root, bd=1, relief="solid", width=60)
componente_label.pack()

numero_label = tk.Label(root, text="Numero da tela:", bg="white")
numero_label.pack()
numero_label = tk.Entry(root, bd=1, relief="solid", width=60)
numero_label.pack()

funcao_label = tk.Label(root, text="Funcao da tela:", bg="white")
funcao_label.pack()
funcao_label = tk.Entry(root, bd=1, relief="solid", width=60)
funcao_label.pack()

sistema_label = tk.Label(root, text="Sistema da tela:", bg="white")
sistema_label.pack()
sistema_label = tk.Entry(root, bd=1, relief="solid", width=60)
sistema_label.pack()

url_label = tk.Label(root, text="URL da tela:", bg="white")
url_label.pack()
url_label = tk.Entry(root, bd=1, relief="solid", width=60)
url_label.pack()

submit_button = tk.Button(root, text="Enviar", command=on_submit, bg="#009688", fg="white", borderwidth=0, width=51)
submit_button.pack()

label = tk.Label(root, bg="white")
label.pack()

root.mainloop()