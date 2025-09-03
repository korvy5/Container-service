import mysql.connector
from app.database import db_config
from app.auth import get_password_hash

def seed_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("USE atk")
    try:
        users = [
            ('user1', get_password_hash('password1')),
            ('user2', get_password_hash('password2')),
            ('user3', get_password_hash('password3'))
        ]
        
        cursor.executemany(
            "INSERT IGNORE INTO users (username, password_hash) VALUES (%s, %s)", users
        )
        
        containers = [
        ('ABCU1234567', 100.50),
        ('DEFU1234567', 200.75),
        ('GHIU3456789', 300.25),
        ('JKLU4567890', 400.00),
        ('MNPU5678901', 500.50),
        ('QSTU6789012', 600.75),
        ('UWXU7890123', 700.25),
        ('YAUU8901234', 800.00),
        ('BCDU9012345', 900.50),
        ('EFGU0123456', 1000.75)
]
        cursor.executemany(
            "INSERT IGNORE INTO containers (container_number, cost) VALUES (%s, %s)", containers
        )
        
        conn.commit()
        print("Тестовые данные добавлены успешно")
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    seed_data()