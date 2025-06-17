import streamlit as st
import cv2
import numpy as np
from pyspark.sql import SparkSession


class ProcesamientoImagenes:
    def __init__(self, imagen):
        self.imagen = imagen
    
    def detectar_bordes(self):
        imagen_bin = self.imange
        
        visitados = np.zeros(imagen_bin.shape)
        bordes = np.zeros(imagen_bin.shape)
        
        for i in range(imagen_bin[0]):
            for j in range(imagen_bin.shape[1]):
                if imagen_bin[i][j] == 255 and visitados[i][j] == 0:
                    cola = [(i,j)]
                    visitados[i][j] = 1
                    
                    while cola:
                        pixel = cola.pop(0)
                        es_borde = False
                        
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            ni, nj = pixel[0] + dx, pixel[1] + dy
                            
                            if ni < 0 or ni >= imagen_bin.shape[0] or nj < 0 or nj >= imagen_bin.shape[1]:
                                continue
                            
                            if imagen_bin[ni][nj] == 0:
                                bordes[pixel[0], pixel[1]] = 255
                            elif visitados[ni][nj] == 0:
                                visitados[ni][nj] = 1
                                cola.append((ni, nj))
                        
                        if es_borde:
                            bordes[pixel[0], pixel[1]] = 255
                
        
        return bordes