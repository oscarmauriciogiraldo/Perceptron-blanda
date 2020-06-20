
def  perceptrón ( datos , num_iter ):
    características  =  datos [:,: - 1 ]
    etiquetas  =  datos [:, - 1 ]
    
    # establecer pesos a cero
    w  =  np . ceros ( forma = ( 1 , características . forma [ 1 ] + 1 ))
    
    mal clasificado_  = []
  
    para  época  en  rango ( num_iter ):
        mal clasificado  =  0
        para  x , etiqueta  en  zip ( características , etiquetas ):
            x  =  np . insertar ( x , 0 , 1 )
            y  =  np . punto ( w , x . transposición ())
            objetivo  =  1.0  si ( y  >  0 ) más  0.0
            
            delta  = ( etiqueta . elemento ( 0 , 0 ) -  objetivo )
            
            if ( delta ): # mal clasificado
                mal clasificado  + =  1
                w  + = ( delta  *  x )
        
        mal clasificado_ . agregar ( mal clasificado )
    return ( w , mal clasificado_ )
             
num_iter  =  10
w , clasificado erróneamente  =  perceptrón ( datos , número_título )