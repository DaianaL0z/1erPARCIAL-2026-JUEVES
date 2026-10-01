## Ejercicio 1: La Serie de Potencias de Homero

Generar una lista por compresión que contenga 
la cantidad de donas que Homero consume en el infierno.
Por cada dona que Homero consume apareceran
más donas al ritmo de raíz de dos donas 
($\displaystyle \sqrt{2}$) en su suplicio hasta que reviente.  

n = 10

donas = [2**(i/2) for i in range(n)]