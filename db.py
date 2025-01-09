import psycopg2

def update_stats(spared_names, killed_names):
    """ Update stats based on the name """    

    rates = {}
    
    try:
        with  psycopg2.connect("dbname='fofdb' user='postgres' host='localhost' password='postgres'") as conn:
            with  conn.cursor() as cur:
                for subject in spared_names:
                    cur.execute(f"SELECT deaths, spares FROM stats WHERE name='{subject}'")
                    record = cur.fetchone()
                    if not record:
                        cur.execute(f"INSERT INTO stats(name, deaths, spares) VALUES ('{subject}', 0, 1)")
                        rates[subject] = 1
                    else:
                        deaths = int(record[0])
                        spares = int(record[1])
                        
                        spares += 1
                        cur.execute(f"UPDATE stats SET spares = {spares} WHERE name = '{subject}'")
                        rates[subject] = spares / (deaths + spares)
                for subject in killed_names:
                    cur.execute(f"SELECT deaths, spares FROM stats WHERE name='{subject}'")
                    record = cur.fetchone()
                    if not record:
                        cur.execute(f"INSERT INTO stats(name, deaths, spares) VALUES ('{subject}', 1, 0)")
                        rates[subject] = 0
                    else:
                        deaths = int(record[0])
                        spares = int(record[1])
                        
                        deaths += 1
                        cur.execute(f"UPDATE stats SET deaths = {deaths} WHERE name = '{subject}'")
                        rates[subject] = spares / (deaths + spares)
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return rates

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "lotterybotdbsecret"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    # Your code goes here.
