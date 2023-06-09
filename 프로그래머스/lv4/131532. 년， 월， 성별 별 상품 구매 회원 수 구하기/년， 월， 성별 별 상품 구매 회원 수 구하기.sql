-- 코드를 입력하세요
SELECT year(b.SALES_DATE) YEAR, month(b.SALES_DATE) MONTH,
    a.GENDER GENDER, count(DISTINCT a.USER_ID) USERS
FROM USER_INFO a, ONLINE_SALE b
WHERE a.USER_ID = b.USER_ID  AND a.GENDER IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3;