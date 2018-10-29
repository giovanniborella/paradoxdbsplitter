from __future__ import division
from pypxlib import Table
import csv
import math
import sys, getopt

def main(argv):

  try:
    opts, args = getopt.getopt(argv,"hi:o:c:x",["ifile=","ofile=","headers=","headershelp="])
  except getopt.GetoptError:
    print ('paradoxdbsplitter.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
       print ('paradoxdbsplitter.py -i <inputfile> -o <outputfile> -c <headers(hola,adios,pepe)>')
       sys.exit()
    elif opt in ("-x", "--helpheaders"):
      headershelp = 1
    elif opt in ("-i", "--ifile"):
       inputfile = arg
    elif opt in ("-o", "--ofile"):
       outputfile = arg
    elif opt in ("-c", "--headers"):
       cabeceras = arg.split(",")
       print(cabeceras)

    # elif opt in ("-b", "--block"):
    #    bloque = arg

  bloque = 100000
  table = Table(inputfile)

  if 'headershelp' in locals():
    fields = table.fields
    headers = []
    for f in fields:
      headers.append(f)
    #print(headers)
    cabeceras = headers
    #sys.exit()

  registros = len(table)
  print ("Table rows: %s" % registros)
  print ("Rows per file: %d" % bloque)
  print ("File headers to be extracted: %s" % cabeceras)
  print ("File (db) path: %s" % inputfile)

  #print (registros)
  #print (bloque)
  #print (registros/bloque)
  #print (math.ceil(registros/bloque))

  iteraciones = int(math.ceil(registros/bloque))

  print ("File parts about to generate: %s" % iteraciones)

  iteracion = 0

  for iteracion in range(0, iteraciones):

    print ("iteracion numero %s" % iteracion)
    with open(outputfile+"_parte_"+str(iteracion)+".csv", "w") as csvfile:
      print(csvfile)

      spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      # headers
      spamwriter.writerow(cabeceras)
      start = iteracion * bloque
      end = start + bloque
      if end > registros:
        end = registros

      for row in range(start, end):

        #print start
        # FIX encoding here
        # spamwriter.writerow([table[row][s].encode('utf8') if type(table[row][s]) is unicode else table[row][s] for s in cabeceras])
        spamwriter.writerow(table[row][s] for s in cabeceras)

if __name__ == "__main__":
   main(sys.argv[1:])
