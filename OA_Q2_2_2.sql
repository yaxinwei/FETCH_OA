-- 1. Join Transactions and Products on BARCODE.
-- 2. Filter for records where CATEGORY_2 is 'Dips & Salsa' and BRAND is not NULL.
-- 3. Calculate total quantity and total sales for each brand.
-- 4. Group the results by brand.
-- 5. Order by Total_quantity (and then Total_sales) in descending order.
-- 6. Return the top 10 brands.
SELECT TOP 10 P1.BRAND
	,SUM(FINAL_QUANTITY ) AS Total_quantity
	,SUM(FINAL_QUANTITY * FINAL_SALE) AS Total_sales
FROM Transactions AS T1
INNER JOIN Products AS P1 ON T1.BARCODE = P1.BARCODE
WHERE CATEGORY_2 = 'Dips & Salsa' AND BRAND IS NOT NULL
GROUP BY P1.BRAND
ORDER BY Total_quantity DESC,Total_sales DESC

