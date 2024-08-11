"""/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - No se puede utilizar la libreria dateTime
 */"""
 
def dias(fecha1,fecha2):
     #months days
     monthDict = {
          '01': 31, 
          '02': 28, 
          '03': 31, 
          '04': 30, 
          '05': 31, 
          '06': 30,
          '07': 31, 
          '08': 31, 
          '09': 30, 
          '10': 31, 
          '11': 30, 
          '12': 31
     }
     
     fechaList1 = fecha1.split('/')
     fechaList2 = fecha2.split('/')
     
     #fechaList1 variables
     fechaList1_Day = list(fechaList1[0])
     fechaList1_Month = list(fechaList1[1])
     fechaList1_Year = fechaList1[2]
     
     #fechaList2 varaibles
     fechaList2_Day = list(fechaList2[0])
     fechaList2_Month = list(fechaList2[1])
     fechaList2_Year = fechaList2[2]
     
     #remove the 0 into the first digit (fecha1 and fecha2)
     if fechaList1_Day[0] == "0":
          fechaList1_Day.remove("0")
          
     if fechaList2_Day[0] == "0":
          fechaList2_Day.remove("0")
     
     daysDifference = 0
     
     #list to string (days)
     numberFecha1_Day = "".join(fechaList1_Day)
     numberFecha2_Day = "".join(fechaList2_Day)
     
     #list to string (months)
     numberFecha1_Month = "".join(fechaList1_Month)
     numberFecha2_Month = "".join(fechaList2_Month)
     
     
     #operation to find the difference between fecha1 and fecha2
     daysDifference = int(numberFecha2_Day) - int(numberFecha1_Day) #days
     if numberFecha1_Month != numberFecha2_Month:
          daysDifference = int(monthDict[numberFecha1_Month]) + int(monthDict[numberFecha2_Month])-int(monthDict[numberFecha2_Month]) + daysDifference #months
     
     if fechaList1_Year != fechaList2_Year:
          daysDifference = ((int(fechaList2_Year) - int(fechaList1_Year))*365) + daysDifference #year

     print(daysDifference)
          
dias("02/04/2024","03/05/2024")