import inspect
import pytest
import giro

class TestGiro:

    def test_giro1936(self):

        stage11_profile = """20.0 km,Monte Terminillo,C.1,2217m"""
        edition = giro.giro1936()
        assert edition.get_stage("11").profile == inspect.cleandoc(stage11_profile)

    def test_giro1937(self):

        stage8a_profile = """20.0 km,Monte Terminillo,C.1,2217m"""
        edition = giro.giro1937()
        assert edition.get_stage("8a").profile == inspect.cleandoc(stage8a_profile)

    def test_giro1938(self):

        stage7a_profile = """19.8 km,Monte Terminillo,C.1,2217m"""
        edition = giro.giro1938()
        assert edition.get_stage("7a").profile == inspect.cleandoc(stage7a_profile)

    def test_giro1939(self):

        stage6b_profile = """14.0 km,Monte Terminillo,C.1,2217m"""
        stage14_profile = """195.0 km,Cortina d'Ampezzo,C.1,1224m"""

        edition = giro.giro1939()

        assert edition.get_stage("6b").profile == inspect.cleandoc(stage6b_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)

    def test_giro1948(self):

        stage16_profile = """90.0 km,Cortina d'Ampezzo,C.1,1224m"""
        edition = giro.giro1948()
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)

    def test_giro1951(self):

        stage17_profile = """255.0 km,Cortina d'Ampezzo,C.1,1224m"""
        stage19_profile = """166.0 km,Saint Moritz,C.1,1822m"""

        edition = giro.giro1951()

        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro1953(self):

        stage19_profile = """125.0 km,Bormio,C.1,1225m"""
        edition = giro.giro1953()
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro1954(self):

        stage11_profile = """230.0 km,Abetone,C.2,1386m"""
        stage19_profile = """247.0 km,San Martino di Castrozza,C.2,1487m"""
        stage21_profile = """222.0 km,Saint Moritz,C.1,1822m"""

        edition = giro.giro1954()

        assert edition.get_stage("11").profile == inspect.cleandoc(stage11_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)

    def test_giro1955(self):

        stage18_profile = """236.0 km,Cortina d'Ampezzo,C.1,1224m"""
        edition = giro.giro1955()
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1956(self):

        stage18_profile = """242.0 km,Monte Bondone,C.1,1685m"""
        edition = giro.giro1956()
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1957(self):

        stage18_profile = """242.0 km,Monte Bondone,C.1,1685m"""
        edition = giro.giro1957()
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1959(self):

        stage3_profile = """180.0 km,Abetone,C.2,1386m"""
        stage7_profile = """8.0 km,Mount Vesuvius,C.1,1030m"""

        edition = giro.giro1959()

        assert edition.get_stage("3").profile == inspect.cleandoc(stage3_profile)
        assert edition.get_stage("7").profile == inspect.cleandoc(stage7_profile)

    def test_giro1960(self):

        stage12_profile = """176.0 km,Cervinia,C.1,2001m"""
        stage20_profile = """229.0 km,Bormio,C.1,1225m"""

        edition = giro.giro1960()

        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro1961(self):

        stage20_profile = """275.0 km,Bormio,C.1,1225m"""
        edition = giro.giro1961()
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro1962(self):

        stage7_profile = """224.0 km,Montevergine di Mercogliano,C.2,1260m"""
        stage14_profile = """160.0 km,Passo Rolle,C.2,1980m"""
        stage15_profile = """215.0 km,Aprica,C.3,1173m"""

        edition = giro.giro1962()

        assert edition.get_stage("7").profile == inspect.cleandoc(stage7_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)

    def test_giro1965(self):

        stage20_profile = """160.0 km,Passo dello Stelvio,C.1,2757m"""
        edition = giro.giro1965()
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro1967(self):

        stage12_profile = """220.0 km,Blockhaus,C.1,1210m"""
        stage19_profile = """170.0 km,Tre Cime di Lavaredo,C.1,2333m"""
        stage22a_profile = """137.0 km,Madonna del Ghisallo,C.3,754m"""

        edition = giro.giro1967()

        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)
        assert edition.get_stage("22a").profile == inspect.cleandoc(stage22a_profile)

    def test_giro1968(self):

        stage10_profile = """136.0 km,Monte Grappa,C.1,1745m"""
        stage12_profile = """213.0 km,Tre Cime di Lavaredo,C.1,2333m"""
        stage21_profile = """198.0 km,Blockhaus,C.1,1210m"""

        edition = giro.giro1968()

        assert edition.get_stage("10").profile == inspect.cleandoc(stage10_profile)
        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)

    def test_giro1971(self):

        stage17_profile = """206.0 km,Großglockner,C.1,1908m"""
        edition = giro.giro1971()
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

    def test_giro1972(self):

        stage4a_profile = """48.0 km,Blockhaus,C.1,1210m"""
        stage14_profile = """256.0 km,Monte Jafferau,C.1,1908m"""
        stage16_profile = """256.0 km,Livigno,C.1,1816m"""
        stage17_profile = """88.0 km,Passo dello Stelvio,C.1,2757m"""

        edition = giro.giro1972()

        assert edition.get_stage("4a").profile == inspect.cleandoc(stage4a_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

    def test_giro1973(self):

        stage8_profile = """156.0 km,Monte Carpegna,C.1,1369m"""
        stage18_profile = """173.0 km,Andalo,C.3,1024m"""

        edition = giro.giro1973()

        assert edition.get_stage("8").profile == inspect.cleandoc(stage8_profile)
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1974(self):

        stage16_profile = """158.0 km,Monte Generoso,C.1,1158m"""
        stage20_profile = """163.0 km,Tre Cime di Lavaredo,C.1,2333m"""

        edition = giro.giro1974()

        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro1975(self):

        stage17b_profile = """46.0 km,Monte Maddalena,C.1,844m"""
        stage21_profile = """186.0 km,Passo dello Stelvio,C.1,2757m"""

        edition = giro.giro1975()

        assert edition.get_stage("17b").profile == inspect.cleandoc(stage17b_profile)
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)

    def test_giro1977(self):

        stage17_profile = """220.0 km,Cortina d'Ampezzo,C.1,1224m"""
        edition = giro.giro1977()
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

    def test_giro1978(self):

        stage12_profile = """204.0 km,Monte Trebbio,C.1,575m"""
        stage17_profile = """205.0 km,Monte Bondone,C.1,1685m"""

        edition = giro.giro1978()

        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

    def test_giro1980(self):

        stage18_profile = """239.0 km,Zoldo Alto,C.2,1514m"""
        edition = giro.giro1980()
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1981(self):

        stage20_profile = """100.0 km,Tre Cime di Lavaredo,C.1,2333m"""
        edition = giro.giro1981()
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro1982(self):

        stage16_profile = """243.0 km,San Martino di Castrozza,C.2,1487m"""
        stage18_profile = """85.0 km,Montecampione,C.1,1200m"""

        edition = giro.giro1982()

        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1984(self):

        stage5_profile = """194.0 km,Blockhaus,C.1,1210m"""
        edition = giro.giro1984()
        assert edition.get_stage("5").profile == inspect.cleandoc(stage5_profile)

    def test_giro1987(self):

        stage6_profile = """134.0 km,Monte Terminillo,C.1,2217m"""
        edition = giro.giro1987()
        assert edition.get_stage("6").profile == inspect.cleandoc(stage6_profile)

    def test_giro1988(self):

        stage14_profile = """120.0 km,Bormio,C.1,1225m"""
        edition = giro.giro1988()
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)

    def test_giro1989(self):

        stage2_profile = """132.0 km,Mount Etna,C.1,1736m"""
        stage18_profile = """10.7 km,Monte Generoso,C.1,1158m"""

        edition = giro.giro1989()

        assert edition.get_stage("2").profile == inspect.cleandoc(stage2_profile)
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

    def test_giro1990(self):

        stage2_profile = """190.0 km,Mount Vesuvius,C.1,1030m"""
        stage15_profile = """171.0 km,Passo Pordoi,C.1,2239m"""
        stage16_profile = """223.0 km,Aprica,C.3,1173m"""

        edition = giro.giro1990()

        assert edition.get_stage("2").profile == inspect.cleandoc(stage2_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)

    def test_giro1991(self):

        stage13_profile = """192.0 km,Sestrière,C.1,2035m"""
        stage15_profile = """132.0 km,Aprica,C.3,1173m"""
        stage17_profile = """169.0 km,Passo Pordoi,C.1,2239m"""

        edition = giro.giro1991()

        assert edition.get_stage("13").profile == inspect.cleandoc(stage13_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

    def test_giro1992(self):

        stage10_profile = """196.0 km,Monte Terminillo,C.1,2217m"""
        stage14_profile = """205.0 km,Monte Bondone,C.1,1685m"""

        edition = giro.giro1992()

        assert edition.get_stage("10").profile == inspect.cleandoc(stage10_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)

    def test_giro1993(self):

        stage19_profile = """55.0 km,Sestrière,C.1,2035m"""
        edition = giro.giro1993()
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro1994(self):

        stage15_profile = """195.0 km,Aprica,C.3,1173m"""
        stage20_profile = """206.0 km,Les Deux Alpes,C.1,1644m"""
        stage21_profile = """121.0 km,Sestrière,C.1,2035m"""

        edition = giro.giro1994()

        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)

    def test_giro1996(self):

        stage13_profile = """115.0 km,Prato Nevoso,C.1,1607m"""
        stage20_profile = """220.0 km,Passo Pordoi,C.1,2239m"""
        stage21_profile = """250.0 km,Aprica,C.3,1173m"""

        edition = giro.giro1996()

        assert edition.get_stage("13").profile == inspect.cleandoc(stage13_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)

    def test_giro1997(self):

        stage5_profile = """215.0 km,Monte Terminillo,C.1,2217m"""
        edition = giro.giro1997()

        assert edition.get_stage("5").profile == inspect.cleandoc(stage5_profile)

    def test_giro1998(self):

        stage19_profile = """239.0 km,Plan di Montecampione,C.1,1732m"""
        edition = giro.giro1998()
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro1999(self):

        stage19_profile = """166.0 km,Alpe di Pampeago,C.1,1983m"""
        stage20_profile = """175.0 km,Madonna di Campiglio,C.1,1715m"""
        stage21_profile = """190.0 km,Aprica,C.3,1173m"""

        edition = giro.giro1999()

        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)

    def test_giro2000(self):

        stage9_profile = """138.0 km,Abetone,C.2,1386m"""
        stage14_profile = """203.0 km,Bormio,C.1,1225m"""
        stage18_profile = """173.0 km,Prato Nevoso,C.1,1607m"""
        stage20_profile = """32.0 km,Sestrière,C.1,2035m"""

        edition = giro.giro2000()

        assert edition.get_stage("9").profile == inspect.cleandoc(stage9_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2001(self):

        stage13_profile = """225.0 km,Passo Pordoi,C.1,2239m"""
        edition = giro.giro2001()
        assert edition.get_stage("13").profile == inspect.cleandoc(stage13_profile)

    def test_giro2003(self):

        stage7_profile = """146.0 km,Monte Terminillo,C.1,2217m"""
        stage12_profile = """185.0 km,Monte Zoncolan,C.1,1730m"""
        stage14_profile = """162.0 km,Alpe di Pampeago,C.1,1983m"""

        edition = giro.giro2003()

        assert edition.get_stage("7").profile == inspect.cleandoc(stage7_profile)
        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)

    def test_giro2004(self):

        stage7_profile = """214.0 km,Montevergine di Mercogliano,C.2,1260m"""
        edition = giro.giro2004()
        assert edition.get_stage("7").profile == inspect.cleandoc(stage7_profile)

    def test_giro2005(self):

        stage11_profile = """150.0 km,Zoldo Alto,C.2,1514m"""
        stage14_profile = """210.0 km,Livigno,C.1,1816m"""
        stage19_profile = """190.0 km,Sestrière,C.1,2035m"""

        edition = giro.giro2005()

        assert edition.get_stage("11").profile == inspect.cleandoc(stage11_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro2006(self):

        stage17_profile = """133.0 km,Plan de Corones,C.1,2273m"""
        stage20_profile = """211.0 km,Aprica,C.3,1173m"""

        edition = giro.giro2006()

        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2007(self):

        stage4_profile = """153.0 km,Montevergine di Mercogliano,C.2,1260m"""
        stage15_profile = """184.0 km,Tre Cime di Lavaredo,C.1,2333m"""
        stage17_profile = """142.0 km,Monte Zoncolan,C.1,1730m"""

        edition = giro.giro2007()

        assert edition.get_stage("4").profile == inspect.cleandoc(stage4_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

    def test_giro2008(self):

        stage14_profile = """195.0 km,Alpe di Pampeago,C.1,1983m"""
        stage15_profile = """153.0 km,Passo Fedaia,C.1,2057m"""
        stage16_profile = """12.8 km,Plan de Corones,C.1,2273m"""

        edition = giro.giro2008()

        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)

    def test_giro2009(self):

        stage4_profile = """162.0 km,San Martino di Castrozza,C.2,1487m"""
        stage5_profile = """125.0 km,Alpe di Siusi,C.1,1844m"""
        stage16_profile = """237.0 km,Monte Petrano,C.1,1105m"""
        stage17_profile = """83.0 km,Blockhaus,C.1,1210m"""
        stage19_profile = """164.0 km,Mount Vesuvius,C.1,1030m"""

        edition = giro.giro2009()

        assert edition.get_stage("4").profile == inspect.cleandoc(stage4_profile)
        assert edition.get_stage("5").profile == inspect.cleandoc(stage5_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro2010(self):

        stage8_profile = """189.0 km,Monte Terminillo,C.1,2217m"""
        stage14_profile = """201.0 km,Asolo (Monte Grappa),C.1,1745m"""
        stage15_profile = """161.0 km,Monte Zoncolan,C.1,1730m"""
        stage16_profile = """12.9 km,Plan de Corones,C.1,2273m"""
        stage19_profile = """195.0 km,Aprica,C.3,1173m"""

        edition = giro.giro2010()

        assert edition.get_stage("8").profile == inspect.cleandoc(stage8_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro2011(self):

        stage7_profile = """110.0 km,Montevergine di Mercogliano,C.2,1260m"""
        stage13_profile = """167.0 km,Großglockner,C.1,1908m"""
        stage14_profile = """170.0 km,Monte Zoncolan,C.1,1730m"""
        stage20_profile = """242.0 km,Sestrière,C.1,2035m"""

        edition = giro.giro2011()

        assert edition.get_stage("7").profile == inspect.cleandoc(stage7_profile)
        assert edition.get_stage("13").profile == inspect.cleandoc(stage13_profile)
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2012(self):

        stage14_profile = """206.0 km,Cervinia,C.1,2001m"""
        stage17_profile = """186.0 km,Cortina d'Ampezzo,C.1,1224m"""
        stage19_profile = """198.0 km,Alpe di Pampeago,C.1,1983m"""
        stage20_profile = """219.0 km,Passo dello Stelvio,C.1,2757m"""

        edition = giro.giro2012()

        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2013(self):

        stage20_profile = """203.0 km,Tre Cime di Lavaredo,C.1,2333m"""
        edition = giro.giro2013()
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2014(self):

        stage15_profile = """225.0 km,Montecampione,C.1,1200m"""
        stage20_profile = """167.0 km,Monte Zoncolan,C.1,1730m"""

        edition = giro.giro2014()

        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2015(self):

        stage5_profile = """152.0 km,Abetone,C.2,1386m"""
        stage15_profile = """165.0 km,Madonna di Campiglio,C.1,1715m"""
        stage16_profile = """174.0 km,Aprica,C.3,1173m"""
        stage19_profile = """236.0 km,Cervinia,C.1,2001m"""
        stage20_profile = """196.0 km,Sestrière,C.1,2035m"""

        edition = giro.giro2015()

        assert edition.get_stage("5").profile == inspect.cleandoc(stage5_profile)
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2016(self):

        stage15_profile = """10.8 km,Alpe di Siusi/Seiseralm,C.1,1844m"""
        stage16_profile = """132.0 km,Andalo,C.3,1024m"""
        stage19_profile = """162.0 km,Risoul,C.1,1855m"""

        edition = giro.giro2016()

        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

    def test_giro2017(self):

        stage9_profile = """149.0 km,Blockhaus,C.1,1210m"""
        stage16_profile = """222.0 km,Bormio,C.1,1225m"""

        edition = giro.giro2017()

        assert edition.get_stage("9").profile == inspect.cleandoc(stage9_profile)
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)

    def test_giro2018(self):

        edition = giro.giro2018()

        stage2_profile = """91.0 km,Zikhrow Ya'Aqov,C.4,162m"""
        assert edition.get_stage("2").profile == inspect.cleandoc(stage2_profile)

        stage3_profile = """127.8 km,Faran River,C.4,322m"""
        assert edition.get_stage("3").profile == inspect.cleandoc(stage3_profile)

        stage4_profile = """86.4 km,Pietre Calde,C.4,779m
        154.5 km,Vizzini,C.4,595m"""
        assert edition.get_stage("4").profile == inspect.cleandoc(stage4_profile)

        stage5_profile = """90.7 km,Santa Margherita di Belice,C.4,430m
        111.8 km,Partanna,C.4,405m"""
        assert edition.get_stage("5").profile == inspect.cleandoc(stage5_profile)

        stage6_profile = """169.0 km,Mount Etna,C.1,1736m"""
        assert edition.get_stage("6").profile == inspect.cleandoc(stage6_profile)

        stage8_profile = """209.0 km,Montevergine di Mercogliano,C.2,1260m"""
        assert edition.get_stage("8").profile == inspect.cleandoc(stage8_profile)

        stage9_profile = """108.1 km,Roccaraso,C.2,1252m
        192.9 km,Calascio,C.2,1190m"""
        assert edition.get_stage("9").profile == inspect.cleandoc(stage9_profile)

        stage10_profile = """21.8 km,Forte Delia Creta,C.2,1254m
        61.2 km,Bruzzolana,C.3,523m
        213.5 km,Annifo,C.4,895m"""
        assert edition.get_stage("10").profile == inspect.cleandoc(stage10_profile)

        stage11_profile = """41.7 km,Passo Cornello,C.3,814m
        97.5 km,Valico di Pietra Rossa,C.3,674m
        156.0 km,Osimo,C.4,265m"""
        assert edition.get_stage("11").profile == inspect.cleandoc(stage11_profile)

        stage12_profile = """206.6 km,Tre Monti,C.4,252m"""
        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)

        stage13_profile = """160.7 km,Montello,C.4,242m"""
        assert edition.get_stage("13").profile == inspect.cleandoc(stage13_profile)

        stage14_profile = """43.3 km,Monte di Ragogna,C.3,494m
        106.0 km,Avaglio,C.3,738m
        142.5 km,Passo Duron,C.2,1609m
        165.8 km,Sella Valcalda Ravascletto,C.3,958m
        186.0 km,Monte Zoncolan,C.1,1730m"""
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)

        stage15_profile = """48.4 km,Passo della Mauria,C.3,1301m
        110.6 km,Passo Tre Croci,C.2,1805m
        146.9 km,Passo di Sant'Antonio,C.2,1470m
        160.6 km,Costalissoio (Bosco dei Giavi),C.2,1300m"""
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)

        stage17_profile = """71.5 km,Lodrino,C.3,736m"""
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

        stage18_profile = """196.0 km,Prato Nevoso,C.1,1607m"""
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

        stage19_profile = """48.9 km,Colle del Lys,C.2,1311m
        110.7 km,Colle delle Finestre,C.1,2178m
        138.4 km,Sestrière,C.3,2035m
        185.0 km,Bardonecchia (Monte Jafferau),C.1,1908m"""
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

        stage20_profile = """146.5 km,Col Tsecore (Col du Mont-Tseuc),C.1,1623m
        185.8 km,Col Saint Pantaléon,C.1,1664m
        214.0 km,Cervinia,C.1,2001m"""
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

    def test_giro2019(self):

        edition = giro.giro2019()

        stage2_profile = """157.6 km,Montalbano,C.3,424m
        178.7 km,San Baranto,C.4,340m"""
        assert edition.get_stage("2").profile == inspect.cleandoc(stage2_profile)

        stage3_profile = """182.0 km,Poggio L'Appartita,C.4,202m"""
        assert edition.get_stage("3").profile == inspect.cleandoc(stage3_profile)

        stage4_profile = """32.8 km,Manciano,C.4,389m"""
        assert edition.get_stage("4").profile == inspect.cleandoc(stage4_profile)

        stage5_profile = """87.2 km,Sezze,C.4,248m"""
        assert edition.get_stage("5").profile == inspect.cleandoc(stage5_profile)

        stage6_profile = """220.1 km,Coppa Casarinelle,C.2,678m"""
        assert edition.get_stage("6").profile == inspect.cleandoc(stage6_profile)

        stage7_profile = """138.8 km,Le Svolte di Popoli,C.2,746m"""
        assert edition.get_stage("7").profile == inspect.cleandoc(stage7_profile)

        stage8_profile = """168.5 km,Monte della Mattera,C.3,418m
        203.7 km,Monteluro,C.4,222m
        214.9 km,Gabicce Monte,C.4,120m"""
        assert edition.get_stage("8").profile == inspect.cleandoc(stage8_profile)

        stage12_profile = """125.9 km,Montoso,C.1,1248m"""
        assert edition.get_stage("12").profile == inspect.cleandoc(stage12_profile)

        stage13_profile = """54.3 km,Colle del Lys,C.1,1311m
        134.3 km,Pian del Lupo,C.2,1405m
        196.0 km,Ceresole Reale (Lago Serrù),C.1,2247m"""
        assert edition.get_stage("13").profile == inspect.cleandoc(stage13_profile)

        stage14_profile = """13.8 km,Verrayes,C.2,1017m
        51.5 km,Verrogne,C.1,1582m
        75.9 km,Truc d'Arbe,C.2,1256m
        106.1 km,Colle San Carlo,C.1,1951m"""
        assert edition.get_stage("14").profile == inspect.cleandoc(stage14_profile)

        stage15_profile = """173.7 km,Madonna del Ghisallo,C.2,754m
        189.6 km,Colman di Sormano,C.2,1124m"""
        assert edition.get_stage("15").profile == inspect.cleandoc(stage15_profile)

        stage16_profile = """89.6 km,Cevo,C.3,1054m
        128.2 km,Aprica,C.3,1173m
        166.3 km,Passo del Mortirolo,C.1,1854m"""
        assert edition.get_stage("16").profile == inspect.cleandoc(stage16_profile)

        stage17_profile = """114.0 km,Elva,C.4,824m
        135.3 km,Terento,C.3,1244m
        181.0 km,Anterselva/Antholz,C.3,1635m"""
        assert edition.get_stage("17").profile == inspect.cleandoc(stage17_profile)

        stage18_profile = """118.1 km,Pieve di Alpago,C.4,691m"""
        assert edition.get_stage("18").profile == inspect.cleandoc(stage18_profile)

        stage19_profile = """66.6 km,Passo di San Boldo,C.3,701m
        116.5 km,Lamon,C.4,594m
        151.0 km,San Martino di Castrozza,C.2,1487m"""
        assert edition.get_stage("19").profile == inspect.cleandoc(stage19_profile)

        stage20_profile = """27.1 km,Cima Campo,C.2,1425m
        78.0 km,Passo Manghen,C.1,2047m
        133.1 km,Passo Rolle,C.2,1980m
        183.1 km,Croce d'Aune,C.2,1015m
        194.0 km,Monte Avena,C.1,1225m"""
        assert edition.get_stage("20").profile == inspect.cleandoc(stage20_profile)

        stage21_profile = """9.5 km,Torricelle,C.4,277m"""
        assert edition.get_stage("21").profile == inspect.cleandoc(stage21_profile)
