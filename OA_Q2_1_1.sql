-- 1. Join Transactions and Products where BRAND is not NULL.
-- 2. Filter for transactions from users aged 21 or older (using their BIRTH_DATE).
-- 3. Count the distinct receipts for each brand.
-- 4. Rank the brands in descending order based on transaction count.
-- 5. Select the top 5 brands.
WITH Ranked AS (
SELECT P1.BRAND,
      DENSE_RANK() OVER (ORDER BY COUNT(DISTINCT T1.RECEIPT_ID) DESC) AS ranking
FROM Transactions AS T1
INNER JOIN Products AS P1 ON T1.BARCODE = P1.BARCODE 
WHERE P1.BRAND IS NOT NULL AND T1.USER_ID IN (
      SELECT ID
      FROM UserS
      WHERE
      DATEDIFF(YEAR, BIRTH_DATE, GETUTCDATE()) - 
			CASE WHEN MONTH(BIRTH_DATE) > MONTH(GETUTCDATE()) OR 
                  (MONTH(BIRTH_DATE) = MONTH(GETUTCDATE()) AND DAY(BIRTH_DATE) > DAY(GETUTCDATE())) 
           THEN 1 ELSE 0 END >= 21
)
GROUP BY P1.BRAND
)
SELECT * FROM Ranked
WHERE ranking <= 5


