from build import AFF_NOTE

JS = r"""
(function(){
function $(s,c){return (c||document).querySelector(s)}
function f(x,d){return (+x).toLocaleString('ro-RO',{maximumFractionDigits:d||0})}
var c=$('#calc');if(c){
 function run(){var cap=+$('#cap').value||0,ef=(+$('#ef').value||85)/100;var tot=0,peak=0;
  c.querySelectorAll('tr[data-w]').forEach(function(r){var n=+$('.n',r).value||0,w=+$('.w',r).value||0,h=+$('.h',r).value||0;tot+=n*w*h;if(n>0)peak+=n*w*(+r.dataset.k||1)});
  var util=cap*ef;var zile=tot>0?util/tot:0;
  $('#rWh').textContent=f(tot)+' Wh/zi';$('#rUtil').textContent=f(util)+' Wh';$('#rZile').textContent=tot?(zile>=1?f(zile,1)+' zile':f(zile*24,1)+' ore'):'—';$('#rPeak').textContent=f(peak)+' W';
  $('#rHint').textContent=peak>0?'Alege o stație cu putere continuă de cel puțin '+f(Math.ceil(peak*1.25/100)*100)+' W (vârfurile de pornire ale frigiderului sau pompei pot fi de câteva ori mai mari).':'';}
 c.addEventListener('input',run);run();}
var b=$('#balc');if(b){function rb(){var w=+$('#bw').value||0,o=+$('#bo').value||0,a=(+$('#ba').value||0)/100,p=+$('#bp').value||0,k=+$('#bk').value||0;
 var prod=w/1000*o,auto=prod*a,econ=auto*p;$('#bProd').textContent=f(prod)+' kWh/an';$('#bEcon').textContent=f(econ)+' lei/an';$('#bLuna').textContent=f(econ/12)+' lei/lună';$('#bPay').textContent=econ>0?f(k/econ,1)+' ani':'—';}
 b.addEventListener('input',rb);b.addEventListener('change',rb);rb()}
})();
"""

ROWS = [('Frigider (medie pe zi)', 45, 24, 1, 3), ('Pompa centralei termice pe gaz', 90, 12, 1, 3), ('Router Wi-Fi', 12, 24, 1, 1),
        ('Laptop', 50, 4, 1, 1), ('Telefon (încărcare)', 15, 2, 2, 1), ('Bec LED', 9, 5, 3, 1), ('Televizor', 80, 3, 0, 1),
        ('CPAP / aparat medical', 40, 8, 0, 1)]
TROWS = ''.join('<tr data-w data-k="%d"><td>%s</td><td><input class="n" type="number" min="0" value="%d" style="width:50px"></td><td><input class="w" type="number" min="0" value="%d" style="width:62px"></td><td><input class="h" type="number" min="0" max="24" step="0.5" value="%s" style="width:54px"></td></tr>' % (k, n, q, w, h)
                for n, w, h, q, k in ROWS)

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Cât ține o stație portabilă? Calculator de autonomie</h2>
<div class="grid2"><div><label class="f" for="cap">Capacitatea stației (Wh)</label><input id="cap" type="number" min="0" step="50" value="1024"></div>
<div><label class="f" for="ef">Randament invertor (%)</label><input id="ef" type="number" min="50" max="100" value="85"></div></div>
<div class="tw"><table class="t"><tr><th>Aparat</th><th>Buc.</th><th>W</th><th>Ore/zi</th></tr>""" + TROWS + """</table></div>
<div class="res"><div class="big"><div class="kpi"><span>Consum zilnic</span><b id="rWh">–</b></div><div class="kpi"><span>Energie utilizabilă</span><b id="rUtil">–</b></div><div class="kpi main"><span>Autonomie estimată</span><b id="rZile">–</b></div><div class="kpi"><span>Putere simultană</span><b id="rPeak">–</b></div></div>
<p id="rHint" class="note" style="margin-top:10px"></p></div></form></div>"""

BALC = """<div class="tool" style="margin-top:24px"><form id="balc" onsubmit="return false"><h2>Cât economisești cu un kit fotovoltaic de balcon?</h2>
<div class="grid3"><div><label class="f" for="bw">Puterea panourilor (W)</label><input id="bw" type="number" min="0" step="10" value="800"></div>
<div><label class="f" for="bo">Orientare și montaj</label><select id="bo"><option value="1150">Sud, înclinat ~30° (~1.150 kWh/kW/an)</option><option value="850" selected>Sud, vertical pe balustradă (~850)</option><option value="750">Est sau vest, vertical (~750)</option><option value="550">Nord-est / umbră parțială (~550)</option></select></div>
<div><label class="f" for="ba">Cât din producție consumi pe loc (%)</label><input id="ba" type="number" min="0" max="100" value="70"></div>
<div><label class="f" for="bp">Prețul curentului (lei/kWh)</label><input id="bp" type="number" min="0" step="0.01" value="1.40"></div>
<div><label class="f" for="bk">Costul kitului (lei)</label><input id="bk" type="number" min="0" value="2300"></div></div>
<div class="res"><div class="big"><div class="kpi"><span>Producție estimată</span><b id="bProd">–</b></div><div class="kpi main"><span>Economie</span><b id="bEcon">–</b></div><div class="kpi"><span>Pe lună (medie)</span><b id="bLuna">–</b></div><div class="kpi"><span>Amortizare</span><b id="bPay">–</b></div></div>
<p class="note">Producțiile pe orientare sunt estimări orientative pentru România. Vara produce de câteva ori mai mult decât iarna. Energia neconsumată pe loc nu se plătește (kiturile de balcon nu sunt sisteme de prosumator).</p></div></form></div>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>Stație portabilă sau generator?</h2><p>O stație de alimentare portabilă este, de fapt, o baterie mare (de obicei LiFePO4) cu invertor și prize. Nu face zgomot, nu scoate gaze și poate sta în casă. În schimb, are energie limitată: o stație de 1.000 Wh ține un frigider și routerul aproximativ o zi, nu o săptămână. Pentru pene lungi, combin-o cu un panou solar pliabil.</p>
<div class="box"><b>Iarna: centrala pe gaz merge fără curent?</b> Nu. Pompa și electronica centralei au nevoie de curent. O stație portabilă de 500–1.000 Wh o poate ține pornită mai multe ore. <a href="/statie-portabila-centrala-termica.html">Cum o conectezi corect →</a></div></section>
""" + BALC + """
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/panouri-fotovoltaice-balcon-2026.html"><span class="tag">Lege</span><b>Panouri pe balcon: ce e legal în 2026</b><span>Ce spune ANRE, ce pregătește Senatul și cât costă un kit.</span></a>
<a class="c" href="/statie-portabila-centrala-termica.html"><span class="tag">Iarnă</span><b>Stație portabilă pentru centrala termică</b><span>Câte ore o ține și ce să nu faci.</span></a>
<a class="c" href="/cum-alegi-statie-portabila.html"><span class="tag">Cumpărare</span><b>Cum alegi o stație portabilă</b><span>Wh, W, LiFePO4, UPS și porturi.</span></a></div></section>"""

FAQ = [
    ('Cât ține o stație de 1.000 Wh?', 'Cu un randament de 85%, ai circa 850 Wh utilizabili. Un frigider (~1 kWh/zi), un router și încărcarea telefoanelor consumă în jur de 1,4 kWh pe zi, deci aproximativ 14–15 ore. Fără frigider, aceeași stație ține routerul, un laptop și câteva becuri mai multe zile.'),
    ('Pot pune panouri fotovoltaice pe balcon la bloc?', 'ANRE spune că sistemele plug-in de până la 800 W se pot monta, cu obligația de a anunța operatorul de distribuție și de a folosi un instalator atestat. Două proiecte de lege din Senat propun reguli simplificate pentru kiturile de balcon.'),
    ('Cât economisesc cu un kit de balcon?', 'Utilizatorii raportează economii de circa 60–100 de lei pe lună pe timp de vară, la un kit care costă 2.000–2.500 de lei. Economia reală depinde de orientare, umbră și cât consumi în timpul zilei.'),
]

ART_BALC = """<p>Kiturile fotovoltaice de balcon, cu unul sau două panouri și un microinvertor care se conectează la priză, au ajuns în magazinele din România. Sunt atractive pentru cei peste 6,5 milioane de români care stau la bloc, dar regulile sunt încă în schimbare.</p>
<h2>Ce spune ANRE acum</h2><ul><li>Sistemele plug-in de până la <strong>800 W</strong> pot fi montate, inclusiv la bloc.</li><li>Cine montează un astfel de sistem are obligația legală de a <strong>informa operatorul de distribuție</strong>.</li><li>Instalarea trebuie făcută de <strong>personal atestat</strong>. ANRE avertizează asupra ofertelor care promit montaj rapid „direct în priză”.</li><li>Dacă vrei să vinzi energia în rețea, devii prosumator și intri sub alte reguli, cu aviz tehnic de racordare.</li></ul>
<h2>Ce pregătește Senatul</h2><p>Două inițiative legislative propun un regim simplificat: maximum patru panouri și un invertor de 800 VA, fără injectarea surplusului în rețea, cu o simplă notificare la distribuitor, fără aviz tehnic și fără autorizație de construire. Un al doilea proiect introduce „prosumatorul de condominiu”, pentru panouri pe acoperișul blocului puse de asociația de proprietari.</p>
<h2>Cât costă și cât economisești</h2><p>Un mini-kit pentru balcon costă în jur de 2.000–2.500 de lei în magazinele de specialitate, iar cei care l-au montat estimează economii de 60–100 de lei pe lună în sezonul cald. Iarna producția scade mult.</p>
<div class="box info">Calculează producția și amortizarea pentru balconul tău cu <a href="/#balc">calculatorul kitului de balcon</a>.</div>
<h2>Siguranța pe primul loc</h2><ol><li>Prinde panourile solid; un panou căzut de la etaj e periculos.</li><li>Verifică cu un electrician starea circuitului din casă.</li><li>Folosește un microinvertor certificat, cu protecție anti-insularizare.</li><li>Verifică regulamentul asociației de proprietari privind fațada.</li></ol>""" + AFF_NOTE

ART_CT = """<p>La o pană de curent iarna, mulți descoperă că și centrala pe gaz se oprește: pompa de circulație, ventilatorul și placa electronică au nevoie de curent. O stație portabilă poate ține centrala pornită ore în șir.</p>
<h2>Cât consumă o centrală pe gaz</h2><p>O centrală murală de apartament consumă, în funcționare, de obicei între 60 și 150 W (verifică puterea electrică pe eticheta sau în cartea tehnică). Nu merge non-stop la putere maximă, așa că o medie de 80–100 W pe oră e o estimare rezonabilă.</p>
<h2>Câte ore o ține o stație</h2><div class="tw"><table class="t"><tr><th>Capacitate stație</th><th>Energie utilizabilă (~85%)</th><th>Centrală la ~90 W</th></tr>
<tr><td>500 Wh</td><td>~425 Wh</td><td>~4,5 ore</td></tr><tr><td>1.000 Wh</td><td>~850 Wh</td><td>~9 ore</td></tr><tr><td>2.000 Wh</td><td>~1.700 Wh</td><td>~19 ore</td></tr></table></div>
<h2>Cum o conectezi corect</h2><ul><li>Multe centrale sunt legate fix la o priză cu ștecher; în acest caz o muți direct în stație.</li><li>Dacă centrala e cablată fix, cheamă un electrician să monteze o priză dedicată sau un comutator.</li><li>Centralele moderne au nevoie de <strong>undă sinusoidală pură</strong>: toate stațiile de calitate o oferă, dar verifică fișa tehnică.</li><li>Unele centrale sunt sensibile la polaritate (fază/nul). Dacă afișează eroare la pornirea de pe stație, întoarce ștecherul.</li><li>Funcția <strong>UPS</strong> (comutare în sub 30 ms) ține centrala pornită fără întrerupere când pică rețeaua.</li></ul>
<div class="box">Nu folosi niciodată un generator pe benzină în interior sau în balconul închis: monoxidul de carbon este mortal.</div>""" + AFF_NOTE

ART_ALEG = """<p>Pe cutie apar multe cifre. Doar cinci contează cu adevărat.</p>
<h2>1. Capacitatea (Wh)</h2><p>Câtă energie stochează. Pentru urgențe în apartament: 1.000–2.000 Wh. Pentru camping: 300–700 Wh. Calculează exact ce îți trebuie cu <a href="/">calculatorul de autonomie</a>.</p>
<h2>2. Puterea continuă (W)</h2><p>Cât poate alimenta simultan. Un frigider are nevoie de 100–200 W în funcționare, dar la pornire cere de câteva ori mai mult. Un cuptor cu microunde sau un fierbător cer 1.000–2.000 W.</p>
<h2>3. Chimia bateriei</h2><p><strong>LiFePO4</strong> (litiu-fier-fosfat) rezistă de obicei la mii de cicluri și e mai sigură termic; este standardul în 2026. <strong>NMC</strong> e mai ușoară, dar are mai puține cicluri.</p>
<h2>4. Încărcarea</h2><ul><li>Viteza de încărcare de la priză (unele modele ajung la 80% în sub o oră).</li><li>Intrarea solară: tensiune și putere maximă acceptată de la panouri.</li><li>Încărcare din mașină (12 V).</li></ul>
<h2>5. UPS și porturi</h2><p>Funcția UPS ține aparatele pornite fără întrerupere la pană. Numără prizele de 230 V, porturile USB-C (cu putere de 60–100 W pentru laptop) și ieșirea de 12 V.</p>
<h2>Capcane</h2><ul><li>Capacitatea „echivalentă” în mAh nu spune nimic; caută Wh.</li><li>Unele stații ieftine au undă sinusoidală modificată: evită-le pentru centrale, pompe și aparate medicale.</li><li>Garanția: brandurile serioase oferă 3–5 ani.</li></ul>""" + AFF_NOTE

SITE = {
    'name': 'EnergieMobilă', 'domain': 'energiemobila.online',
    'c1': '#0b5c8a', 'c2': '#14a0b8', 'accent': '#ffb703',
    'mark': '<rect x="14" y="18" width="36" height="34" rx="7" fill="#fff"/><rect x="24" y="12" width="16" height="6" rx="2" fill="#fff"/><path d="M34 22l-8 14h7l-3 12 9-16h-7z" fill="#ffb703"/>',
    'tagline': 'Stații de alimentare portabile și panouri de balcon: calcule de autonomie, economie și ghiduri clare.',
    'badges': ['Calculator autonomie', 'Panouri de balcon 2026', 'Pene de curent iarna'],
    'nav': [('/', 'Autonomie'), ('/#balc', 'Panou balcon'), ('/panouri-fotovoltaice-balcon-2026.html', 'Ce e legal'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Calculator autonomie stație portabilă',
    'side_title': 'Cât ține stația ta?', 'side_text': 'Calculează autonomia pentru aparatele tale.',
    'about': '<p>EnergieMobilă este un site independent despre energie la purtător: stații de alimentare portabile, panouri solare pliabile și kituri fotovoltaice de balcon. Explicăm cifrele de pe cutie și legislația din România.</p><h2>Sursele noastre</h2><p>Comunicări ANRE, proiectele legislative publice, fișele tehnice ale producătorilor.</p><p>Unele linkuri către magazine pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'css': '.t input{padding:7px 5px;font-size:15px}.t td,.t th{padding:7px 5px}@media(max-width:480px){.tool{padding:16px 12px}}',
    'pages': [
        {'slug': 'index', 'title': 'Stație portabilă: calculator autonomie și panou de balcon', 'kind': 'tool', 'short': 'Calculator autonomie', 'appcat': 'UtilitiesApplication',
         'desc': 'Calculează câte ore ține o stație de alimentare portabilă (frigider, centrală, router) și cât economisești cu un kit fotovoltaic de balcon de 800 W.',
         'h1': 'Cât ține o stație portabilă? Calculator de autonomie', 'toolname': 'Calculator autonomie stație portabilă',
         'lead': 'Alege aparatele pe care vrei să le alimentezi la o pană de curent și afli de ce capacitate ai nevoie. Mai jos: economia unui kit solar de balcon.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'panouri-fotovoltaice-balcon-2026', 'title': 'Panouri fotovoltaice pe balcon în 2026: ce e legal', 'kind': 'article', 'short': 'Panouri de balcon: ce e legal',
         'desc': 'Ce spune ANRE despre kiturile solare plug-in de 800 W, ce prevăd proiectele din Senat, cât costă un kit și cât economisești la bloc.',
         'h1': 'Panouri fotovoltaice pe balcon: ce e legal în 2026', 'lead': 'Regulile ANRE, proiectele de lege, costurile și regulile de siguranță.', 'body': ART_BALC},
        {'slug': 'statie-portabila-centrala-termica', 'title': 'Stație portabilă pentru centrala termică: câte ore o ține', 'kind': 'article', 'short': 'Stație pentru centrala termică',
         'desc': 'Cât consumă o centrală pe gaz, câte ore o ține o stație portabilă de 500, 1.000 sau 2.000 Wh și cum o conectezi corect la o pană de curent.',
         'h1': 'Centrala pe gaz la pană de curent: o ții pornită cu o stație portabilă', 'lead': 'Consum, autonomie și conectare corectă, cu tabel pe capacități.', 'body': ART_CT},
        {'slug': 'cum-alegi-statie-portabila', 'title': 'Cum alegi o stație de alimentare portabilă (2026)', 'kind': 'article', 'short': 'Cum alegi o stație',
         'desc': 'Ghid de cumpărare: capacitate în Wh, putere continuă, LiFePO4 vs NMC, încărcare solară, UPS și capcanele de pe cutie.',
         'h1': 'Cum alegi o stație de alimentare portabilă', 'lead': 'Cele cinci cifre care contează și capcanele de evitat.', 'body': ART_ALEG},
    ]
}
