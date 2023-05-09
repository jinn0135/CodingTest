-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME #, a.SEX_UPON_INTAKE, b.SEX_UPON_OUTCOME
FROM ANIMAL_INS a, ANIMAL_OUTS b
WHERE a.ANIMAL_ID = b.ANIMAL_ID AND
      (a.SEX_UPON_INTAKE like 'Intact%' AND (b.SEX_UPON_OUTCOME like 'Spayed%' OR 
                                             b.SEX_UPON_OUTCOME like 'Neutered%'))
#    ((NOT a.SEX_UPON_INTAKE like 'Spayed%' OR NOT a.SEX_UPON_INTAKE like 'Neutered%') 
#     AND (b.SEX_UPON_OUTCOME like 'Spayed%' OR b.SEX_UPON_OUTCOME like 'Neutered%'))
ORDER BY 1