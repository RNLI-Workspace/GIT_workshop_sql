-- Databricks notebook source
select * from  dev_bronze.ripcurrent.rnli_lifeguard_beaches

-- COMMAND ----------

SELECT BEACH_SLOPE, BEACH_TYPE
FROM dev_bronze.ripcurrent.rnli_lifeguard_beaches where BEACH_SHORE_NORMAL_WAVE <=200

-- COMMAND ----------

SELECT BEACH_SLOPE, BEACH_TYPE
FROM dev_bronze.ripcurrent.rnli_lifeguard_beaches where BEACH_SHORE_NORMAL_WAVE <=500