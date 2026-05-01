from app.db.connection import get_conn

def create_user(name, email, password):
    conn = get_conn()
    cursor = conn.cursor()

    sql = "INSERT INTO tbl_users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)

    cursor.execute(sql, values)
    conn.commit()

    return {"message": "User inserted"}