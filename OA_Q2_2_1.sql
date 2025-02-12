-- 1. Join Users and Transactions to get each user's transactions.
-- 2. Count transactions per user.
-- 3. Calculate the number of months each user has been active.
-- 4. Compute transactions per month (handle division by zero when months active is 0).
-- 5. Group by user and order by transactions per month in descending order.

SELECT 
    U1.ID,
    U1.CREATED_DATE,
    COUNT(T1.RECEIPT_ID) AS transaction_count,
    DATEDIFF(MONTH, U1.CREATED_DATE, GETDATE()) AS months_active,
    -- Calculate transactions per month (avoiding division by zero)
    CASE 
        WHEN DATEDIFF(MONTH, U1.CREATED_DATE, GETDATE()) = 0 THEN COUNT(T1.PURCHASE_DATE)
        ELSE ROUND(COUNT(T1.PURCHASE_DATE) *1.0 / DATEDIFF(MONTH, U1.CREATED_DATE, GETDATE()),2)
    END AS transactions_per_month
FROM 
    Users U1
INNER JOIN 
    Transactions T1
    ON U1.ID = T1.USER_ID
GROUP BY 
    U1.ID, U1.CREATED_DATE
ORDER BY 
    transactions_per_month DESC;
