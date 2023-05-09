-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    if(SEX_UPON_INTAKE like '%Neutered%' OR SEX_UPON_INTAKE like '%Spayed%','O','X') 중성화
FROM ANIMAL_INS
ORDER BY 1