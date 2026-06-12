-- Total Customers

SELECT COUNT(*) AS Total_Customers
FROM customer_churn;


-- Total Churn Customers

SELECT COUNT(*) AS Churn_Customers
FROM customer_churn
WHERE `Churn Label` = 'Yes';


-- Churn Rate

SELECT
    ROUND(
        (SUM(CASE WHEN `Churn Label`='Yes' THEN 1 ELSE 0 END)
        *100.0)/COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn;


-- Gender Wise Churn

SELECT
    Gender,
    `Churn Label`,
    COUNT(*) AS Total
FROM customer_churn
GROUP BY Gender, `Churn Label`;


-- Contract Wise Churn

SELECT
    Contract,
    `Churn Label`,
    COUNT(*) AS Total
FROM customer_churn
GROUP BY Contract, `Churn Label`;


-- Average Monthly Charges

SELECT
    `Churn Label`,
    ROUND(AVG(`Monthly Charges`),2)
    AS Avg_Monthly_Charges
FROM customer_churn
GROUP BY `Churn Label`;


-- Average Tenure

SELECT
    `Churn Label`,
    ROUND(AVG(`Tenure Months`),2)
    AS Avg_Tenure
FROM customer_churn
GROUP BY `Churn Label`;


-- Top Payment Methods Causing Churn

SELECT
    `Payment Method`,
    COUNT(*) AS Churn_Count
FROM customer_churn
WHERE `Churn Label`='Yes'
GROUP BY `Payment Method`
ORDER BY Churn_Count DESC;


-- Internet Service Analysis

SELECT
    `Internet Service`,
    `Churn Label`,
    COUNT(*) AS Total
FROM customer_churn
GROUP BY `Internet Service`,
         `Churn Label`;