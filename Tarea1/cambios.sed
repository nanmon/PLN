### quitar lineas inutiles
s/\(.*\)\.$//g  
###Lineas que terminan con punto
s/=\(.*\)//g   
### lineas que empiezan con =
s/{\(.*\)//g   
### Lineas que empiezan con {
s/\(.*\)<ref\(.*\)//g  
###Lineas que tengan un <ref en alguna parte de la linea
s/\(.*\)}$//g
s/!\(.*\)!!\(.*\)//g

s/\[\[\(.*\)\]\]$//   
###Remover lineas que empiezan con [[ y terminan con ]]

/^$/d  
### Remover lineas vacias


### csv
s/| [0-9]* || ''\(.*\)'' || \(.*\) || \([0-9]*\) <\/tr>/\1,\2,\3/
# Mulholland Drive <td>
s/| [0-9]* || ''\(.*\)'' || \(.*\) <td> \([0-9]*\) <\/tr>/\1,\2,\3/

### quitar texto extra
s/\[\[\(.*\) (.*)|.*\]\]\(,.*,.*\)/\1\2/
# steve mcqueen
s/\(.*,\)\[\[\(.*\) (.*)|.*\]\]\(,.*\)/\1\2\3/

### quitar corchetes
s/\(\]\,\)/, /g
s/\(\[\|\]\)//g
