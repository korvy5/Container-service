import mysql.connector
from app.database import db_config
from app.auth import get_password_hash

def init_database():
    config = db_config.copy()
    config.pop('database', None)
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS atk")
        cursor.execute("USE atk")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS containers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                container_number CHAR(11) UNIQUE NOT NULL,
                cost DECIMAL(10,2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                INDEX idx_container_number (container_number),
                INDEX idx_cost (cost)
            )
        """)
        
        conn.commit()
        print("База данных и таблицы успешно созданы")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_database()