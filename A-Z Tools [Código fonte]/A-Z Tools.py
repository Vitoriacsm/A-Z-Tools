import tkinter as tk
import tools


class App:
        # Inicio do programa
    def __init__(self):

            # Janelas das funções
        def repair_windows():
                new_window = tk.Toplevel(app)
                new_window.title('Reparo do Windows')
                new_window.configure(bg='black')
                new_window.resizable(0, 0)
            
                ferramentas = tk.LabelFrame(new_window, text='FERRAMENTAS', bg='black', fg='white' )
                ferramentas.grid(row=0, column=0)

                tk.Button(ferramentas, text='IR', width=10, height=1, bg='#363636', fg='white', command=tools.check).grid(row=0, column=1, sticky='E', pady=5)
                tk.Label(ferramentas, text='CHECAGEM RÁPIDA DA IMAGEM DO SISTEMA', bg='black', fg='white').grid(row=0, column=0, sticky='W', padx=10)

                tk.Button(ferramentas, text='IR', width=10, height=1, bg='#363636', fg='white', command=tools.scan).grid(row=1, column=1, sticky='E', pady=5)
                tk.Label(ferramentas, text='VARREDURA DA IMAGEM DO SISTEMA', bg='black', fg='white').grid(row=1, column=0, sticky='W', padx=10)

                tk.Button(ferramentas, text='IR', width=10, height=1, bg='#363636', fg='white', command=tools.restore).grid(row=2, column=1, sticky='E', pady=5)
                tk.Label(ferramentas, text='RESTAURAR A IMAGEM DO SISTEMA', bg='black', fg='white').grid(row=2, column=0, sticky='W', padx=10)

                tk.Button(ferramentas, text='IR', width=10, height=1, bg='#363636', fg='white', command=tools.sfc).grid(row=3, column=1, sticky='E', pady=5)
                tk.Label(ferramentas, text='CORRIGIR ARQUIVOS CORROMPIDOS DO SISTEMA', bg='black', fg='white').grid(row=3, column=0, sticky='W', padx=10)

        def qrcode_window():
                def gettext():
                    url = link.get('1.0', 'end')
                    name = nome.get('1.0', 'end')
                    name_mod = name.replace('\n', '')
                    tools.make_qrcode(url, name_mod)


                new_window = tk.Toplevel(app)
                new_window.configure(bg='black')
                new_window.title('Criador de QR code')
                new_window.resizable(0, 0)

                maketext = tk.LabelFrame(new_window, text='CRIAR QR CODE', bg='black', fg='white')
                maketext.grid(row=0, column=0, sticky='W')

                tk.Label(maketext, text='Cole a URL:', bg='black', fg='white').grid(row=1, column=0, sticky='W')
                link = tk.Text(maketext, width=40, height=1)
                link.grid(row=1, column=1, sticky='W')

                tk.Label(maketext, text='Nome do QR code:', bg='black', fg='white').grid(row=2, column=0, sticky='W')
                nome = tk.Text(maketext, width=25, height=1)
                nome.grid(row=2, column=1, sticky='W')

                tk.Button(new_window, text='Criar', width=10, height=1, bg='#363636', fg='white', command=gettext).grid(row=3, column=0, sticky='E')

        def ip_window():
                def gettext():
                    result = ip.get('1.0', 'end')
                    x = tools.search_ip(result)

                    def result_window():
                        window = tk.Toplevel(app)
                        window.title('Resultado do IP')
                        window.resizable(0, 0)
                        window.configure(bg='black')

                        result1 = tk.LabelFrame(window, text='IP', bg='black', fg='white')
                        result1.grid(row=0, column=0, sticky='W')
                        result2 = tk.LabelFrame(window, text='ORG', bg='black', fg='white')
                        result2.grid(row=1, column=0, sticky='W')
                        result3 = tk.LabelFrame(window, text='ISP', bg='black', fg='white')
                        result3.grid(row=2, column=0, sticky='W')
                        result4 = tk.LabelFrame(window, text='ASN', bg='black', fg='white')
                        result4.grid(row=3, column=0, sticky='W')
                        result5 = tk.LabelFrame(window, text='TIPO', bg='black', fg='white')
                        result5.grid(row=4, column=0, sticky='W')
                        result6 = tk.LabelFrame(window, text='CONTINENTE', bg='black', fg='white')
                        result6.grid(row=5, column=0, sticky='W')
                        result7 = tk.LabelFrame(window, text='REGIÃO', bg='black', fg='white')
                        result7.grid(row=6, column=0, sticky='W')
                        result8 = tk.LabelFrame(window, text='CAPITAL', bg='black', fg='white')
                        result8.grid(row=7, column=0, sticky='W')
                        result9 = tk.LabelFrame(window, text='LATITUDE', bg='black', fg='white')
                        result9.grid(row=8, column=0, sticky='W')
                        result10 = tk.LabelFrame(window, text='LONGITUDE', bg='black', fg='white')
                        result10.grid(row=9, column=0, sticky='W')
                        result11 = tk.LabelFrame(window, text='GMT', bg='black', fg='white')
                        result11.grid(row=10, column=0, sticky='W')

                        tk.Label(result1, text=x['ip'], bg='black', fg='white', width=50).grid(row=0, column=3, sticky='E')

                        tk.Label(result2, text=x['org'], bg='black', fg='white', width=50).grid(row=1, column=3, sticky='E')

                        tk.Label(result3, text=x['isp'], bg='black', fg='white', width=50).grid(row=2, column=3, sticky='E')

                        tk.Label(result4, text=x['asn'], bg='black', fg='white', width=50).grid(row=3, column=3, sticky='E')

                        tk.Label(result5, text=x['type'], bg='black', fg='white', width=50).grid(row=4, column=3, sticky='E')

                        tk.Label(result6, text=x['continent'], bg='black', fg='white', width=50).grid(row=5, column=3, sticky='E')

                        tk.Label(result7, text=x['region'], bg='black', fg='white', width=50).grid(row=6, column=3, sticky='E')

                        tk.Label(result8, text=x['country_capital'], bg='black', fg='white', width=50).grid(row=7, column=3, sticky='E')

                        tk.Label(result9, text=x['latitude'], bg='black', fg='white', width=50).grid(row=8, column=3, sticky='E')

                        tk.Label(result10, text=x['longitude'], bg='black', fg='white', width=50).grid(row=9, column=3, sticky='E')

                        tk.Label(result11, text=x['timezone_gmt'], bg='black', fg='white', width=50).grid(row=10, column=3, sticky='E')
                    result_window()

                new_window = tk.Toplevel(app)
                new_window.title('Pesquisar IP')
                new_window.resizable(0, 0)
                new_window.configure(bg='black')

                tk.Label(new_window, text='(Digite o IP com os pontos ex: 1.1.1.1)', bg='black', fg='white').grid(row=0, column=1, sticky='N')
                tk.Label(new_window, text='IP:', bg='black', fg='white').grid(row=1, column=0, sticky='W')

                ip = tk.Text(new_window, width=27, height=1)
                ip.grid(row=1, column=1, sticky='W')

                tk.Button(new_window, text='Pesquisar', bg='#363636', fg='white', width=10, height=1, command=gettext).grid(row=2, column=1, sticky='E')

        def cep_window():
                def gettext():
                    result = cep.get('1.0', 'end')
                    result1 = result.strip()
                    y = tools.search_cep(result1)

                    def result_window():
                        window = tk.Toplevel(app)
                        window.title('Resultado do CEP')
                        window.resizable(0, 0)

                        result1 = tk.LabelFrame(window, text='CEP', bg='black', fg='white')
                        result1.grid(row=0, column=0, sticky='W')
                        result2 = tk.LabelFrame(window, text='LOGRADOURO', bg='black', fg='white')
                        result2.grid(row=1, column=0, sticky='W')
                        result3 = tk.LabelFrame(window, text='COMPLEMENTO', bg='black', fg='white')
                        result3.grid(row=2, column=0, sticky='W')
                        result4 = tk.LabelFrame(window, text='BAIRRO', bg='black', fg='white')
                        result4.grid(row=3, column=0, sticky='W')
                        result5 = tk.LabelFrame(window, text='CIDADE', bg='black', fg='white')
                        result5.grid(row=4, column=0, sticky='W')
                        result6 = tk.LabelFrame(window, text='UF', bg='black', fg='white')
                        result6.grid(row=5, column=0, sticky='W')
                        result7 = tk.LabelFrame(window, text='DDD', bg='black', fg='white')
                        result7.grid(row=6, column=0, sticky='W')
                        result8 = tk.LabelFrame(window, text='IBGE', bg='black', fg='white')
                        result8.grid(row=7, column=0, sticky='W')

                        tk.Label(result1, text=y['cep'], bg='black', fg='white', width=50).grid(row=0, column=3, sticky='E')

                        tk.Label(result2, text=y['logradouro'], bg='black', fg='white', width=50).grid(row=1, column=3, sticky='E')

                        tk.Label(result3, text=y['complemento'], bg='black', fg='white', width=50).grid(row=2, column=3, sticky='E')

                        tk.Label(result4, text=y['bairro'], bg='black', fg='white', width=50).grid(row=3, column=3, sticky='E')

                        tk.Label(result5, text=y['localidade'], bg='black', fg='white', width=50).grid(row=4, column=3, sticky='E')

                        tk.Label(result6, text=y['uf'], bg='black', fg='white', width=50).grid(row=5, column=3, sticky='E')

                        tk.Label(result7, text=y['ddd'], bg='black', fg='white', width=50).grid(row=6, column=3, sticky='E')

                        tk.Label(result8, text=y['ibge'], bg='black', fg='white', width=50).grid(row=7, column=3, sticky='E')
                    result_window()

                new_window = tk.Toplevel(app)
                new_window.title('Pesquisar CEP')
                new_window.resizable(0, 0)
                new_window.configure(bg='black')

                tk.Label(new_window, text='(Digite o cep com apenas números)', bg='black', fg='white').grid(row=0, column=2, sticky='N')
                tk.Label(new_window, text='CEP: ', bg='black', fg='white').grid(row=1, column=0, sticky='W')
                cep = tk.Text(new_window, width=25, height=1)
                cep.grid(row=1, column=2, sticky='W')
                tk.Button(new_window, text='Pesquisar', width=10, height=1, bg='#363636', fg='white', command=gettext).grid(row=2, column=2, sticky='E')

            # Janela inicial / Menu
        app = tk.Tk()
        app.title('A-Z Tools')
        app.resizable(0, 0)
        app.configure(bg='black')

        botoes = tk.LabelFrame(app, text='FERRAMENTAS', bg='black', fg='white')
        botoes.configure(bg='black')
        botoes.grid(row=0, column=0, sticky='N')

        menu = tk.LabelFrame(app, text='INFO', bg='black', fg='white')
        menu.grid(row=0, column=3, sticky='N')
        tk.Label(menu, text='By: MarchPy', bg='black', fg='white').grid(row=1, column=2, sticky='W')
        tk.Label(menu, text='Version: 1.0.0', bg='black', fg='white').grid(row=2, column=2, sticky='W')
        tk.Label(menu, text='GitHub: https://github.com/MarchPy', bg='black', fg='white').grid(row=3, column=2, sticky='W')

            # Botão 1
        tk.Button(botoes, text='IR', width=8, bg='#363636', fg='white', command=repair_windows).grid(row=1, column=1, sticky='E', padx=2, pady=3)
        tk.Label(botoes, text='CORREÇÃO DO WINDOWS', bg='black', fg='white').grid(row=1, column=0, sticky='W')

            # Botão 2
        tk.Button(botoes, text='IR', width=8, bg='#363636', fg='white', command=qrcode_window).grid(row=2, column=1, sticky='E', padx=2, pady=3)
        tk.Label(botoes, text='CRIAR QR CODE', bg='black', fg='white').grid(row=2, column=0, sticky='W')
            
            # Botão 3
        tk.Button(botoes, text='IR', width=8, bg='#363636', fg='white', command=ip_window).grid(row=3, column=1, sticky='E', padx=2, pady=3)
        tk.Label(botoes, text='PESQUISAR IP', bg='black', fg='white').grid(row=3, column=0, sticky='W')
            
            # Botão 4
        tk.Button(botoes, text='IR', width=8, bg='#363636', fg='white', command=cep_window).grid(row=4, column=1, sticky='E', padx=2, pady=3)
        tk.Label(botoes, text='PESQUISAR CEP', bg='black', fg='white').grid(row=4, column=0, sticky='W')

        tk.Label(app, text='---> Leia o arquivo txt antes de usar. <---', bg='black', fg='white').grid(row=5, column=3, sticky='N')

        app.mainloop()

if __name__ == '__main__':
    App()
else:
    print('Error')
    