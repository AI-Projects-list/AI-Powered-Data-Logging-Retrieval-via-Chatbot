CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    type TEXT,
    content TEXT,
    timestamp TIMESTAMP,
    metadata JSONB
);
