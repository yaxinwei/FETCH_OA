-- 1. Join Transactions and Products, selecting only records with a non-null BRAND.
-- 2. Filter transactions for users whose account was created at least 6 months ago.
-- 3. Group by BRAND and calculate total sales using (FINAL_QUANTITY * FINAL_SALE).
-- 4. Order the brands by total sales in descending order.
-- 5. Return the top 5 brands.
SELECT TOP 5 P1.BRAND
	  --,SUM(FINAL_QUANTITY * FINAL_SALE) AS Total_sales
FROM Transactions AS T1
     INNER JOIN Products AS P1 ON T1.BARCODE = P1.BARCODE
WHERE P1.BRAND IS NOT NULL AND 
	T1.USER_ID IN (
	SELECT ID
	FROM Users
	WHERE CREATED_DATE <= DATEADD(MONTH, -6, GETDATE())

)
GROUP BY P1.BRAND
ORDER BY SUM(FINAL_QUANTITY * FINAL_SALE) DESC







