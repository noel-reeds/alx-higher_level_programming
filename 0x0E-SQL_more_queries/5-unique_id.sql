-- creates a table and sets a constraint
-- sql syntax to set a UNIQUE key
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT '1' UNIQUE, name VARCHAR(256));
