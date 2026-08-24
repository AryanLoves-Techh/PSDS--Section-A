import psycopg

conn = psycopg.connect(
    host="localhost",
    port=****,
    dbname="python_url_shortner",
    user="****",
    password="****"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS urls (
    url_id SERIAL PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(20) NOT NULL UNIQUE,
    user_id INT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS clicks (
    click_id SERIAL PRIMARY KEY,
    url_id INT NOT NULL,

    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    referrer TEXT,

    FOREIGN KEY (url_id)
        REFERENCES urls(url_id)
        ON DELETE CASCADE
);
""")

conn.commit()

print("Database tables created successfully!")

cursor.close()
conn.close()

