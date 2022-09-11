
import tkinter as tk
import cv2

def catRecognizion():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')  
      
    cap = cv2.VideoCapture(0)  
      
    while 1:  
      
        
        ret, img = cap.read()  
      
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
      
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
      
        for (x,y,w,h) in faces:  
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
            roi_gray = gray[y:y+h, x:x+w]  
            roi_color = img[y:y+h, x:x+w]  
      
      
        
        cv2.imshow('img',img)  
      
        
        k = cv2.waitKey(30) & 0xff
        if k == 27: 
            print("cerrar")
            break
      
    cap.release()  
      
    cv2.destroyAllWindows()  

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.title(self,"Biblioteca OpenCV")
        tk.Tk.iconbitmap(self, "icono.ico")
       
        self._frame = None
        self.switch_frame(StartPage)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self,
                      text = "Biblioteca OpenCV",
                      font = ("Bahnschrift semibold", 20),
                      bd = 1, relief = "sunken").grid(row = 1, column = 1, padx = 10, pady = 20)

        tk.Label(self,
                      text = "Ginneidy Leon - 20192020077",
                      font = ("Bahnschrift", 18),
                      bd = 1, relief = "sunken").grid(row = 2, column = 1, padx = 10, pady = 5)

        tk.Button(self, text = "Definición", command = lambda: master.switch_frame(DescriptionPage),  font = ("Bahnschrift", 18)).grid(row = 3, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Historia", command = lambda: master.switch_frame(HistoryPage), font = ("Bahnschrift", 18)).grid(row = 3, column = 2, padx = 20, pady = 20)
        tk.Button(self, text = "Usos", command = lambda: master.switch_frame(UsesPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Funcionalidades", command = lambda: master.switch_frame(FunctionPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 2, padx = 20, pady = 20)
     

class HistoryPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,width=100, height =100)
        tk.Frame.config(self,width=100, height =100)
        tk.Label(self,
                        text = "Historia Biblioteca OpenCV",
                        font = ("Bahnschrift semibold", 20),
                        bd = 1, relief="sunken",).grid(row = 0, column = 1, pady = 20, padx = 10)


        tk.Label(self,
                        text = "Desde que aparecio su primera versión alfa en el mes de enero de 1999, se ha utilizado en infinidad de aplicaciones. Desde sistemas de"+
                        "seguridad con detección de \nmovimiento, hasta aplicativos de control de procesos donde se requiere reconocimiento de objetos. Esto se debe a que"+
                        " su publicación se da bajo \nlicencia BSD, que permite que sea usada libremente para propósitos comerciales y de investigación con las condiciones"+
                        " en ella expresadas.",
                        font = ("Bahnschrift", 18),
                        bd = 1, relief="sunken",
                        justify = tk.LEFT).grid(row = 1, columnspan = 3, pady = 20, padx = 10)

        tk.Label(self,
                         text = "Hitos",
                         font = ("Bahnschrift semibold", 20),
                         bd = 1, relief="sunken").grid(row = 2, column = 1, pady = 20, padx = 10)

        tk.Label(self,
                 text = "•Alfa, 1999\n  •Liberado al público en 2000"+
                 "\n•2.0, Octubre de 2009\n  •Adopcion de C++, iniciando un proceso que concluirá en la versión 2.4.9"+
                 "•2.4.9, abril de 2014\n  •Concluye el proceso de adopción a C++\n  •Esta versión brinda soporte completo y mixto a C y C++"+
                 "\n  •Se continuó desarrollando hasta la 2.4.13"+
                 "\n•3.0, junio de 2015\n  •Versión dedicada a C++, abandonando el soporte a C.\n  •El soporte a C continua en las versiones 2.4.x, que siguen desarrollando en paralelo."+
                 "\n•4.0, noviembre de 2018\n  •Versión escrita enteramente en C++, abandonando todos los elementos expresados en C.\n  •Quitaron gran parte de funciones obsoletas, que cuentan con alternativas superiores más modernas.",
                 font = ("Bahnschrift", 18),
                 bd = 1, relief="sunken",
                 justify = tk.LEFT).grid(row = 3, column = 1, pady = 20, padx = 10)
        
        tk.Button(self, text = " ⬅", command = lambda: master.switch_frame(StartPage), font = ("Bahnschrift", 18)).grid(row = 0, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Descripción", command = lambda: master.switch_frame(DescriptionPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Usos", command = lambda: master.switch_frame(UsesPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 1, padx = 20, pady = 20)
        tk.Button(self, text = "Funcionalidades", command = lambda: master.switch_frame(FunctionPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 2, padx = 20, pady = 20)

class UsesPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self,
                 text = "Usos de la biblioteca OpenCV",
                 font = ("Bahnschrift semibold", 20),
                 bd = 1, relief="sunken",).grid(row = 0, column = 1, pady = 20, padx = 10)


        tk.Label(self,
                 text = "Las areas de aplicación de la biblioteca de OpenCV incluyen:"+
                 "\n  •Caracteristicas 2D y 3D.\n  •Estimación de pose de cámara.\n  •Reconocimiento facial.\n  •Reconocimiento de gestos."+
                 "\n  •Interacción persona - computadora.\n  •Robótica móvil.\n  •Comprensión de movimientos.\n  •Reconocimiento de objetos."+
                 "\n  •Segmentación.\n  •Estereoscopía.\n  •Structure from motion.\n  •Tracking.\n  •Realidad aumentada.",
                 font = ("Bahnschrift", 18),
                 bd = 1, relief="sunken",
                 justify = tk.LEFT).grid(row = 1, column = 1, pady = 20, padx = 10)

        tk.Label(self,
                 text = "Aplicaciones en las que es utilizada",
                 font = ("Bahnschrift semibold", 20),
                 bd = 1, relief="sunken").grid(row = 2, column = 1, pady = 20, padx = 10)

        tk.Label(self,
                 text = "• SwisTrack: Herramienta para rastrear robots, humanos, animales y objetos y utilizando una cámara"+
                 " o un video grabado como fuente de entrada. Utiliza la biblioteca \nIntel OpenCV para el procesamiento rápido de imágenes y contiene interfaces para cámaras USB, FireWire y GigE, así como archivos AVI."+
                 "\n• Usada en el sistema de visión del vehículo no tripulado Stanley de la Universidad de Stanford, el ganador en el año 2005 del Gran desafio DARPA.",
                 font = ("Bahnschrift", 18),
                 bd = 1, relief="sunken",
                 justify = tk.LEFT).grid(row = 3, columnspan = 3, pady = 20, padx = 10)
        
        tk.Button(self, text = " ⬅", command = lambda: master.switch_frame(StartPage), font = ("Bahnschrift", 18)).grid(row = 0, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Descripción", command = lambda: master.switch_frame(DescriptionPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Historia", command = lambda: master.switch_frame(HistoryPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 1, padx = 20, pady = 20)
        tk.Button(self, text = "Funcionalidades", command = lambda: master.switch_frame(FunctionPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 2, padx = 20, pady = 20)


class DescriptionPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        
        
        tk.Label(self,
                 text = "OpenCV",
                 font = ("Bahnschrift semibold", 20),
                 bd = 1, relief="sunken",).grid(row = 0, column = 1, pady = 20, padx = 10)

        tk.Label(self,
                 text = "Es una biblioteca informática de código abierto desarrollada originalmente por la visión de Intel con una numerosa cantidad de algoritmos, especializada en visión \nartificial y machine learning "+
                 ". Es gratuita para uso comercial y la investigación bajo una licencia BSD. La biblioteca es multiplataforma"+
                 "y funciona en Mac OSX, Windows \ny Linux. Se centra principalmente hacia procesamiento imagen tiempo real",
                 font = ("Bahnschrift", 18),
                 bd = 1, relief="sunken",
                 justify = tk.LEFT).grid(row = 1, columnspan = 3, pady = 20, padx = 10)
        
        tk.Button(self, text = " ⬅", command = lambda: master.switch_frame(StartPage), font = ("Bahnschrift", 18)).grid(row = 0, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Usos", command = lambda: master.switch_frame(UsesPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Historia", command = lambda: master.switch_frame(HistoryPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 1, padx = 20, pady = 20)
        tk.Button(self, text = "Funcionalidades", command = lambda: master.switch_frame(FunctionPage), font = ("Bahnschrift", 18)).grid(row = 4, column = 2, padx = 20, pady = 20)
       
class FunctionPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self,
                 text = "Funcionalidad",
                 font = ("Bahnschrift semibold", 20),
                 bd = 1, relief="sunken",).grid(row = 0, column = 1, pady = 20, padx = 10)
    
    
        tk.Label(self,
                 text = "Se propone un aplicativo mediante el uso de OpenCV con el cual se pueda desarrollar un sistemas de"+
                 "alimentación para animales \ncomo, perros, gatos. Con el uso de esta biblioteca se busca que mediante"+
                 " sus funcionalidades de reconocimiento se pueda \nidentificar en los puestos de comida, que animal se acerca"+
                 " y asi mismo dispensar la comida correcta segun el animal identificado.",
                 font = ("Bahnschrift", 18),
                 bd = 1, relief="sunken",
                 justify = tk.LEFT).grid(row = 1, columnspan = 3, pady = 20, padx = 10)

        tk.Button(self, text = " ⬅", command = lambda: master.switch_frame(StartPage), font = ("Bahnschrift semibold", 18)).grid(row = 0, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Gatos", command = catRecognizion,  font = ("Bahnschrift semibold", 18)).grid(row = 2, column = 0, padx = 20, pady = 20)
        tk.Button(self, text = "Perros", command = lambda: master.switch_frame(StartPage),  font = ("Bahnschrift semibold", 18)).grid(row = 2, column = 2, padx = 20, pady = 20)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()