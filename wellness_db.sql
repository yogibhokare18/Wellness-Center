-- ============================================
-- Wellness Center Database
-- ============================================

CREATE DATABASE IF NOT EXISTS wellness_db;

USE wellness_db;


-- ============================================
-- Registrations Table
-- ============================================

CREATE TABLE IF NOT EXISTS registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    phone VARCHAR(10) NOT NULL,

    gender VARCHAR(20) NOT NULL,

    dob DATE NOT NULL,

    address VARCHAR(255) NOT NULL,

    password VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ============================================
-- View All Registrations
-- ============================================

SELECT * FROM registrations;