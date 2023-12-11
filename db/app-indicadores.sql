-- Script SQL para crear tablas en MySQL

-- Crea la tabla de usuarios
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    telephone VARCHAR(120) UNIQUE NOT NULL,
    pwd VARCHAR(255) NOT NULL
);

-- Crea la tabla de retroalimentación
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    file VARCHAR(120) UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Crea la tabla de asignación
CREATE TABLE assignment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    task VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Crea la tabla de notificaciones
CREATE TABLE notification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)

);

-- Script SQL para crear la tabla ChartData en MySQL

CREATE TABLE chart_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    chart_type VARCHAR(50) NOT NULL,
    date DATETIME,
    data JSON NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL  
);

-- Crea la tabla de historial
CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chart_id INT NOT NULL,
    user_id INT NOT NULL,
    description VARCHAR(255) UNIQUE NOT NULL,
    date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (chart_id) REFERENCES chart_data(id)
);