-- 코드를 입력하세요
set @h:=-1;
SELECT @h:=@h+1 HOUR, 
    IFNULL((SELECT count(DATETIME) FROM ANIMAL_OUTS
           WHERE @h = hour(DATETIME)
           GROUP BY hour(DATETIME)),0) COUNT
FROM ANIMAL_OUTS
WHERE @h <23