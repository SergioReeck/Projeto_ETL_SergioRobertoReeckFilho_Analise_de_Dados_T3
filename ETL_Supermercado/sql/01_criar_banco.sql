-- Active: 1790377505119@@127.0.0.1@5432@etl_vendas_supermercado
-- ============================================================
-- Criação do banco de dados do projeto ETL
-- ============================================================

CREATE DATABASE etl_vendas_supermercado;

-- ============================================================
-- Limpeza do schema public e criação do schema vendas
-- ============================================================

DROP SCHEMA IF EXISTS public CASCADE;
DROP SCHEMA IF EXISTS vendas CASCADE;

CREATE SCHEMA vendas;