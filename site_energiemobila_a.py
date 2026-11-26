# Artículos añadidos el 26 nov 2026 (build.py los carga si existe este archivo).
NOTE = ('<p class="note">Unele linkuri către magazine pot fi linkuri de afiliere. Prețurile sunt orientative, '
        'verificate la data actualizării; verifică prețul final în magazin.</p>')

PAGES = [
{
    'slug': 'pana-de-curent-iarna',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Pană de curent iarna: ce faci și ce stație îți trebuie',
    'kind': 'article',
    'short': 'Pană de curent iarna',
    'desc': 'Ce se oprește în casă la o pană de curent iarna, cât consumă centrala, frigiderul și routerul, ce capacitate de stație portabilă îți trebuie pentru 4, 12 sau 24 de ore.',
    'h1': 'Pană de curent iarna: ce faci și ce stație portabilă îți trebuie',
    'lead': 'Consumul real al aparatelor importante, trei scenarii calculate și greșelile periculoase de evitat.',
    'body': """<p>Iarna, o pană de curent nu înseamnă doar lumina stinsă. Centrala pe gaz se oprește și ea, pentru că pompa, ventilatorul și placa electronică au nevoie de curent. Frigiderul începe să se încălzească, routerul cade, iar telefoanele se descarcă exact când ai nevoie de ele. În 2025, românii au stat fără curent, în medie, aproape patru ore (indicele SAIDI, opriri planificate și accidentale, raportat de ANRE). Media ascunde însă diferențe mari: în zonele rurale și la capăt de rețea, o pană după o furtună de zăpadă poate dura o noapte întreagă.</p>
<p>Vestea bună: pentru aparatele care contează cu adevărat nu ai nevoie de un generator pe benzină. O stație de alimentare portabilă, adică o baterie mare cu prize de 230 V, ține centrala, frigiderul, routerul și câteva becuri ore în șir, în liniște și fără gaze de eșapament.</p>

<h2>Pasul 1: ce vrei să ții pornit</h2>
<p>Nu ai nevoie de toată casa. Fă lista scurtă a aparatelor esențiale și notează puterea lor (o găsești pe eticheta aparatului sau în manual). Valorile de mai jos sunt tipice pentru o locuință obișnuită:</p>
<div class="tw"><table class="t"><tr><th>Aparat</th><th>Putere tipică</th><th>Consum în 12 ore</th></tr>
<tr><td>Centrală murală pe gaz (pompă, ventilator, electronică)</td><td>60–150 W, în medie ~90 W</td><td>~1.100 Wh</td></tr>
<tr><td>Frigider combinat clasa A–C</td><td>pornește și se oprește singur</td><td>~400–600 Wh</td></tr>
<tr><td>Router Wi-Fi + ONT/modem</td><td>10–20 W</td><td>~180 Wh</td></tr>
<tr><td>3 becuri LED</td><td>3 × 8 W</td><td>~150 Wh (6 ore aprinse)</td></tr>
<tr><td>Încărcare 3 telefoane</td><td>~15 Wh fiecare</td><td>~45 Wh</td></tr>
<tr><td>Laptop</td><td>40–60 W</td><td>~200 Wh (4 ore)</td></tr>
<tr><td>Televizor LED 43"</td><td>60–90 W</td><td>~300 Wh (4 ore)</td></tr></table></div>
<p>Aparatele care încălzesc cu rezistență (aeroterma, fierbătorul, cuptorul cu microunde, plita electrică) consumă 1.000–2.500 W. O stație de 1 kWh le poate porni, dar le ține doar câteva zeci de minute. Pentru căldură, soluția corectă la o pană este să ții <strong>centrala pe gaz</strong> pornită, nu să încălzești cu curent din baterie.</p>

<h2>Pasul 2: cât timp trebuie să reziști</h2>
<p>Capacitatea stației se măsoară în wați-oră (Wh). În practică poți folosi cam 85% din ea, din cauza pierderilor din invertor. Iată trei scenarii realiste:</p>
<div class="tw"><table class="t"><tr><th>Scenariu</th><th>Ce ții pornit</th><th>Energie necesară</th><th>Stație potrivită</th></tr>
<tr><td>Pană scurtă, 3–4 ore</td><td>router, becuri, telefoane, laptop</td><td>~150–250 Wh</td><td>~300 Wh (clasa River 3 Plus)</td></tr>
<tr><td>O seară și o noapte, ~12 ore</td><td>centrală, frigider, router, becuri, telefoane</td><td>~1.700–2.000 Wh</td><td>2 kWh sau 1 kWh fără frigider</td></tr>
<tr><td>O zi întreagă, 24 de ore</td><td>centrală, frigider, router, becuri</td><td>~3.300–3.800 Wh</td><td>3 kWh sau 2 kWh + reîncărcare</td></tr></table></div>
<p>Dacă vrei să calculezi exact pentru aparatele tale, folosește <a href="/calculator-autonomie.html">calculatorul de autonomie</a>: alegi aparatele și vezi câte ore ține fiecare capacitate.</p>

<h2>Ce stație alegi, pe scurt</h2>
<ul><li><strong>Sub 300 Wh</strong>: pentru internet, lumină și telefoane la o pană scurtă. Ușoară, ieftină, bună și pentru mașină sau camping. Nu ține centrala o noapte.</li>
<li><strong>Clasa 1 kWh</strong> (1.000–1.100 Wh): punctul ideal pentru un apartament. Ține centrala aproximativ 9 ore singură sau centrala plus routerul și becurile o seară întreagă. Pentru frigider pe toată noaptea devine la limită.</li>
<li><strong>Clasa 2 kWh</strong>: centrala, frigiderul și routerul toată noaptea, cu rezervă. Alegerea bună pentru o casă cu pene dese.</li>
<li><strong>3 kWh sau mai mult</strong>: rezervă serioasă pentru o zi întreagă sau pentru o casă de vacanță; de obicei se pot extinde cu baterii suplimentare.</li></ul>
{{CARDS:ecoflow-river-3-plus,anker-solix-c1000x,ecoflow-delta-3-max}}

<h2>Cum conectezi centrala corect</h2>
<p>Dacă centrala are ștecher, o muți direct din priza de perete în stație. Dacă e legată fix în instalație, cere unui electrician autorizat să monteze o priză dedicată sau un comutator; nu improviza. Centralele moderne au nevoie de <strong>undă sinusoidală pură</strong>, pe care o oferă toate stațiile de calitate. Unele sunt sensibile la polaritate: dacă afișează o eroare când le pornești de pe stație, întoarce ștecherul în priză. Detaliile, cu un tabel pe capacități, sunt în ghidul <a href="/statie-portabila-centrala-termica.html">stație portabilă pentru centrala termică</a>.</p>
<p>Un lucru util: multe stații au funcție <strong>UPS</strong>. Le ții permanent în priză, cu centrala sau routerul legate la ele, iar când pică rețeaua comută singure pe baterie în câteva milisecunde. Nu mai trebuie să cobori în beci cu lanterna ca să muți ștechere.</p>

<h2>Greșeli periculoase de evitat</h2>
<div class="box">Nu porni niciodată un generator pe benzină în casă, în garaj, pe balconul închis sau lângă o fereastră deschisă. Monoxidul de carbon nu are miros și poate ucide în câteva minute. Nu încălzi locuința cu aragazul sau cuptorul pe gaz.</div>
<ul><li><strong>Nu băga stația sau generatorul în priza casei</strong> ca să „alimentezi toată instalația”. Fără un comutator de transfer montat de electrician, curentul poate ajunge înapoi în rețea și pune în pericol echipele care lucrează la avarie.</li>
<li><strong>Nu acoperi stația</strong> și nu o ține lângă calorifer sau sobă; are nevoie de ventilație.</li>
<li><strong>Nu lăsa frigiderul deschis</strong> „să vezi dacă mai e rece”. Fiecare deschidere scurtează timpul cât alimentele rămân în siguranță.</li></ul>

<h2>Lista de pregătire pentru iarnă</h2>
<ol><li>Încarcă stația la 100% la începutul iernii și verifică-o o dată pe lună. Bateriile LiFePO4 pierd foarte puțin în depozitare.</li>
<li>Pune lângă ea un prelungitor scurt și de calitate și notează pe o hârtie ce aparat merge în ce priză.</li>
<li>Ține o lanternă frontală și un power bank încărcat pentru drumul până la stație.</li>
<li>Dacă ai un kit solar sau un panou pliabil, verifică-l: chiar și iarna, în zilele însorite, reîncarcă o parte din baterie.</li>
<li>Notează numărul de avarii al distribuitorului tău (este trecut pe factură).</li></ol>

<h2>Ai dreptul la compensații</h2>
<p>Conform standardului de performanță ANRE pentru distribuția energiei electrice, operatorii de distribuție trebuie să acorde compensații între 5 și 300 de lei clienților afectați de întreruperi neplanificate, atunci când acestea depășesc durata sau numărul stabilit de standard. Compensațiile pentru întreruperi se acordă pe factură, iar pentru aparatele defectate de variațiile de tensiune trebuie să depui o cerere la distribuitor în termenul prevăzut (de regulă câteva zile de la incident). Păstrează dovezi: ora întreruperii, fotografii, bonuri de reparație.</p>
<p class="note">Surse: ANRE (indicele SAIDI 2025 și standardul de performanță pentru serviciul de distribuție), fișele tehnice ale producătorilor de stații. Consumurile sunt orientative; verifică eticheta aparatelor tale.</p>""" + NOTE,
    'faq': [
        ('Ce stație portabilă îmi trebuie ca să țin centrala pe gaz o noapte?',
         'O centrală murală consumă în medie 80–100 W. Pentru 10–12 ore ai nevoie de aproximativ 1.100 Wh utilizabili, deci de o stație de 1.000–1.300 Wh. Dacă vrei și frigiderul, alege clasa de 2 kWh.'),
        ('Pot încălzi casa cu o stație portabilă?',
         'Practic nu. O aerotermă de 2.000 W golește o stație de 1 kWh în aproximativ 25 de minute. Folosește stația ca să ții pornită centrala pe gaz, care produce căldura din gaz și are nevoie doar de puțin curent.'),
        ('Pot lăsa stația conectată permanent la centrală?',
         'Da, dacă stația are funcție UPS sau pass-through. O ții în priză, centrala e legată la stație, iar la pană comută automat pe baterie. Verifică în manual timpul de comutare și dacă producătorul recomandă folosirea permanentă ca UPS.'),
    ],
},
{
    'slug': 'cat-tine-frigiderul-pe-statie',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Cât ține un frigider pe o stație portabilă? Calcul simplu',
    'kind': 'article',
    'short': 'Frigiderul pe stație',
    'desc': 'Cât consumă un frigider pe zi, ce înseamnă vârful de pornire al compresorului și câte ore ține pe o stație de 300 Wh, 1 kWh, 2 kWh sau 3 kWh. Cu tabel și sfaturi.',
    'h1': 'Cât ține un frigider pe o stație portabilă',
    'lead': 'Consumul real pe zi, vârful de pornire și un tabel pe capacități, plus cum câștigi ore în plus.',
    'body': """<p>Frigiderul este, după centrală, aparatul pe care oamenii vor cel mai des să-l țină pornit la o pană de curent. Vestea bună este că un frigider modern consumă mult mai puțin decât crezi: nu merge non-stop, ci pornește compresorul câteva minute, apoi se oprește. Vestea mai puțin bună este că, la fiecare pornire, cere pentru o clipă de câteva ori mai mult decât puterea lui normală. Ambele contează când alegi stația.</p>

<h2>Cât consumă un frigider pe zi</h2>
<p>Cea mai bună sursă este eticheta energetică: pe ea scrie consumul anual în kWh. Împarte la 365 și ai consumul pe zi.</p>
<div class="tw"><table class="t"><tr><th>Tip de frigider</th><th>Consum anual tipic (etichetă)</th><th>Consum pe zi</th></tr>
<tr><td>Frigider mic sub blat</td><td>~100–150 kWh</td><td>~0,3–0,4 kWh</td></tr>
<tr><td>Combină frigorifică modernă, clasa A–C</td><td>~150–250 kWh</td><td>~0,4–0,7 kWh</td></tr>
<tr><td>Combină mai veche sau clasa E–F</td><td>~250–350 kWh</td><td>~0,7–1 kWh</td></tr>
<tr><td>Side-by-side mare</td><td>~350–450 kWh</td><td>~1–1,2 kWh</td></tr></table></div>
<p>Atenție: consumul de pe etichetă este măsurat în laborator, la o temperatură a camerei constantă. Iarna, într-o bucătărie mai rece, frigiderul consumă de obicei <em>mai puțin</em>; vara, mai mult. Dacă ai o priză inteligentă sau un wattmetru, măsoară consumul real o zi întreagă: este cel mai exact.</p>

<h2>Vârful de pornire: de ce contează puterea stației</h2>
<p>Motorul compresorului are nevoie la pornire de un curent mare pentru o fracțiune de secundă. Un frigider care consumă 100–150 W în funcționare poate cere de 3–5 ori mai mult la pornire. Frigiderele cu compresor <strong>inverter</strong> pornesc mult mai lin. Orice stație serioasă de peste 500 W putere continuă face față fără probleme; stațiile foarte mici (300 W) pot opri ieșirea la fiecare pornire. Dacă ai o stație mică, verifică în fișa tehnică puterea de vârf (surge) și încearcă frigiderul înainte de iarnă, nu în timpul penei.</p>

<h2>Câte ore ține, pe capacități</h2>
<p>Calculul: capacitatea stației × 0,85 (energia utilizabilă după pierderile invertorului) împărțit la consumul frigiderului pe oră.</p>
<div class="tw"><table class="t"><tr><th>Stație</th><th>Energie utilizabilă</th><th>Frigider 0,5 kWh/zi</th><th>Frigider 0,8 kWh/zi</th><th>Frigider 1,2 kWh/zi</th></tr>
<tr><td>~300 Wh</td><td>~250 Wh</td><td>~12 ore</td><td>~7,5 ore</td><td>~5 ore</td></tr>
<tr><td>~1.000 Wh</td><td>~870 Wh</td><td>~1,7 zile</td><td>~26 de ore</td><td>~17 ore</td></tr>
<tr><td>~2.000 Wh</td><td>~1.740 Wh</td><td>~3,5 zile</td><td>~2,2 zile</td><td>~1,4 zile</td></tr>
<tr><td>~3.000 Wh</td><td>~2.610 Wh</td><td>~5 zile</td><td>~3,3 zile</td><td>~2,2 zile</td></tr></table></div>
<p>Valorile sunt pentru frigider singur. Dacă pe aceeași stație ai și centrala (~90 W), routerul și becurile, împarte timpul cam la jumătate sau mai mult. Combinațiile exacte le faci în <a href="/calculator-autonomie.html">calculatorul de autonomie</a>.</p>
{{CARDS:anker-solix-c1000x,ecoflow-delta-3-plus,bluetti-premium-100-v2}}

<h2>Cum câștigi ore în plus</h2>
<ul><li><strong>Nu deschide ușa.</strong> Un frigider închis păstrează alimentele în siguranță în jur de 4 ore fără curent, iar un congelator plin în jur de 48 de ore (24 de ore dacă e pe jumătate gol). Asta înseamnă că nu trebuie să-l ții alimentat continuu.</li>
<li><strong>Alimentează-l pe tranșe.</strong> La o pană lungă, poți porni frigiderul de pe stație câte o oră la 3–4 ore. Consumi mai puțin, iar temperatura din interior rămâne sigură. Verifică cu un termometru: sub 4 °C în frigider, sub −18 °C în congelator.</li>
<li><strong>Umple spațiile goale</strong> cu sticle de apă: masa rece ține temperatura mai bine decât aerul.</li>
<li><strong>Folosește frigul de afară.</strong> Iarna, balconul sau o cutie izotermă cu acumulatori de frig pot prelua o parte din alimente, cu grijă să nu înghețe ce nu trebuie.</li>
<li><strong>Setează termostatul cu un grad mai sus</strong> la începutul penei; reduce numărul de porniri ale compresorului.</li></ul>

<h2>Ce să nu faci</h2>
<ul><li>Nu lega frigiderul la stație printr-un prelungitor subțire, cu multe aparate pe el.</li>
<li>Nu folosi modul „eco” al stației dacă oprește automat ieșirea AC la consum mic: între cicluri, frigiderul consumă aproape nimic, iar stația îl poate opri.</li>
<li>Nu așeza stația lângă grila fierbinte din spatele frigiderului.</li></ul>
<p class="note">Surse: etichetele energetice UE pentru aparate frigorifice, recomandările de siguranță alimentară pentru pene de curent (USDA / FoodSafety.gov), fișele tehnice ale stațiilor. Consumurile sunt orientative.</p>""" + NOTE,
    'faq': [
        ('Merge un frigider pe o stație de 300 W?',
         'Uneori, dar e la limită: la pornire, compresorul cere pentru o clipă de câteva ori puterea normală, iar stația poate opri ieșirea. Pentru frigider, alege o stație cu cel puțin 600–1.000 W putere continuă.'),
        ('Câte ore ține o stație de 1 kWh un frigider?',
         'Pentru o combină modernă care consumă ~0,6–0,8 kWh pe zi, aproximativ 26–35 de ore, dacă stația alimentează doar frigiderul. Cu centrala și routerul pe aceeași stație, timpul scade la o noapte.'),
        ('Trebuie să țin frigiderul pornit toată pana?',
         'Nu neapărat. Închis, un frigider păstrează alimentele în siguranță în jur de 4 ore. La pene lungi, îl poți alimenta câte o oră la câteva ore, verificând temperatura cu un termometru.'),
    ],
},
{
    'slug': 'generator-sau-statie-portabila',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Generator sau stație portabilă? Comparație completă',
    'kind': 'article',
    'short': 'Generator sau stație?',
    'desc': 'Generator pe benzină sau stație de alimentare portabilă pentru pene de curent: preț, autonomie, zgomot, siguranță, întreținere și când merită fiecare. Comparație cu cifre.',
    'h1': 'Generator pe benzină sau stație portabilă: ce alegi pentru pene de curent',
    'lead': 'Cât costă, cât țin, cât de zgomotoase sunt și unde are fiecare avantaj real.',
    'body': """<p>Ani la rând, singura soluție pentru pene de curent a fost generatorul pe benzină. Astăzi, stațiile de alimentare portabile cu baterie LiFePO4 fac aceeași treabă pentru majoritatea apartamentelor și caselor, fără zgomot și fără gaze de eșapament. Totuși, generatorul nu a devenit inutil: la pene de mai multe zile sau la consumatori mari, încă are avantaje. Iată o comparație cinstită.</p>

<h2>Comparația pe scurt</h2>
<div class="tw"><table class="t"><tr><th></th><th>Generator pe benzină (~2 kW)</th><th>Stație portabilă (~1–2 kWh)</th></tr>
<tr><td>Preț de pornire</td><td>~1.100 lei (clasic), ~1.800 lei (cu invertor)</td><td>~3.000–4.000 lei (1 kWh), ~6.000 lei (2 kWh)</td></tr>
<tr><td>Autonomie</td><td>câteva ore pe rezervor, dar o realimentezi oricând</td><td>limitată de capacitate; se reîncarcă din priză, solar sau mașină</td></tr>
<tr><td>Folosire în interior</td><td><strong>Interzisă</strong> (monoxid de carbon)</td><td>Da, oriunde în casă</td></tr>
<tr><td>Zgomot</td><td>de la ~70 dB(A) la invertoarele silențioase până la peste 90 dB(A) la cele clasice</td><td>practic silențioasă; ventilator doar la consum mare</td></tr>
<tr><td>Pornire</td><td>manuală, afară, pe frig</td><td>instantanee; multe au UPS automat</td></tr>
<tr><td>Întreținere</td><td>ulei, bujie, combustibil proaspăt, pornire lunară</td><td>practic zero; o încărcare la câteva luni</td></tr>
<tr><td>Consumatori mari (pompă, sudură, unelte)</td><td>Da, cu limita puterii</td><td>Da, dar golesc bateria repede</td></tr>
<tr><td>Calitatea curentului</td><td>bună doar la modelele cu invertor</td><td>undă sinusoidală pură, sigură pentru electronice și centrală</td></tr></table></div>

<h2>Cât costă cu adevărat</h2>
<p>Un generator clasic de 2 kW pornește de la aproximativ 1.100 de lei, iar unul cu invertor, mai silențios și cu curent „curat” pentru centrală și electronice, de la aproximativ 1.800 de lei (de exemplu Hyundai HY2000Si D la Hornbach). Modelele de referință, ca Honda EU22i, costă de câteva ori mai mult. Pe hârtie, generatorul este mult mai ieftin.</p>
<p>Diferența se micșorează când pui la socoteală tot: canistra și benzina proaspătă (benzina veche de câteva luni strică carburatorul), uleiul, faptul că trebuie pornit lunar ca să nu se înțepenească și, mai ales, că îl folosești doar afară. O stație de 1 kWh costă mai mult la cumpărare, dar nu are costuri de funcționare și o poți folosi și în rest: camping, rulotă, unelte în grădină, sau ca UPS permanent pentru router și centrală.</p>

<h2>Autonomie: unde câștigă generatorul</h2>
<p>Un generator cu invertor de 2 kW, ca Honda EU22i (1,8 kW putere continuă, rezervor de 3,6 litri), merge în jur de 3,5 ore la două treimi din putere și mult mai mult la sarcină mică. Când se termină benzina, torni alta și merge mai departe. La o pană de trei zile într-o zonă izolată, asta e greu de egalat cu o baterie.</p>
<p>O stație de 1 kWh ține centrala aproximativ 9 ore, iar una de 2 kWh centrala, frigiderul și routerul toată noaptea. După aceea trebuie reîncărcată. Iarna, un panou solar pliabil de 200 W aduce doar câteva sute de Wh pe zi, în zilele senine. Pentru majoritatea penelor din orașe (câteva ore), capacitatea unei stații este suficientă; pentru pene de mai multe zile, nu.</p>

<h2>Siguranța: unde câștigă clar stația</h2>
<div class="box">Generatorul pe benzină se folosește doar afară, departe de uși, ferestre și guri de aerisire. Monoxidul de carbon nu are miros și se acumulează rapid în garaje, beciuri și balcoane închise. Nu conecta niciodată un generator la priza casei fără un comutator de transfer montat de un electrician autorizat.</div>
<p>Iarna, tentația de a ține generatorul „doar puțin” în garaj sau pe balcon este mare, pentru că afară e frig, plouă sau ninge. Exact atunci se întâmplă accidentele. O stație portabilă stă lângă centrală, în bucătărie sau în dormitor, fără niciun risc de acest tip.</p>

<h2>Când alegi generatorul</h2>
<ul><li>Locuiești într-o zonă unde penele durează des o zi sau mai mult.</li>
<li>Ai consumatori mari care trebuie să meargă ore în șir: pompă de puț, hidrofor, unelte pe șantier.</li>
<li>Ai unde să-l folosești în siguranță, afară, sub un acoperiș deschis, și ești dispus să-l întreții.</li></ul>

<h2>Când alegi stația portabilă</h2>
<ul><li>Locuiești la bloc sau într-o casă fără loc sigur pentru generator.</li>
<li>Penele tale durează de obicei câteva ore și vrei să ții centrala, frigiderul și internetul.</li>
<li>Vrei să funcționeze automat (UPS), fără să cobori noaptea să pornești ceva.</li>
<li>O vei folosi și în afara penelor: camping, mașină, grădină, panou solar de balcon.</li></ul>

<h2>Varianta hibridă</h2>
<p>Mulți aleg ambele: stația ține casa automat și în liniște la penele obișnuite, iar un generator mic cu invertor reîncarcă stația câteva ore pe zi la penele foarte lungi. Multe stații acceptă încărcare direct de la generator. Așa generatorul merge puțin, afară, iar în casă ai curent tot timpul.</p>
{{CARDS:anker-solix-c1000x,ecoflow-delta-3-max,anker-solix-f3000}}
<p>Ca să vezi ce capacitate îți trebuie pentru aparatele tale, folosește <a href="/calculator-autonomie.html">calculatorul de autonomie</a>; pentru scenariile de iarnă, citește și <a href="/pana-de-curent-iarna.html">ghidul pentru pană de curent iarna</a>.</p>
<p class="note">Surse: fișele tehnice Honda EU22i, oferta Hornbach România pentru Hyundai HY2000Si D, fișele tehnice ale stațiilor. Prețurile sunt orientative, din noiembrie 2026.</p>""" + NOTE,
    'faq': [
        ('Pot ține generatorul pe balcon?',
         'Nu, dacă balconul este închis sau aproape de ferestre și uși. Gazele de eșapament conțin monoxid de carbon, care poate intra în locuință. Generatorul se folosește doar afară, în spațiu deschis, departe de deschideri.'),
        ('Merge centrala pe gaz pe generator?',
         'Da, dar alege un generator cu invertor. Generatoarele clasice pot avea tensiune și frecvență instabile, iar plăcile electronice ale centralelor sunt sensibile. Stațiile portabile oferă undă sinusoidală pură.'),
        ('Ce e mai ieftin pe termen lung?',
         'Generatorul e mai ieftin la cumpărare, dar are costuri de benzină și întreținere și se folosește doar afară. Stația costă mai mult la început, dar nu are costuri de funcționare și o poți folosi și în rest: camping, unelte, UPS.'),
    ],
},
]
