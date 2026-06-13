-- Total Records
SELECT COUNT(*) FROM crop_prices;

-- Average Price by Crop
SELECT
    crop,
    ROUND(AVG(modal_price),2) AS avg_price
FROM crop_prices
GROUP BY crop
ORDER BY avg_price DESC;

-- Average Price by Market
SELECT
    market,
    ROUND(AVG(modal_price),2) AS avg_price
FROM crop_prices
GROUP BY market
ORDER BY avg_price DESC;

-- Highest Price Crop
SELECT
    crop,
    MAX(modal_price)
FROM crop_prices
GROUP BY crop;

-- Monthly Trend
SELECT
    DATE_TRUNC('month', date) AS month,
    AVG(modal_price)
FROM crop_prices
GROUP BY month
ORDER BY month;