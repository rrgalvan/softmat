import numpy as np
import matplotlib.pylab as plt


class TortugaBasica(object):
    """
    Clase Tortuga: impementa geometría a partir de un puntero gráfico
    """
    def __init__(self, posicion=[0, 0], orientacion=[0, 1],
                    color='blak'):
        """Constructor a partir de su orientación y su posición"""
        self.posicion = np.array(posicion, dtype='d')
        self.orientacion = np.array(orientacion, dtype='d')
        self.pluma_abajo = True
        self.color = color

    def info(self):
        "Imprime información sobre la tortuga"
        print("Posición: %s" % (self.posicion))
        print("Orientación: %s" % (self.orientacion))
        print("Pluma abajo: %i" % (self.pluma_abajo))

    def __str__(self):
        return "Tortuga: P=%s, v=%s, p_a=%i" % (self.posicion, self.orientacion, self.pluma_abajo)

    def avanza(self, distancia):
        self.posicion += distancia*self.orientacion

    def derecha(self, angulo):
        M = np.array([
            [ np.cos(angulo), np.sin(angulo)],
            [-np.sin(angulo), np.cos(angulo)]])
        self.orientacion = np.dot(M, self.orientacion)

    def izquierda(self, angulo):
        self.derecha(-angulo)

class TortugaInteractiva(TortugaBasica):
    """Tortuga básica que dibuja una línea cada vez que avanza"""
    def __init__(self, axis, posicion=[0, 0], orientacion=[0, 1],
                 color="black"):
        super().__init__(posicion, orientacion, color)
        self.ax = axis

    def avanza(self, distancia):
        posicion_anterior = self.posicion.copy()
        super(TortugaInteractiva, self).avanza(distancia)
        if(self.pluma_abajo):
            self.ax.plot([posicion_anterior[0], self.posicion[0]],
                         [posicion_anterior[1], self.posicion[1]])

class TortugaConMemoria(TortugaBasica):
    """Tortuga básica que 'recuerda' los puntos por los que pasa"""
    def __init__(self, posicion=[0, 0], orientacion=[0, 1],
                 color="black"):
        super().__init__(posicion, orientacion, color)
        self.posicion_inicial = self.posicion.copy()
        self.orientacion_inicial = self.orientacion.copy()
        self.color_inicial = self.color
        self.ruta = [self.posicion.copy()]

    def reiniciar(self):
        """Vaciar la ruta almacenada"""
        # self.ruta = [self.posicion.copy()]
        # self.posicion = self.posicion_inicial.copy()
        # self.orientacion = self.orientacion_inicial.copy()
        # self.color = self.color_inicial
        super().__init__(self.posicion_inicial, self.orientacion_inicial,
                         self.color_inicial)
        self.ruta = [self.posicion.copy()]

    def avanza(self, distancia):
        super(TortugaConMemoria, self).avanza(distancia)
        self.ruta.append(self.posicion.copy())

    def plot(self):
        x = [p[0] for p in self.ruta]
        y = [p[1] for p in self.ruta]
        plt.plot(x, y, color=self.color)

class TortugaConOlfato(TortugaConMemoria):
    """Tortuga con una función olor() que le proporciona el nivel de olor
    a una sustancia (por ejemplo un alimento) en su posición actual"""

    def __init__(self, funcion_olor, posicion=[0, 0], orientacion=[0, 1],
                 color="black"):
        super().__init__(posicion, orientacion, color)
        self.olor = funcion_olor

    def huele_mejor(self):
        if len(self.ruta) > 1:
            Px, Py = self.posicion
            Qx, Qy = self.ruta[-2]
            # print(self.olor(Qx,Qy), "->", self.olor(Px,Py))
            if self.olor(Px, Py) < self.olor(Qx, Qy):
                return True
        else:
            return False
