-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_INS a, ANIMAL_OUTS b
WHERE a.ANIMAL_ID = b.ANIMAL_ID
ORDER BY DATEDIFF(b.DATETIME,a.DATETIME) desc
LIMIT 2;