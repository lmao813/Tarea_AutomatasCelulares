# 📝 Modelo de difusión de una enfermedad usando ACs probabilísticos.

## 🎯 Objetivo
Simular cómo se propaga una enfermedad infecciosa en una población distribuida en una cuadrícula, usando un autómata celular probabilístico.

## 📐 Definición del modelo
La cuadrícula es de 100 x 100 “celdas” que representan personas.  
Cada celda puede estar en uno de tres estados:  
* 🟢 S (Susceptible): sana, pero puede infectarse.  
* 🔴 I (Infectada): está enferma y puede contagiar.
* ⚫ R (Recuperada): ya pasó la enfermedad, no se vuelve a infectar.

## 🔁 Reglas de transición
* Si la celda está en estado 🟢 S, y al menos un vecino está infectado, se infecta con probabilidad p_infect.
* Si la celda está en estado 🔴 I, pasa a estado ⚫ R con probabilidad p_recover (representa el tiempo variable de recuperación).
* Si está en ⚫ R, permanece en ese estado.

## ⚙️ Parámetros
* p_infect = 0.2 (probabilidad de contagio por paso si hay un infectado en la vecindad).
* p_recover = 0.1 (probabilidad de recuperarse en cada paso de tiempo).
* Vecindad: Moore (8 vecinos alrededor).

## 🖥️ Código en Python 
https://colab.research.google.com/drive/1lWLDi2xWKr6wIRyh7VMT0_75u8vsBGqC?usp=sharing
