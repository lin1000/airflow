import airflow
import json
from airflow.models import Connection

S3_CONN_ID = 'S3_lin1000'

if __name__ == '__main__':
    session = airflow.settings.Session()

    """
    SELECT 
        connection.password AS connection_password, 
        connection.extra AS connection_extra, 
        connection.id AS connection_id,
        connection.conn_id AS connection_conn_id,
        connection.conn_type AS connection_conn_type, 
        connection.host AS connection_host, 
        connection.schema AS connection_schema, 
        connection.login AS connection_login, 
        connection.port AS connection_port, 
        connection.is_encrypted AS connection_is_encrypted, 
        connection.is_extra_encrypted AS connection_is_extra_encrypted
    """

    #print(session.query(Connection).session.query(Connection))
    

    for conn in session.query(Connection).all():
        print(str(conn.id) + "\t" + conn.conn_id + "\t\t" + conn.conn_type + "\t" + str(conn.is_encrypted))
        #print(conn.extra)
    
    print("Total Connections are : " + str(session.query(Connection).session.query(Connection).count()))

    # check if the connection exists
    s3_connection = (
        session.query(Connection)
        .filter(Connection.conn_id == S3_CONN_ID)
        .one())

    if not s3_connection:
        print('Creating connection: {}'.format(S3_CONN_ID))
        session.add(
            Connection(
                conn_id=S3_CONN_ID,
                conn_type='s3',
                extra=json.dumps(dict(
                    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']))))
        session.commit()
        print('Done creating connections.')

