import mysql.connector

try:
    # Step 1: Connect to MySQL Server
    connection = mysql.connector.connect(
        host='localhost',
        user='patrick',  # Use your created MySQL user
        password='securepass123'  # Replace with your actual password
    )

    # Step 2: Check if connection was successful
    if connection.is_connected():
        cursor = connection.cursor()

        # Step 3: Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    # Step 4: Handle MySQL-specific errors
    print(f"Error connecting to MySQL: {err}")

finally:
    # Step 5: Clean up resources
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

