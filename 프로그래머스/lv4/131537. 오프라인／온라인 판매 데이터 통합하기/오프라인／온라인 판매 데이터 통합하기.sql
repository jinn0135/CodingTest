-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d'), PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE a
WHERE extract(year_month from SALES_DATE) = '202203'
UNION ALL
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d'), PRODUCT_ID, NULL USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE extract(year_month from SALES_DATE) = '202203'
ORDER BY 1,2,3