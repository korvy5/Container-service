from app.database import get_db_connection
from app.schemas import ContainerCreate 
from typing import List, Optional
import mysql.connector

def get_containers(search: Optional[str] = None, limit: int = 50) -> List[dict]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("USE atk")
        
        if search:
            query = "SELECT id, container_number, cost, created_at FROM containers WHERE container_number LIKE %s LIMIT %s"
            cursor.execute(query, (f'%{search}%', limit))
        else:
            query = "SELECT id, container_number, cost, created_at FROM containers LIMIT %s"
            cursor.execute(query, (limit,))  # Исправлено: добавлена запятая
        
        return cursor.fetchall()
    
    finally:
        cursor.close()
        conn.close()

def get_containers_by_cost(exact: Optional[float] = None, min_cost: Optional[float] = None, max_cost: Optional[float] = None) -> List[dict]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("USE atk")
        
        query = "SELECT id, container_number, cost, created_at FROM containers WHERE 1=1"
        params = []
        
        if exact is not None:
            query += " AND cost = %s"  # Добавлен пробел перед AND
            params.append(exact)
        
        if min_cost is not None:
            query += " AND cost >= %s"  # Добавлен пробел перед AND
            params.append(min_cost)
        
        if max_cost is not None:
            query += " AND cost <= %s"  # Добавлен пробел перед AND
            params.append(max_cost)
        
        query += " ORDER BY cost LIMIT 50"
        cursor.execute(query, params)
        
        return cursor.fetchall()
    
    finally:
        cursor.close()
        conn.close()

def create_container(container: ContainerCreate) -> dict:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("USE atk")
        
        cursor.execute("SELECT id FROM containers WHERE container_number = %s", (container.container_number,))
        
        if cursor.fetchone():
            raise ValueError("Контейнер с таким номером уже существует")
        
        query = "INSERT INTO containers (container_number, cost) VALUES (%s, %s)"
        cursor.execute(query, (container.container_number, container.cost))
        conn.commit()
        
        # Исправлено: выбираем всю запись, а не только ID
        cursor.execute("SELECT * FROM containers WHERE id = LAST_INSERT_ID()")
        
        return cursor.fetchone()
    
    except mysql.connector.Error as e:
        conn.rollback()
        raise e
    
    finally:
        cursor.close()
        conn.close()