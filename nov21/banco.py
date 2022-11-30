import psycopg2

try: 
    conn = psycopg2.connect(host = "localhost", port = "5435", database = "postgres", user = "teste", password = 123456 )
    print("deu boa")

except:
    print("deu ruim")

if conn:
    print("conexão ruim")

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE lalalala (id serial PRIMARY KEY, nome VARCHAR(15), sobreNome VARCHAR(15));")
    
    print("criastes a tabela jovem")
    conn.commit()
    cursor.close()
    conn.close()