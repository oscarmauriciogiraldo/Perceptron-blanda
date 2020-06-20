importar  numpy  como  np
importar  pandas  como  pd
importar  matplotlib . pyplot  como  plt
def  load_data ():
    URL_ = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    datos  =  pd . read_csv ( URL_ , encabezado  =  Ninguno )
    imprimir ( datos )
    
    # hacer que el conjunto de datos sea linealmente separable
    datos  =  datos [: 100 ]
    datos [ 4 ] =  np . donde ( datos . iloc [:, - 1 ] == 'Iris-setosa' , 0 , 1 )
    datos  =  np . asmatriz ( datos , dtype  =  'float64' )
    devolver  datos
data  =  load_data ()