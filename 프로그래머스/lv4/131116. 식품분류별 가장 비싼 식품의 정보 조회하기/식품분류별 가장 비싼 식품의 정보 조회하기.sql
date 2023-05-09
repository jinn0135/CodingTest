-- 코드를 입력하세요
SELECT CATEGORY, PRICE MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (SELECT CATEGORY, max(PRICE)
                            FROM FOOD_PRODUCT
                            WHERE CATEGORY IN ('과자','국','김치','식용유')
                            GROUP BY 1)
ORDER BY 2 DESC