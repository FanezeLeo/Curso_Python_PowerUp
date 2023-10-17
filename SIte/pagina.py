#ctrl + C no terminal para fechar o site q tava compilando
import flet as ft

#def cria uma função, essa função vai ser uma pagina do site
def main(pagina):
    #função pra criar um texto
    texto = ft.Text('Chat')

    #Caixa de texto que o usuario coloca seu nome
    nomeUsuario = ft.TextField(label="Escreva seu nome")

    campoMensagem = ft.TextField(label="Digite uma mensagem")
    botaoEnviarMensagem = ft.ElevatedButton("Enviar")

    #Abre o Popup
    def entrarChat(e):
        pagina.dialog = popup
        #abre o popup
        popup.open = True
        #atualiza a pagina
        pagina.update()

        #botão de entrar, on_click para evento ao clicar
    botaoIniciar = ft.ElevatedButton("Iniciar chat", on_click=entrarChat)

    #ação de quando apertamos o botão entrar do popup
    def entrarPopup(e):
        #Fecha o Popup e o botão iniciar
        popup.open = False
        pagina.remove(botaoIniciar)
        #Cria o campo mensagem
        pagina.add(campoMensagem)
        #Botão de enviar mensagem
        pagina.add(botaoEnviarMensagem)
        pagina.update()

    #cria um pop-up
    popup = ft.AlertDialog(
        open = False,
        modal=True,
        title=ft.Text("Bem Vindo ao chat!!!"),
        content=nomeUsuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrarPopup)],
        )
    

    #para a função funcionar tem q colocar um add.o nome da pagina
    pagina.add(texto)
    pagina.add(botaoIniciar)


#função que faz a pagina que a gente criou compilar
#view=ft.WEB_BROWSER faz o programa abrir no navegador padrão do seu pc
ft.app(target=main)