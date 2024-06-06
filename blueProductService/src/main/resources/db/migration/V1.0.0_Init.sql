create schema if not exists blue;

CREATE TABLE IF NOT EXISTS blue.product (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DOUBLE NOT NULL,
    imageUrl VARCHAR(255),
    type VARCHAR(255) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    size INT NOT NULL,
    quantity INT DEFAULT 0 NOT NULL,
    color VARCHAR(50) NOT NULL,
    material VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    rarity VARCHAR(50) NOT NULL,
    impression VARCHAR(50) NOT NULL,
    createdAt TIMESTAMP NOT NULL,
    lastUpdated TIMESTAMP NOT NULL
);
