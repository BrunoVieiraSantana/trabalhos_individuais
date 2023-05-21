# Bibliotecas para interface gráfica
import customtkinter
import tkinter
import tkinter.ttk as ttk
from CTkMessagebox import CTkMessagebox
import re

# Bibliotecas para importação de imagens
from PIL import Image

# Importação dos códigos sql de um arquivo externo
from database import *


# Variaveis de controle
login=False

# Classe principal do aplicativo
class App(customtkinter.CTk):

    #Tamanhp da janela
    width = 800
    height = 600
    
    # Definir tema padrão
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("green")

    def __init__(self):
        super().__init__()

        # Nomear a Janela,defir o tamanho, bloquear o tamanho da janela
        self.title("Biblioteca.py")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # Carregar imagens utilizadas no projeto
        self.logo_image = customtkinter.CTkImage(Image.open("imagens\_athena.png"), size=(120, 120))
        self.plus_image = customtkinter.CTkImage(Image.open("imagens\plus-outline.png"), size=(25, 25))
        self.shild_image = customtkinter.CTkImage(Image.open("imagens\shield-crown-outline.png"), size=(25, 25))
        
        self.bg_image =  customtkinter.CTkImage(Image.open("imagens\image.png"), size=(800, 600))

        # Background
        self.background_frame = customtkinter.CTkLabel(self, text= "", image=self.bg_image)
        self.background_frame.grid(row=0, column=0,)

        # Tela de Login
        self.login_frame = customtkinter.CTkFrame(self.background_frame, corner_radius=0,fg_color="#11E8B5")
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_frame_logo_label = customtkinter.CTkLabel(self.login_frame, compound="left",image=self.logo_image, anchor="n", text="",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_frame_logo_label.grid(row=0, pady=(40,5))
        self.login_frame_label = customtkinter.CTkLabel(self.login_frame , text="Biblioteca Athenas",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_frame_label.grid(row=1, pady=(5,30))
        self.login_frame_username_entry = customtkinter.CTkEntry(self.login_frame , width=200, placeholder_text="login")
        self.login_frame_username_entry.grid(row=2, pady=5, padx=(30,30))
        self.login_frame_password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.login_frame_password_entry.grid(row=3, pady=5)
        self.login_frame_login_button = customtkinter.CTkButton(self.login_frame, text="Login",command=self.button_login_user, width=200,text_color=("gray10", "gray90"),border_color=("gray10", "gray90"), border_width=1)
        self.login_frame_login_button.grid(row=4, pady=5)
        self.login_frame_forgot_pass_button = customtkinter.CTkButton(self.login_frame, text="Esqueceu sua senha?",command=self.forgot_pass,hover=False, width=200, fg_color="transparent", text_color=("gray10", "gray90"))
        self.login_frame_forgot_pass_button.grid(row=5, pady=5)
        self.login_frame_new_user_button = customtkinter.CTkButton(self.login_frame, text="Criar conta",command=self.new_user,hover=False, width=200, fg_color="transparent", text_color=("gray10", "gray90"))
        self.login_frame_new_user_button.grid(row=6, pady=5)
        self.login_frame_admin_button = customtkinter.CTkButton(self.login_frame, text="Administrar     ",compound="left",image=self.shild_image, anchor="n",hover=False, width=200, fg_color="transparent", text_color=("gray10", "gray90"))
        self.login_frame_admin_button.grid(row=7, pady=75)

        # Novo Usuario
        self.new_user_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#11E8B5")
        self.new_user_frame.grid_columnconfigure(0, weight=1)
        self.new_user_frame_label_new_user = customtkinter.CTkLabel(self.new_user_frame , text="""Novo Usuário""",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_user_frame_label_new_user.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.new_user_frame_label_2 = customtkinter.CTkLabel(self.new_user_frame , text="""Digite os dados abaixo""",font=customtkinter.CTkFont(size=15,))
        self.new_user_frame_label_2.grid(row=1, column=0,pady=(20, 5), sticky="n")
        self.new_user_frame_entry_login = customtkinter.CTkEntry(self.new_user_frame , placeholder_text="Login",width=250)
        self.new_user_frame_entry_login.grid(row=2, column=0,  pady=(5, 5), sticky='n')
        self.new_user_frame_entry_senha = customtkinter.CTkEntry(self.new_user_frame , placeholder_text="Senha",width=250)
        self.new_user_frame_entry_senha.grid(row=3, column=0,  pady=(5, 5), sticky='n')
        self.new_user_frame_entry_email = customtkinter.CTkEntry(self.new_user_frame , placeholder_text="E-mail",width=250)
        self.new_user_frame_entry_email.grid(row=5, column=0,  pady=(5,5), sticky='n')
        self.new_user_frame_button_buscar = customtkinter.CTkButton(self.new_user_frame , text="Cadastrar", width=200,text_color=("gray10", "gray90"),border_color=("gray10", "gray90"), border_width=1)
        self.new_user_frame_button_buscar.grid(row=6, column=0,  pady=(5,5), sticky='n')
        self.new_user_frame_button_voltar = customtkinter.CTkButton(self.new_user_frame , text="Voltar",command=self.new_user_event, width=200,text_color=("gray10", "gray90"),border_color=("gray10", "gray90"), border_width=1)
        self.new_user_frame_button_voltar.grid(row=7, column=0,  pady=(5,5), sticky='n')

        # Esqueceu sua senha
        self.forgot_pass_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#11E8B5")
        self.forgot_pass_frame.grid_columnconfigure(0, weight=1)
        self.forgot_pass_frame_label = customtkinter.CTkLabel(self.forgot_pass_frame , text="""Esqueceu sua Senha?""",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.forgot_pass_frame_label.grid(row=0, column=0,pady=(20, 5), sticky="n")
        self.forgot_pass_frame_label_2 = customtkinter.CTkLabel(self.forgot_pass_frame , text="""Digite os dados abaixo""",font=customtkinter.CTkFont(size=15,))
        self.forgot_pass_frame_label_2.grid(row=1, column=0,pady=(20, 5), sticky="n")
        self.forgot_pass_frame_entry_login = customtkinter.CTkEntry(self.forgot_pass_frame , placeholder_text="Login",width=250)
        self.forgot_pass_frame_entry_login.grid(row=2, column=0,  pady=(5, 5), sticky='n')
        self.forgot_pass_frame_entry_email = customtkinter.CTkEntry(self.forgot_pass_frame , placeholder_text="E-mail",width=250)
        self.forgot_pass_frame_entry_email.grid(row=3, column=0,  pady=(5,5), sticky='n')
        self.forgot_pass_frame_button_buscar = customtkinter.CTkButton(self.forgot_pass_frame , border_width=2,text="Buscar", text_color=("gray10", "#DCE4EE"))
        self.forgot_pass_frame_button_buscar.grid(row=4, column=0,  pady=(5,5), sticky='n')
        self.forgot_pass_frame_entry_resultado = customtkinter.CTkEntry(self.forgot_pass_frame , placeholder_text="Resultado da busca",width=250)
        self.forgot_pass_frame_entry_resultado.grid(row=5, column=0,  pady=(5,5), sticky='n')
        self.forgot_pass_frame_button_voltar = customtkinter.CTkButton(self.forgot_pass_frame , border_width=2,text="Voltar",command=self.forgot_pass_envent, text_color=("gray10", "#DCE4EE"))
        self.forgot_pass_frame_button_voltar.grid(row=6, column=0,  pady=(5,5), sticky='n')

        # Home
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0,fg_color="#11E8B5")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame , text="""Que livro deseja alugar?""",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.home_frame_label.grid(row=0, column=0,pady=(5, 5), sticky="n")
        self.home_frame_ajuste = customtkinter.CTkFrame(self.home_frame, corner_radius=0,fg_color="#11E8B5", height=35, width=680)
        self.home_frame_ajuste.grid(row=1, column=0, sticky="we",padx=(10,10))
        self.home_frame_entry_busca_livro = customtkinter.CTkEntry(self.home_frame_ajuste,placeholder_text='Busca por Titulo',width=250)
        self.home_frame_entry_busca_livro.grid(row=1, column=0, sticky='w')
        self.home_frame_entry_busca_autor = customtkinter.CTkEntry(self.home_frame,placeholder_text='Busca por Autor',width=250)
        self.home_frame_entry_busca_autor.grid(row=1, column=0, pady=(5,5), padx=(100,0), sticky='n')
        self.home_frame_button_alugar = customtkinter.CTkButton(self.home_frame,command=self.button_search_livro, border_width=2,text="Buscar",text_color=("gray10", "#DCE4EE"))
        self.home_frame_button_alugar.grid(row=1, column=0, pady=(5,5),padx=(70,15), sticky='e')
        self.home_frame_button_alugar = customtkinter.CTkButton(self.home_frame , border_width=2,text="Alugar",compound="left",image=self.plus_image, anchor="n", text_color=("gray10", "#DCE4EE"))
        self.home_frame_button_alugar.grid(row=3, column=0,  pady=(5,5), sticky='n')
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame , text="""Livros alugados""",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.home_frame_label.grid(row=4, column=0,pady=(5, 0), sticky="n")
        self.home_frame_button_sair = customtkinter.CTkButton(self.home_frame , border_width=2,text="Sair",command=self.logout_event, text_color=("gray10", "#DCE4EE"),fg_color="transparent")
        self.home_frame_button_sair.grid(row=6, column=0,  pady=(5,5), sticky='n')

        # Tabela de Buscas
        columns = ('index','nome', 'autor', 'ano', 'paginas')
        self.table_livro_buscas = ttk.Treeview(self.home_frame, columns=columns, height=10, selectmode='browse', show='headings')

        self.table_livro_buscas.column("#1", anchor="c", minwidth=35, width=35)
        self.table_livro_buscas.column("#2", anchor="c", minwidth=180, width=180)
        self.table_livro_buscas.column("#3", anchor="c", minwidth=160, width=160)
        self.table_livro_buscas.column("#4", anchor="c", minwidth=35, width=35)
        self.table_livro_buscas.column("#5", anchor="c", minwidth=35, width=35)

        self.table_livro_buscas.heading('index', text='ID')
        self.table_livro_buscas.heading('nome', text='Nome')
        self.table_livro_buscas.heading('autor', text='Autor')
        self.table_livro_buscas.heading('ano', text='Ano')
        self.table_livro_buscas.heading('paginas', text='Páginas')
        self.table_livro_buscas.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        self.table_livro_buscas.bind('<Motion>', 'break')

        
        def display_selected_item_visualizar(a):
            selected_item = self.table_livro_buscas.selection()[0]
            id = self.table_livro_buscas.item(selected_item)['values'][0]
            print(f'O id selecionado é {id}')

        self.table_livro_buscas.bind("<<TreeviewSelect>>", display_selected_item_visualizar)

        # Tabela de Alugueis
        columns = ('nome', 'aluguel', 'devolver')
        self.table_livros_alugueis = ttk.Treeview(self.home_frame, columns=columns, height=4, selectmode='browse', show='headings')

        self.table_livros_alugueis.column("#1", anchor="c", minwidth=160, width=160)
        self.table_livros_alugueis.column("#2", anchor="c", minwidth=160, width=160)
        self.table_livros_alugueis.column("#3", anchor="c", minwidth=160, width=160)

        self.table_livros_alugueis.heading('nome', text='Nome')
        self.table_livros_alugueis.heading('aluguel', text='Data de locação')
        self.table_livros_alugueis.heading('devolver', text='Data de Devolução')
        self.table_livros_alugueis.grid(row=5, column=0, sticky='nsew', padx=10, pady=(0,10))
        livros = ["O_Hobbit 16/05/2023 24/05/2023"]
        #verlivro(con)
        for livro in livros:
            self.table_livros_alugueis.insert('', tkinter.END, values=livro)
        

    #Funções de login e logout
    def login_event(self):
        global login
        login = True
        self.login_frame.grid_forget()
        self.home_frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=50)  

    def logout_event(self):
        self.home_frame.grid_forget()
        self.login_frame.grid(row=0, column=0)  
        global login
        login = False

    def new_user_event(self):
        self.new_user_frame.grid_forget()
        self.login_frame.grid(row=0, column=0)          

    def forgot_pass_envent(self):
        self.forgot_pass_frame.grid_forget()
        self.login_frame.grid(row=0, column=0)  

    # Funções tela de login
    def button_login_user(self):
        login = self.login_frame_username_entry.get()
        senha = self.login_frame_password_entry.get()
        if login == "" and senha == "":
            self.login_event()

    def button_login_user_bind(self, event):
        self.login_event()

    def new_user(self):
        self.login_frame.grid_forget()  
        self.new_user_frame.grid(row=0, column=0, sticky="nsew", pady=50, padx=50) 

    def forgot_pass(self):
        self.login_frame.grid_forget() 
        self.forgot_pass_frame.grid(row=0, column=0, sticky="nsew", pady=50, padx=50) 


    # Funções Esqueceu a senha
    def forgot_pass_search(self):
        login = self.forgot_pass_frame_entry_login.get()
        email = self.forgot_pass_frame_entry_email.get()
        resultado = 0
        #esqueceuSenha(con, login, email)
        self.forgot_pass_frame_entry_resultado.delete(0, "end")
        self.forgot_pass_frame_entry_resultado.insert("end", resultado)

    def button_new_user(self):
        login = self.new_user_frame_entry_login.get()
        senha = self.new_user_frame_entry_senha.get()
        email = self.new_user_frame_entry_email.get()

    # Funções Home
    def button_search_livro(self):
        titulo = self.home_frame_entry_busca_livro.get()
        autor = self.home_frame_entry_busca_autor.get()

        lista = []

        if len(autor) == 0:
            my_list = search_book_auto_titulo(con)
            busca = re.compile(f".*{titulo}")
            newlist = list(filter(busca.match, my_list))
            for x in newlist:
                livro = search_book(con, x)
                lista.append(livro)

        elif len(titulo) == 0:
            my_list = search_book_auto_autor(con)
            busca = re.compile(f".*{autor}", re.IGNORECASE)

            newlist = list(filter(busca.match, my_list))

            for x in newlist:
                autor = search_book_autor(con, x)
                lista.append(autor)

        for item in self.table_livro_buscas.get_children():
            self.table_livro_buscas.delete(item)

        for livro in lista:
            self.table_livro_buscas.insert('', tkinter.END, values=livro[0])



app = App()
app.mainloop()