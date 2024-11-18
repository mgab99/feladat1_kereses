Először beolvasom az inputot.

Mivel az indexeket kell visszaadni, ezeket egy külön listába szervezem.
Ezután létrehozok egy 'solutions' változót, amiben azt tárolom, hogy
létezik-e jó megoldás.

Utána pedig bejárom n alkalommal az adathalmazt, s a beolvasott
cél, azaz target az, amit keresni fogok. Ha pontosan egyenlő,
akkor megvan a megoldás, és visszatérek, ha pedig nem, akkor 
folytatom vagy az inkrementálást, vagy pedig a csökkentést,
attól függően, hogy a jelenlegi értékünk nagyobb-e mint az elvárt,
avagy kisebb.

a ciklus végén pedig megvizsgálom, hogy a bejárás után van-e megoldás.
Ha nincs, akkor visszaadom a feladtban kért "IMPOSSIBLE" kiírást.