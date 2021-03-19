import sys
import os
import csv
import re
import xlsxwriter
from gensim.models import Word2Vec
from gensim.models import FastText

entrada = "cancelacion"

prueba1 = ['comunidades','normatividad','negras','palenqueras','vulnerables','indigena','raizales','reinsercion','reinsercien','condicidn','desplazada','exceptuando','resguardo','leyes','provengan','anticorrupcion','presidencial','moreno','excepcin','excepcion']
prueba2 = ['formato','calificacion','admision','documentacion','admisien','admisidn','transferencia','evaluaciones','inscripcien','inscripcidn','faltantes','homologables','permanecer','homologaciones','formulario','matricularse','autorizadas','justificacion','cursadas','solicitud','reingresos']
prueba3 = ['cursar','cursaba','cursadas','proceso','evaluaciones','homologables','permanecer','homologable','academicamente','parciales','pendientes','reingreso','reingresen','culminara','homologaciones','academicamente','materias','estudiadas','amnistias','aprobaron','validas','retirado','reingrese']
prueba4 = ['aprobar','sanciones','ingresar','equivalencias','bajo','disciplinarias','regular','incurra','incurrir','reincidencia','regular','reingresen','continuar','concluir','disciplinarias','incurrido','monitoria','promedio']
prueba5 = ['matricular','cursar','asignaturas','equivalentes','electivas','curso','calificacien','calificacion','matriculado','porcentaje','creditos','horaria','hora','carga','estudiante','promedio','practica','electivas','asignaturas','aprobar','acumulado','semestre']
prueba6 = ['calificacien','calificacion','ponderaciones','evaluacien','evaluacion','pesos','exposicion','resultado','criterio','corte','individual','exposiciones','oral','prueba','derecho','cronograma','pruebas','evaluacin']
prueba7 = ['fechas','inscribirse','inscripcion','traslado','transferencia','solicitud','inscripcien','documentos','admision','admisien','calendario','inscripciones','solicitar','amnistia','traslado','reingresen','candidatos','admision','reingresos','equivalencias','formulario','formato','fechas']
prueba8 = ['matriculado','pagar','llamados','formulario','beneficiaro','bancaria','situacion','justificada','monto','costo','estratos','fuerza','excepcin','excepcion','becas','exenciones','beca','tarifa','tarifas']
prueba9 = ['admitidos','cupo','inscripcien','proceso','matriculados','financiera','cohorte','excepcien','valor','plazo','semestral','recargo','calendario','traslado','transferencia','econemicos','econonomicos','costo','recargo','valor','pago']
prueba10 = ['cancelar','cancelacien','cancelaciones','condicien','condicion','solicitar','examenes','matriculado','historial','matricule','limite','estipuladas','validaciones','adiciones','perdida']

pruebas =[prueba1 , prueba2, prueba3, prueba4, prueba5, prueba6, prueba7,prueba8, prueba9, prueba10]
entradas =["afrocolombianas","equivalencias","homologacion","rendimiento","asignatura","calificacion","reingreso","exencion","matricula","cancelacion"]

workbook = xlsxwriter.Workbook('AuxiliarPruebasCbowFT.xlsx')
worksheet = workbook.add_worksheet()

fila = 0 
col = 0
for j in range(len(pruebas)):
    fila = 0
    worksheet.write(fila,col,"pruebas"+str(j+1))
    fila = fila+1
    for i in range(7):

        contador = 0
        model = FastText.load("C:/Users/Mateo/Documents/OCR/modelosAutogenerados/FTCbow/FTCBoW"+str(i)+".model")

        try:
            top = model.wv.most_similar(entradas[j],topn=30)   
            for palabra,valor in top:
                if palabra in pruebas[j]:
                    contador = contador + 1
        except:
            print("La palabra no existe en este modelo")    


        worksheet.write(fila,col,contador)
        fila = fila+1
    col = col+1       
workbook.close()