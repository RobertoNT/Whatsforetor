from  tkinter import *
from  MenuAplicacion import *
def main():
        """Ejecuta el programa"""
        principal=Tk()
        principal.title('Whatsforetor')
        principal.iconbitmap('wats.ico')
        principal.geometry("700x700")
        menu= MenuAplicacion(principal)
        menu.barra_menu()
        menu.botones()
        menu.cuadro_resultados()
        principal.mainloop()

if __name__ =='__main__':
    main()
