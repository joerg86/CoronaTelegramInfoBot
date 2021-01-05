bl = {'Bayern': 9, 'Nordrhein-Westfalen': 5, 'Sachsen': 14, 'Brandenburg': 12, 'Saarland': 10, 'Baden-Württemberg': 8, 'Hessen': 6, 'Niedersachsen': 3, 'Hamburg': 2, 'Rheinland-Pfalz': 7, 'Schleswig-Holstein': 1, 'Bremen': 4, 'Berlin': 11, 'Mecklenburg-Vorpommern': 13, 'Thüringen': 16, 'Sachsen-Anhalt': 15}

lk = ['Ahrweiler', 'Aichach-Friedberg', 'Alb-Donau-Kreis', 'Altenburger Land', 'Altenkirchen (Westerwald)', 'Altmarkkreis Salzwedel', 'Altötting', 'Alzey-Worms', 'Amberg', 'Amberg-Sulzbach', 'Ammerland', 'Anhalt-Bitterfeld', 'Ansbach', 'Aschaffenburg', 'Augsburg', 'Aurich', 'Bad Dürkheim', 'Bad Kissingen', 'Bad Kreuznach', 'Bad Tölz-Wolfratshausen', 'Baden-Baden', 'Bamberg', 'Barnim', 'Bautzen', 'Bayreuth', 'Berchtesgadener Land', 'Bergstraße', 'Berlin Charlottenburg-Wilmersdorf', 'Berlin Friedrichshain-Kreuzberg', 'Berlin Lichtenberg', 'Berlin Marzahn-Hellersdorf', 'Berlin Mitte', 'Berlin Neukölln', 'Berlin Pankow', 'Berlin Reinickendorf', 'Berlin Spandau', 'Berlin Steglitz-Zehlendorf', 'Berlin Tempelhof-Schöneberg', 'Berlin Treptow-Köpenick', 'Bernkastel-Wittlich', 'Biberach', 'Bielefeld', 'Birkenfeld', 'Böblingen', 'Bochum', 'Bodenseekreis', 'Bonn', 'Börde', 'Borken', 'Bottrop', 'Brandenburg an der Havel', 'Braunschweig', 'Breisgau-Hochschwarzwald', 'Bremen', 'Bremerhaven', 'Burgenlandkreis', 'Calw', 'Celle', 'Cham', 'Chemnitz', 'Cloppenburg', 'Coburg', 'Cochem-Zell', 'Coesfeld', 'Cottbus', 'Cuxhaven', 'Dachau', 'Dahme-Spreewald', 'Darmstadt', 'Darmstadt-Dieburg', 'Deggendorf', 'Delmenhorst', 'Dessau-Roßlau', 'Diepholz', 'Dillingen a.d. Donau', 'Dingolfing-Landau', 'Dithmarschen', 'Donau-Ries', 'Donnersbergkreis', 'Dortmund', 'Dresden', 'Duisburg', 'Düren', 'Düsseldorf', 'Ebersberg', 'Eichsfeld', 'Eichstätt', 'Eifelkreis Bitburg-Prüm', 'Eisenach', 'Elbe-Elster', 'Emden', 'Emmendingen', 'Emsland', 'Ennepe-Ruhr-Kreis', 'Enzkreis', 'Erding', 'Erfurt', 'Erlangen', 'Erlangen-Höchstadt', 'Erzgebirgskreis', 'Essen', 'Esslingen', 'Euskirchen', 'Flensburg', 'Forchheim', 'Frankenthal (Pfalz)', 'Frankfurt (Oder)', 'Frankfurt am Main', 'Freiburg im Breisgau', 'Freising', 'Freudenstadt', 'Freyung-Grafenau', 'Friesland', 'Fulda', 'Fürstenfeldbruck', 'Fürth', 'Garmisch-Partenkirchen', 'Gelsenkirchen', 'Gera', 'Germersheim', 'Gießen', 'Gifhorn', 'Göppingen', 'Görlitz', 'Goslar', 'Gotha', 'Göttingen', 'Grafschaft Bentheim', 'Greiz', 'Groß-Gerau', 'Günzburg', 'Gütersloh', 'Hagen', 'Halle (Saale)', 'Hamburg', 'Hameln-Pyrmont', 'Hamm', 'Harburg', 'Harz', 'Haßberge', 'Havelland', 'Heidekreis', 'Heidelberg', 'Heidenheim', 'Heilbronn', 'Heinsberg', 'Helmstedt', 'Herford', 'Herne', 'Hersfeld-Rotenburg', 'Herzogtum Lauenburg', 'Hildburghausen', 'Hildesheim', 'Hochsauerlandkreis', 'Hochtaunuskreis', 'Hof', 'Hohenlohekreis', 'Holzminden', 'Höxter', 'Ilm-Kreis', 'Ingolstadt', 'Jena', 'Jerichower Land', 'Kaiserslautern', 'Karlsruhe', 'Kassel', 'Kaufbeuren', 'Kelheim', 'Kempten (Allgäu)', 'Kiel', 'Kitzingen', 'Kleve', 'Koblenz', 'Köln', 'Konstanz', 'Krefeld', 'Kronach', 'Kulmbach', 'Kusel', 'Kyffhäuserkreis', 'Lahn-Dill-Kreis', 'Landau in der Pfalz', 'Landsberg am Lech', 'Landshut', 'Leer', 'Leipzig', 'Leverkusen', 'Lichtenfels', 'Limburg-Weilburg', 'Lindau (Bodensee)', 'Lippe', 'Lörrach', 'Lübeck', 'Lüchow-Dannenberg', 'Ludwigsburg', 'Ludwigshafen am Rhein', 'Ludwigslust-Parchim', 'Lüneburg', 'Magdeburg', 'Main-Kinzig-Kreis', 'Main-Spessart', 'Main-Tauber-Kreis', 'Main-Taunus-Kreis', 'Mainz', 'Mainz-Bingen', 'Mannheim', 'Mansfeld-Südharz', 'Marburg-Biedenkopf', 'Märkischer Kreis', 'Märkisch-Oderland', 'Mayen-Koblenz', 'Mecklenburgische Seenplatte', 'Meißen', 'Memmingen', 'Merzig-Wadern', 'Mettmann', 'Miesbach', 'Miltenberg', 'Minden-Lübbecke', 'Mittelsachsen', 'Mönchengladbach', 'Mühldorf a. Inn', 'Mülheim an der Ruhr', 'München', 'Münster', 'Neckar-Odenwald-Kreis', 'Neuburg-Schrobenhausen', 'Neumarkt i.d. OPf.', 'Neumünster', 'Neunkirchen', 'Neustadt a.d. Aisch-Bad Windsheim', 'Neustadt a.d. Waldnaab', 'Neustadt an der Weinstraße', 'Neu-Ulm', 'Neuwied', 'Nienburg (Weser)', 'Nordfriesland', 'Nordhausen', 'Nordsachsen', 'Nordwestmecklenburg', 'Northeim', 'Nürnberg', 'Nürnberger Land', 'Oberallgäu', 'Oberbergischer Kreis', 'Oberhausen', 'Oberhavel', 'Oberspreewald-Lausitz', 'Odenwaldkreis', 'Oder-Spree', 'Offenbach', 'Offenbach am Main', 'Oldenburg', 'Oldenburg (Oldb)', 'Olpe', 'Ortenaukreis', 'Osnabrück', 'Ostalbkreis', 'Ostallgäu', 'Osterholz', 'Ostholstein', 'Ostprignitz-Ruppin', 'Paderborn', 'Passau', 'Peine', 'Pfaffenhofen a.d. Ilm', 'Pforzheim', 'Pinneberg', 'Pirmasens', 'Plön', 'Potsdam', 'Potsdam-Mittelmark', 'Prignitz', 'Rastatt', 'Ravensburg', 'Recklinghausen', 'Regen', 'Regensburg', 'Region Hannover', 'Regionalverband Saarbrücken', 'Remscheid', 'Rems-Murr-Kreis', 'Rendsburg-Eckernförde', 'Reutlingen', 'Rhein-Erft-Kreis', 'Rheingau-Taunus-Kreis', 'Rhein-Hunsrück-Kreis', 'Rheinisch-Bergischer Kreis', 'Rhein-Kreis Neuss', 'Rhein-Lahn-Kreis', 'Rhein-Neckar-Kreis', 'Rhein-Pfalz-Kreis', 'Rhein-Sieg-Kreis', 'Rhön-Grabfeld', 'Rosenheim', 'Rostock', 'Rotenburg (Wümme)', 'Roth', 'Rottal-Inn', 'Rottweil', 'Saale-Holzland-Kreis', 'Saalekreis', 'Saale-Orla-Kreis', 'Saalfeld-Rudolstadt', 'Saarlouis', 'Saarpfalz-Kreis', 'Sächsische Schweiz-Osterzgebirge', 'Salzgitter', 'Salzlandkreis', 'Schaumburg', 'Schleswig-Flensburg', 'Schmalkalden-Meiningen', 'Schwabach', 'Schwäbisch Hall', 'Schwalm-Eder-Kreis', 'Schwandorf', 'Schwarzwald-Baar-Kreis', 'Schweinfurt', 'Schwerin', 'Segeberg', 'Siegen-Wittgenstein', 'Sigmaringen', 'Soest', 'Solingen', 'Sömmerda', 'Sonneberg', 'Speyer', 'Spree-Neiße', 'St. Wendel', 'Stade', 'Städteregion Aachen', 'Starnberg', 'Steinburg', 'Steinfurt', 'Stendal', 'Stormarn', 'Straubing', 'Straubing-Bogen', 'Stuttgart', 'Südliche Weinstraße', 'Südwestpfalz', 'Suhl', 'Teltow-Fläming', 'Tirschenreuth', 'Traunstein', 'Trier', 'Trier-Saarburg', 'Tübingen', 'Tuttlingen', 'Uckermark', 'Uelzen', 'Ulm', 'Unna', 'Unstrut-Hainich-Kreis', 'Unterallgäu', 'Vechta', 'Verden', 'Viersen', 'Vogelsbergkreis', 'Vogtlandkreis', 'Vorpommern-Greifswald', 'Vorpommern-Rügen', 'Vulkaneifel', 'Waldeck-Frankenberg', 'Waldshut', 'Warendorf', 'Wartburgkreis', 'Weiden i.d. OPf.', 'Weilheim-Schongau', 'Weimar', 'Weimarer Land', 'Weißenburg-Gunzenhausen', 'Werra-Meißner-Kreis', 'Wesel', 'Wesermarsch', 'Westerwaldkreis', 'Wetteraukreis', 'Wiesbaden', 'Wilhelmshaven', 'Wittenberg', 'Wittmund', 'Wolfenbüttel', 'Wolfsburg', 'Worms', 'Wunsiedel i. Fichtelgebirge', 'Wuppertal', 'Würzburg', 'Zollernalbkreis', 'Zweibrücken', 'Zwickau']