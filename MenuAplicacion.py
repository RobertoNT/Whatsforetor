from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import Aplicacion as a


class MenuAplicacion:
    """ Esta clase almacena todo el código de las funcionalidades de la aplicacion.

     Attributes:
     contenido (List)
     Contenido_Final (List)

    La variable contenido: almacena una lista con todo el texto del log de whatsapp una vez iniciado sesión con el usuario
    La variable contenido_Final:  es una lista que almacen el texto filtrado de la lista anterior según lo que queremos investigar
    """
    contenido = list()
    contenido_Final = list()
    oscuro=0
    def __init__(self, root=None):
        """ Inicializamos la clase con la ventana principal creada en el método main de la clase aplicación. """

        self.root = root

    def barra_menu(self):
        """Crea la barra de menu superior de la aplicacion junto a sus botones.

        Attributes:

        barra_menu (Menu) es la barra de menu superior de la aplicación

        menu_Archivo (Menu) es el boton Archivo del panel superior que contiene los botones que ejecutan todas las funcionalidades

        menu_ayuda (Menu) es el botón que da te indica como usar la interfaz gráfica de la aplicacion

        menu_ver (Menu) es el botón ver de la barra superior que contiene el boton para ver la aplicación en modo oscuro

        """
        self.barra_menu = Menu(self.root)
        # Se asigna la barra de menu a la ventana principal con este tamaño
        self.root.config(menu=self.barra_menu, width=300, height=300,bg="white")
        # La colocamos en el menu de inicio
        # Los tres menus  del panel que contienen botones en su interior
        self.menu_Archivo = Menu(self.barra_menu, tearoff=0)
        self.menu_ayuda = Menu(self.barra_menu, tearoff=0)
        self.menu_ver = Menu(self.barra_menu, tearoff=0)

        # Le ponemos el nombre al menu
        self.barra_menu.add_cascade(label='Archivo', menu=self.menu_Archivo)
        # Menus:Añadimos los diferentes botones al  menu desplegable y le vinculamos el método que ejecutará al clicar
        # Menu Archivo
        self.menu_Archivo.add_command(label=' Abrir Archivo',
                                 command=self.cargaArchivo)
        self.menu_Archivo.add_command(label='Exportar Archivo',
                                 command=self.exportarArchivo)
        self.menu_Archivo.add_command(label='Ejecutar funcionalidades',
                                 command=self.funcionalidades)

    # Menu ver
        self.barra_menu.add_cascade(label="Ver", menu=self.menu_ver)
        self.menu_ver.add_command(label='modo oscuro', command=self.cambiarOscuro)

        # Menu ayuda
        self.barra_menu.add_cascade(label="Ayuda", command=self.ayuda)

        # barra_menu.add_radiobutton(label="Ayuda",menu=menu_ayuda,command=ayuda())

    def ayuda(self):
        """Este método crea una ventana y muestra la información de como se usa la herramienta

        Attributes:

        ventana_Ayuda (TopLevel)  es la ventana emergente que aparece al presionar el botón de ayuda

        etq_titulo (Label) muestra el contenido dentro de la ventana 
        """
        self.ventana_Ayuda = Toplevel()
        # Añadimos el titulo a la ventana
        self.ventana_Ayuda.title("Ayuda")
        if self.oscuro==1:
            self.ventana_Ayuda.config(background="#2F4F4F")
        # Establecemos el tamaño de la ventana
        self.ventana_Ayuda.geometry("500x200")
        # Etiqueta con la información
        if self.oscuro==1:
            self.etq_ayuda = Label(self.ventana_Ayuda, text=
            """---Funcionalidades de la herramienta---
            
            - En Archivo tienes las funcionalidades de cargar, ejecutar funcionalidades y exportar
            -Si no cargas antes de ejecutar funcionalidades, el programa no hará nada.
            -Si exportas sin cargar las funcionalidades, el programa no hará nada
            -Primero cargas el archivo, seleccionas las funcionalidades en los botones y pulsas en 
            ejecutar funcionalidades. 
            Si deseas una vez realizados estos pasos puedes exportar
            -Dentro de edición puedes cambiar el color de fondo

            Suerte y espero que encuentres lo que buscas""",bg="#2F4F4F",fg="white").pack()
        else:
            self.etq_ayuda = Label(self.ventana_Ayuda, text=
            """---Funcionalidades de la herramienta---
            
            - En Archivo tienes las funcionalidades de cargar, ejecutar funcionalidades y exportar
            -Si no cargas antes de ejecutar funcionalidades, el programa no hará nada.
            -Si exportas sin cargar las funcionalidades, el programa no hará nada
            -Primero cargas el archivo, seleccionas las funcionalidades en los botones y pulsas en 
            ejecutar funcionalidades. 
            Si deseas una vez realizados estos pasos puedes exportar
            -Dentro de edición puedes cambiar el color de fondo

            Suerte y espero que encuentres lo que buscas""").pack()
            
        
    
    def lecturaArchivo(self, nombreArchivo):
        """Lee el log y lo almacena en la variable contenido (list) definida al inicio de la clase.

        Args:

        nombreArchivo (String) es la ruta donde se encuentra el archivo ubicado

        """
        try:
            # Escribir bien la ruta del LOG de Whatsapp
            ##
            palabraClave = ""
            with open(nombreArchivo, encoding="ANSI") as lectura:
                for line in lectura:

                    self.contenido.append(line)

        except:
            return self.contenido

    def cargaArchivo(self):
        """Es el método que muestra la ventana gráfica que se muestra al pusar sobre el botón de cargar archivo. Esta te permite moverte por los directorios del sistema
        hasta encontrar el archivo deseado

        Attributes:

        archivo (filedialog) es la ventana gráfica.

        """
        archivo = filedialog.askopenfilename(
            title="Cargar Archivo", filetypes=(("Archivos de registro", "*.log"),))
        self.lecturaArchivo(archivo)

    def exportarArchivo(self):
        """Es el método que  se encarga de exportar el archivo resultante trás haberlo filtrado.
            Attributes:

            ruta_Archivo (filedialog) se almacena la ventana donde seleccionas la ubicación donde guardar el archivo

            file (TextIOWrapper) crea el fichero donde se escibirán los datos
        """

        if len(self.contenido_Final) == 0:
            return None
        ruta_Archivo = filedialog.asksaveasfilename(title="Guardar como", filetypes=(
            ("Archivo de registro", "*.log"), ("Archivo de texto", "*txt"), ("Archivo PDF", "*.pdf")))

        file = open(ruta_Archivo, "w", encoding="UTF8")

        for i in self.contenido_Final:  # Lee cada dato extraido en el método anterior

            file.write(i)

        file.close()

    def botones(self):
        """Son los botones para indicar a partir de lo que quemos filtrar. """
        self.audio()
        self.documento()
        self.imagen()
        self.video()
        self.ubicacion()
        self.contacto()
        self.reaccion()

    def audio(self):
        """El método que crea el botón de audio.

        Attributes:

        Valor_audio (BooleanVar) almacena el valor del botón si está chequeado es 1
        boton_audio  es la interfaz del botón
        """
        self.valor_audio = tk.BooleanVar()
        if self.oscuro==1:
            self.boton_audio = tk.Checkbutton(
                self.root, text="Audio",bg="#2F4F4F", variable=self.valor_audio).place(relx=0.1, rely=0.1)
        else:
             self.boton_audio = tk.Checkbutton(
                self.root, text="Audio",bg="white", variable=self.valor_audio).place(relx=0.1, rely=0.1)
            
        # boton_audio.pack()

    def documento(self):
        """El método que crea el botón de  documento.

        Attributes:

        valor_documento (BooleanVar) almacena el valor del botón si está chequeado es 1

        boton_documento  es la interfaz del botón
        """

        self.valor_documento = tk.BooleanVar()
        if self.oscuro==0:
            self.boton_documento = tk.Checkbutton(
            self.root, text="documento",bg="white", variable=self.valor_documento).place(relx=0.25, rely=0.1)
        else:
            self.boton_documento = tk.Checkbutton(
            self.root, text="documento",bg="#2F4F4F",variable=self.valor_documento).place(relx=0.25, rely=0.1)
            
        
        # boton_documento.pack()

    def imagen(self):
        """El método que crea el botón de imagen.

        Attributes:

        valor_imagen (BooleanVar) almacena el valor del botón si está chequeado es 1

        boton_imagen  es la interfaz del botón
        """
        self.valor_imagen = tk.BooleanVar()
        if self.oscuro==1:
            self.boton_imagen = tk.Checkbutton(
            self.root, text="imagen",bg="#2F4F4F", variable=self.valor_imagen).place(relx=0.4, rely=0.1)
        else:
            self.boton_imagen = tk.Checkbutton(
            self.root, text="imagen",bg="white", variable=self.valor_imagen).place(relx=0.4, rely=0.1)
        
            
       
       
    def video(self):
        """El método que crea el botón de video.

        Attributes:

        valor_video (BooleanVar) almacena el valor del botón si está chequeado es 1

        boton_video  es la interfaz del botón
        """
        self.valor_video = tk.BooleanVar()
        if self.oscuro==1:
            self.boton_video = tk.Checkbutton(
            self.root, text="video",bg="#2F4F4F", variable=self.valor_video).place(relx=0.55, rely=0.1)
        else:
            self.boton_video = tk.Checkbutton(
            self.root, text="video",bg="white", variable=self.valor_video).place(relx=0.55, rely=0.1)
            
        

    def ubicacion(self):
        """El método que crea el botón de  ubicacion.

        Attributes:

        valor_ubicacion (BooleanVar) almacena el valor del botón si está chequeado es 1

        boton_ubicacion  es la interfaz del botón
        """
        self.valor_ubicacion = tk.BooleanVar()
        if self.oscuro==1:
            self.boton_ubicacion = tk.Checkbutton(
            self.root, text="ubicación",bg="#2F4F4F" ,variable=self.valor_ubicacion).place(relx=0.1, rely=0.2)
        else:
            self.boton_ubicacion = tk.Checkbutton(
            self.root, text="ubicación" ,bg="white",variable=self.valor_ubicacion).place(relx=0.1, rely=0.2)
        
            
        

    def contacto(self):
        """El método que crea el botón de  contacto.

        Attributes:

        valor_contacto (BooleanVar) almacena el valor del botón si está chequeado es 1

        boton_contacto  es la interfaz del botón
        """
        self.valor_contacto = tk.BooleanVar()
        if self.oscuro==1:
            self.bboton_contacto = tk.Checkbutton(
            self.root, text="contacto",bg="#2F4F4F" ,variable=self.valor_contacto).place(relx=0.25, rely=0.2)
        else:
            self.bboton_contacto = tk.Checkbutton(
            self.root, text="contacto" ,bg="white",variable=self.valor_contacto).place(relx=0.25, rely=0.2)
            
        # boton_contacto.pack()

    def reaccion(self):
        """El método que crea el botón de  reacción.

        Attributes:

        valor_reaccion (BooleanVar) almacena el valor del botón si está chequeado es 1

        boton_reaccion  es la interfaz del botón
        """
        self.valor_reaccion = tk.BooleanVar()
        if self.oscuro==1:
            self.boton_reaccion = tk.Checkbutton(
            self.root, text="reaccion", bg="#2F4F4F",variable=self.valor_reaccion).place(relx=0.4, rely=0.2)
        else:
            self.boton_reaccion = tk.Checkbutton(
            self.root, text="reaccion",bg="white",variable=self.valor_reaccion).place(relx=0.4, rely=0.2)
        # boton_reaccion.pack()

    def cuadro_resultados(self):
        """Es el método que crea la pantalla de la pantalla principal del progrma  donde podemos ver todo el texto filtrado 

        Attributes:

        pantalla (ScrolledText) crea la interfaz de la pantalla donde se ve el texto
        """

        self.pantalla = st.ScrolledText(self.root, width=80, heigh=20)
        self.pantalla.place(relx=0.05, rely=0.3, relheight=0.6, relwidth=0.9)
        self.pantalla.configure(state='disabled')

    def mostrarTexto(self):
        
        """Muestra el texto en la pantalla de la pentana principal
        """
        if len(self.contenido_Final) != 0:
            self.pantalla.configure(state='normal')
            for line in self.contenido_Final:
                self.pantalla.insert(END, line)
            self.pantalla.configure(state='disabled')

    def funcionalidades(self):
        """Filtra el texto según los botones pulsados en la aplicación"""

        for line in self.contenido:

            if "WANotification" in line:  # Independientemente el tipo de mensaje aparece esto si es recibido
                self.contenido_Final.append(line)
            if "getHighestAck" in line:  # Independiente del mensaje si es enviado aparece esto#
                self.contenido_Final.append(line)
            if "queryMsgInfo" in line:  # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if "proccessOrphanPeerReceipt" in line:  # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if "line" in line:                        # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if "groupMetadata:" in line:              # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if "@c" in line:                          # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if "@g" in line:                        # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if "msg" in line:                         # Independiente del mensaje si es enviado o recibido aparece esto#
                self.contenido_Final.append(line)
            if self.valor_audio.get():
                if "audio" in line:
                    self.contenido_Final.append(line)
            if self.valor_documento.get():
                if "doc" in line:
                    self.contenido_Final.append(line)
                if "pdf" in line:
                    self.contenido_Final.append(line)
                if "media" in line:
                    self.contenido_Final.append(line)
            if self.valor_video.get():
                if "mp4" in line:
                    self.contenido_Final.append(line)
                if "video" in line:
                    self.contenido_Final.append(line)
                if "media" in line:
                    self.contenido_Final.append(line)
            if self.valor_imagen.get():
                if "png" in line:
                    self.contenido_Final.append(line)
                if "jpeg" in line:
                    self.contenido_Final.append(line)
                if "image" in line:
                    self.contenido_Final.append(line)
                if "media" in line:
                    self.contenido_Final.append(line)
            if self.valor_reaccion.get():
                if "processReactionOrphanPeerReceipt" in line:
                    self.contenido_Final.append(line)
                if "react" in line:
                    self.contenido_Final.append(line)
            if self.valor_contacto.get():
                if "contact" in line:
                    self.contenido_Final.append(line)
                if "vcard" in line:
                    self.contenido_Final.append(line)
            if self.valor_ubicacion.get():
                if "location" in line:
                    self.contenido_Final.append(line)
        self.mostrarTexto()
        
    def cambiarOscuro(self):
        """Cambiar la interfaz de la aplicación a un color verde oscura si esta en modo claro si no cambia a modo claro"""
        if self.oscuro==0:
            self.oscuro=1
            self.root.config(background="#2F4F4F")
            self.pantalla.config(background="#2F4F4F")
            self.audio()
            self.documento()
            self.video()
            self.reaccion()
            self.contacto()
            self.ubicacion()
            self.imagen()
        else:
            self.oscuro=0
            self.root.config(background="white")
            self.pantalla.config(background="white")
            self.audio()
            self.documento()
            self.video()
            self.reaccion()
            self.contacto()
            self.ubicacion()
            self.imagen()
                
            
        
   
        
        
        