-- 코드를 입력하세요
SELECT a.PRODUCT_ID, a.PRODUCT_NAME, a.PRICE*SUM(b.AMOUNT) TOTAL_SALES
FROM FOOD_PRODUCT a JOIN FOOD_ORDER b ON a.PRODUCT_ID = b.PRODUCT_ID
WHERE DATE_FORMAT(b.PRODUCE_DATE,'%Y-%m')='2022-05'
GROUP BY b.PRODUCT_ID
ORDER BY 3 DESC, 1;
#SELECT * FROM FOOD_PRODUCT;