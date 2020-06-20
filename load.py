
plt . dispersión ( np . array ( datos [: 50 , 0 ]), np . array ( datos [: 50 , 2 ]), marcador = 'o' , etiqueta = 'setosa' )
plt . dispersión ( np . array ( datos [ 50 :, 0 ]), np . array ( datos [ 50 :, 2 ]), marcador = 'x' , etiqueta = 'versicolor' )
plt . xlabel ( 'longitud del pétalo' )
plt . ylabel ( 'longitud sepal' )
plt . leyenda ()
plt . show ()