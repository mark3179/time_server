CREATE DATABASE IF NOT EXISTS time_service
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE time_service;

CREATE TABLE IF NOT EXISTS qa (
  id CHAR(36) NOT NULL COMMENT 'UUID primary key',
  query VARCHAR(500) NOT NULL COMMENT 'question text',
  answer TEXT NOT NULL COMMENT 'answer text',
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'created time',
  PRIMARY KEY (id),
  UNIQUE KEY uk_qa_query (query)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;