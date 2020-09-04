SELECT S.stdName, S.addr, C.clubName, C.roomNo
FROM stdtbl S
INNER JOIN stdclubtbl SC
ON S.stdName = SC.stdName
INNER JOIN clubtbl C
ON SC.clubName = C.clubName
ORDER BY S.stdName;