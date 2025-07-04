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

## ✅ Resultados
![image](https://github.com/user-attachments/assets/099b5989-b5e3-46a7-84ca-92cc22d011cc)
![image](https://github.com/user-attachments/assets/0c165424-df2d-4a35-9f68-9715f44b8f48)
![image](https://github.com/user-attachments/assets/749a1894-d870-4c9f-a56f-4dab86b61e14)
![image](https://github.com/user-attachments/assets/268eeb82-ca92-4dcf-9e6e-dd543c74addb)
![image](https://github.com/user-attachments/assets/c9512f6c-2958-498c-b125-c10bfab5df0b)
![image](https://github.com/user-attachments/assets/54cf47f0-a4a7-4033-b325-65f5e21340cc)





