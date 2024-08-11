"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */"""
 
#Nota: funciona si se ponen los 3 parentesis
def check_balanced_parentheses(expression):
     balanced = bool
     parenthesis_Dict ={
          '(': ')',
          '[': ']',
          '{': '}'
     }

     expression_list = list(expression)
     for i in parenthesis_Dict:
          balanced = False
          for j in expression_list:
               if j == i:
                    if parenthesis_Dict[i] in expression_list:
                         expression_list.remove(i)
                         expression_list.remove(parenthesis_Dict[i])
                         balanced = True
                    else:
                         balanced = False
                         break
                    
          if balanced == False:
               break
     
     if balanced:
          print("Expresion Balanceada")
     else:
          print("Expresion no balanceada")
     
                    
check_balanced_parentheses("({ [a * ( c + d ) ] - 5 }")
          

      