from __future__ import print_function
import csv
import MySQLdb

with open('/home/gregory/apiFeitaTeste/feira.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['longitude'], row['latitude'], row['setcens'], row['areap'], row['cod_dist'],
              row['distrito'], row['cod_subpref'], row['subpref'], row['regiao5'], row['regiao8'],
              row['nome_feira'], row['registro'], row ['logradouro'], row['numero'], row['bairro'], row['referencia'])
        # insert
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="1234", db="apiFeira")
        sql_statement = "INSERT INTO api_feira(longitude, latitude, setcens, areap, " \
                        "cod_dist, distrito, cod_subpref, " \
                        "subpref, regiao5, regiao8, nome_feira, registro, logradouro, " \
                        "numero, bairro, referencia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['longitude'], row['latitude'], row['setcens'], row['areap'], row['cod_dist'], row['distrito'], row['cod_subpref'], row['subpref'], row['regiao5'], row['regiao8'], row['nome_feira'], row['registro'], row ['logradouro'], row['numero'], row['bairro'], row['referencia'])])
        conn.escape_string(sql_statement)
        conn.commit()

