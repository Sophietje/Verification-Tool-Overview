#!/Users/grammarware/opt/anaconda3/bin/python
import unittest

import hyper

class TestConverter(unittest.TestCase):
    def test_text2text_0_a(self):
        self.assertEqual(hyper.text2text('a'), 'a')

    def test_text2text_1_ee(self):
        self.assertEqual(hyper.text2text('`'), '`')
    def test_text2text_1_eA(self):
        self.assertEqual(hyper.text2text('`a'), '`a')
    def test_text2text_1_Ae(self):
        self.assertEqual(hyper.text2text('a`'), 'a`')
    def test_text2text_1_AA(self):
        self.assertEqual(hyper.text2text('a`b'), 'a`b')

    def test_text2text_2_eee(self):
        self.assertEqual(hyper.text2text('``'), '``')
    def test_text2text_2_eeA(self):
        self.assertEqual(hyper.text2text('``a'), '``a')
    def test_text2text_2_eAe(self):
        self.assertEqual(hyper.text2text('`a`'), '<code>a</code>')
    def test_text2text_2_eAA(self):
        self.assertEqual(hyper.text2text('`a`b'), '<code>a</code>b')
    def test_text2text_2_Aee(self):
        self.assertEqual(hyper.text2text('a``'), 'a``')
    def test_text2text_2_AeA(self):
        self.assertEqual(hyper.text2text('a``b'), 'a``b')
    def test_text2text_2_AAe(self):
        self.assertEqual(hyper.text2text('a`b`'), 'a<code>b</code>')
    def test_text2text_2_AAA(self):
        self.assertEqual(hyper.text2text('a`b`c'), 'a<code>b</code>c')

    def test_text2text_3_eeee(self):
        # opens a block in proper Markdown
        self.assertEqual(hyper.text2text('```'), '```')
    def test_text2text_3_eeeA(self):
        self.assertEqual(hyper.text2text('```a'), '```a')
    def test_text2text_3_eeAe(self):
        self.assertEqual(hyper.text2text('``a`'), '``a`')
    def test_text2text_3_eeAA(self):
        self.assertEqual(hyper.text2text('``a`b'), '``a`b')
    def test_text2text_3_eAee(self):
        self.assertEqual(hyper.text2text('`a``'), '<code>a</code>`')
    def test_text2text_3_eAeA(self):
        self.assertEqual(hyper.text2text('`a``b'), '<code>a</code>`b')
    def test_text2text_3_eAAe(self):
        self.assertEqual(hyper.text2text('`a`b`'), '<code>a</code>b`')
    def test_text2text_3_eAAA(self):
        self.assertEqual(hyper.text2text('`a`b`c'), '<code>a</code>b`c')
    def test_text2text_3_Aeee(self):
        self.assertEqual(hyper.text2text('a```'), 'a```')
    def test_text2text_3_AeeA(self):
        self.assertEqual(hyper.text2text('a```b'), 'a```b')
    def test_text2text_3_AeAe(self):
        self.assertEqual(hyper.text2text('a``b`'), 'a``b`')
    def test_text2text_3_AeAA(self):
        self.assertEqual(hyper.text2text('a``b`c'), 'a``b`c')
    def test_text2text_3_AAee(self):
        self.assertEqual(hyper.text2text('a`b``'), 'a<code>b</code>`')
    def test_text2text_3_AAeA(self):
        self.assertEqual(hyper.text2text('a`b``c'), 'a<code>b</code>`c')
    def test_text2text_3_AAAe(self):
        self.assertEqual(hyper.text2text('a`b`c`'), 'a<code>b</code>c`')
    def test_text2text_3_AAAA(self):
        self.assertEqual(hyper.text2text('a`b`c`d'), 'a<code>b</code>c`d')

    def test_text2text_after_code1(self):
        self.assertEqual(hyper.text2text('`a``b`'), '<code>ab</code>')
    def test_text2text_after_code2(self):
        self.assertEqual(hyper.text2text('`a`b`c`'), '<code>a</code>b<code>c</code>')
    def test_text2text_after_code2(self):
        self.assertEqual(hyper.text2text('`PASS`, `FAIL` or `UNKNOWN`?'),
            '<code>PASS</code>, <code>FAIL</code> or <code>UNKNOWN</code>?')


    def test_internal_link_expl(self):
        self.assertEqual(hyper.link2link(\
            '2LS is a C program analyser built upon the [CProver](Frameworks/CProver.md) infrastructure'),
            '2LS is a C program analyser built upon the <a href="cprover.html">CProver</a> infrastructure')
    def test_internal_link_impl(self):
        self.assertEqual(hyper.link2link(\
            '[[BA]] format'),
            '<a href="ba.html">BA</a> format')
    def test_internal_link_both(self):
        self.assertEqual(hyper.link2link(\
            'Built on top of [[CakeML]]; [HOL](Provers/HOL.md)4'),
            'Built on top of <a href="cakeml.html">CakeML</a>; <a href="hol.html">HOL</a>4')
    def test_internal_link_none(self):
        self.assertEqual(hyper.link2link(\
            '[STMC can] statically verify'),
            '[STMC can] statically verify')
    def test_internal_link_tail(self):
        self.assertEqual(hyper.link2link(\
            'It is part of [CProver](../Frameworks/CProver.md)'),
            'It is part of <a href="cprover.html">CProver</a>')
    def test_internal_link_inter(self):
        self.assertEqual(hyper.link2link(\
            'I never finish ['),
            'I never finish [')
    def test_internal_link_inter_expl1(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [AnyTh'),
            'I never finish [AnyTh')
    def test_internal_link_inter_expl2(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [AnyThing]'),
            'I never finish [AnyThing]')
    def test_internal_link_inter_expl3(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [AnyThing](any'),
            'I never finish [AnyThing](any')
    def test_internal_link_inter_impl1(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [['),
            'I never finish [[')
    def test_internal_link_inter_impl2(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [[AnyTh'),
            'I never finish [[AnyTh')
    def test_internal_link_inter_impl3(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [[AnyThing]'),
            'I never finish [[AnyThing]')
    def test_internal_link_inter_impl4(self):
        self.assertEqual(hyper.link2link(\
            'I never finish [[AnyThing] and it remains unmatched'),
            'I never finish [[AnyThing] and it remains unmatched')
    def test_internal_link_inter_fig1(self):
        self.assertEqual(hyper.link2link(\
            'I never finish !'),
            'I never finish !')
    def test_internal_link_inter_fig2(self):
        self.assertEqual(hyper.link2link(\
            'I never finish !['),
            'I never finish ![')
    def test_internal_link_inter_fig3(self):
        self.assertEqual(hyper.link2link(\
            'I never finish ![['),
            'I never finish ![[')
    def test_internal_link_inter_fig4(self):
        self.assertEqual(hyper.link2link(\
            'I never finish ![[Any'),
            'I never finish ![[Any')
    def test_internal_link_inter_fig5(self):
        self.assertEqual(hyper.link2link(\
            'I never finish ![[AnyThing]'),
            'I never finish ![[AnyThing]')

    def test_text2text_ee(self):
        self.assertEqual(hyper.text2text('_'), '_')
    def test_text2text_eA(self):
        self.assertEqual(hyper.text2text('_a'), '_a')
    def test_text2text_Ae(self):
        self.assertEqual(hyper.text2text('a_'), 'a_')
    def test_text2text_AA(self):
        self.assertEqual(hyper.text2text('a_b'), 'a_b')

    def test_text2text_eee(self):
        self.assertEqual(hyper.text2text('__'), '__')
    def test_text2text_eeA(self):
        self.assertEqual(hyper.text2text('__a'), '__a')
    def test_text2text_eAe(self):
        self.assertEqual(hyper.text2text('_a_'), '<em>a</em>')
    def test_text2text_eAA(self):
        self.assertEqual(hyper.text2text('_a_b'), '<em>a</em>b')
    def test_text2text_Aee(self):
        self.assertEqual(hyper.text2text('a__'), 'a__')
    def test_text2text_AAe(self):
        self.assertEqual(hyper.text2text('a_b_'), 'a<em>b</em>')
    def test_text2text_AeA(self):
        self.assertEqual(hyper.text2text('a__b'), 'a__b')
    def test_text2text_AAA(self):
        self.assertEqual(hyper.text2text('a_b_c'), 'a<em>b</em>c')

    def test_text2text_eeee(self):
        self.assertEqual(hyper.text2text('___'), '___')
    def test_text2text_eeeA(self):
        self.assertEqual(hyper.text2text('___a'), '___a')
    def test_text2text_eeAe(self):
        self.assertEqual(hyper.text2text('__a_'), '_<em>a</em>')
    # def test_text2text_eeAA(self):
    #     self.assertEqual(hyper.text2text('__a_b'), '_<em>a</em>b')
    def test_text2text_eAee(self):
        self.assertEqual(hyper.text2text('_a__'), '<em>a</em>_')
    def test_text2text_eAeA(self):
        self.assertEqual(hyper.text2text('_a__b'), '<em>a</em>_b')
    def test_text2text_eAAe(self):
        self.assertEqual(hyper.text2text('_a_b_'), '<em>a</em>b_')
    def test_text2text_eAAA(self):
        self.assertEqual(hyper.text2text('_a_b_c'), '<em>a</em>b_c')
    def test_text2text_Aeee(self):
        self.assertEqual(hyper.text2text('a___'), 'a___')
    def test_text2text_AeeA(self):
        self.assertEqual(hyper.text2text('a___b'), 'a___b')
    def test_text2text_AeAe(self):
        self.assertEqual(hyper.text2text('a__b_'), 'a_<em>b</em>')
    # def test_text2text_AeAA(self):
    #     self.assertEqual(hyper.text2text('a__b_c'), 'a_<em>b</em>c')
    def test_text2text_AAee(self):
        self.assertEqual(hyper.text2text('a_b__'), 'a<em>b</em>_')
    def test_text2text_AAeA(self):
        self.assertEqual(hyper.text2text('a_b__c'), 'a<em>b</em>_c')
    def test_text2text_AAAe(self):
        self.assertEqual(hyper.text2text('a_b_c_'), 'a<em>b</em>c_')
    def test_text2text_AAAA(self):
        self.assertEqual(hyper.text2text('a_b_c_d'), 'a<em>b</em>c_d')

    def test_text2text_eeeee(self):
        self.assertEqual(hyper.text2text('____'), '____')
    def test_text2text_eeeeA(self):
        self.assertEqual(hyper.text2text('____a'), '____a')
    def test_text2text_eeeAe(self):
        self.assertEqual(hyper.text2text('___a_'), '__<em>a</em>')
    # def test_text2text_eeeAA(self):
    #     self.assertEqual(hyper.text2text('___a_b'), '__<em>a</em>b')
    def test_text2text_eeAee(self):
        self.assertEqual(hyper.text2text('__a__'), '<strong>a</strong>')
    def test_text2text_eeAeA(self):
        self.assertEqual(hyper.text2text('__a__b'), '<strong>a</strong>b')
    def test_text2text_eeAAe(self):
        # NB: alternative implementation would be   '_<em>a</em>b_'
        self.assertEqual(hyper.text2text('__a_b_'), '_<em>a_b</em>')
    # def test_text2text_eeAAA(self):
    #     self.assertEqual(hyper.text2text('__a_b_c'), '_<em>a</em>b_c')
    def test_text2text_eAeee(self):
        self.assertEqual(hyper.text2text('_a___'), '<em>a</em>__')
    def test_text2text_eAeeA(self):
        self.assertEqual(hyper.text2text('_a___b'), '<em>a</em>__b')
    def test_text2text_eAeAe(self):
        self.assertEqual(hyper.text2text('_a__b_'), '<em>ab</em>')
    def test_text2text_eAeAA(self):
        self.assertEqual(hyper.text2text('_a__b_c'), '<em>ab</em>c')
    def test_text2text_eAAee(self):
        self.assertEqual(hyper.text2text('_a_b__'), '<em>a</em>b__')
    def test_text2text_eAAeA(self):
        self.assertEqual(hyper.text2text('_a_b__c'), '<em>a</em>b__c')
    def test_text2text_eAAAe(self):
        self.assertEqual(hyper.text2text('_a_b_c_'), '<em>a</em>b<em>c</em>')
    def test_text2text_eAAAA(self):
        self.assertEqual(hyper.text2text('_a_b_c_d'), '<em>a</em>b<em>c</em>d')
    def test_text2text_Aeeee(self):
        self.assertEqual(hyper.text2text('a____'), 'a____')
    def test_text2text_AeeeA(self):
        self.assertEqual(hyper.text2text('a____b'), 'a____b')
    def test_text2text_AeeAe(self):
        self.assertEqual(hyper.text2text('a___b_'), 'a__<em>b</em>')
    # def test_text2text_AeeAA(self):
    #     self.assertEqual(hyper.text2text('a___b_c'), 'a__<em>b</em>c')
    def test_text2text_AeAee(self):
        self.assertEqual(hyper.text2text('a__b__'), 'a<strong>b</strong>')
    def test_text2text_AeAeA(self):
        self.assertEqual(hyper.text2text('a__b__c'), 'a<strong>b</strong>c')
    def test_text2text_AeAAe(self):
        # NB: alternative interpretation could be    'a_<em>b</em>c_')
        self.assertEqual(hyper.text2text('a__b_c_'), 'a_<em>b_c</em>')
    # def test_text2text_AeAAA(self):
    #     self.assertEqual(hyper.text2text('a__b_c_d'), 'a_<em>b</em>c_d')
    def test_text2text_AAeee(self):
        self.assertEqual(hyper.text2text('a_b___'), 'a<em>b</em>__')
    def test_text2text_AAeeA(self):
        self.assertEqual(hyper.text2text('a_b___c'), 'a<em>b</em>__c')
    def test_text2text_AAeAe(self):
        self.assertEqual(hyper.text2text('a_b__c_'), 'a<em>bc</em>')
    def test_text2text_AAeAA(self):
        self.assertEqual(hyper.text2text('a_b__c_d'), 'a<em>bc</em>d')
    def test_text2text_AAAee(self):
        self.assertEqual(hyper.text2text('a_b_c__'), 'a<em>b</em>c__')
    def test_text2text_AAAeA(self):
        self.assertEqual(hyper.text2text('a_b_c__d'), 'a<em>b</em>c__d')
    def test_text2text_AAAAe(self):
        self.assertEqual(hyper.text2text('a_b_c_d_'), 'a<em>b</em>c<em>d</em>')
    def test_text2text_AAAAA(self):
        self.assertEqual(hyper.text2text('a_b_c_d_e'), 'a<em>b</em>c<em>d</em>e')

    def test_text2text_combo_eeeee(self):
        self.assertEqual(hyper.text2text('_****_'), '<em>****</em>')
    def test_text2text_combo_eeeeA(self):
        self.assertEqual(hyper.text2text('_****_a'), '<em>****</em>a')
    def test_text2text_combo_eeeAe(self):
        self.assertEqual(hyper.text2text('_****a_'), '<em>****a</em>')
    def test_text2text_combo_eeeAA(self):
        self.assertEqual(hyper.text2text('_****a_b'), '<em>****a</em>b')
    def test_text2text_combo_eeAee(self):
        self.assertEqual(hyper.text2text('_**a**_'), '<em><strong>a</strong></em>')
    def test_text2text_combo_eeAeA(self):
        self.assertEqual(hyper.text2text('_**a**_b'), '<em><strong>a</strong></em>b')
    def test_text2text_combo_eeAAe(self):
        self.assertEqual(hyper.text2text('_**a**b_'), '<em><strong>a</strong>b</em>')
    def test_text2text_combo_eeAAA(self):
        self.assertEqual(hyper.text2text('_**a**b_c'), '<em><strong>a</strong>b</em>c')
    def test_text2text_combo_eAeee(self):
        self.assertEqual(hyper.text2text('_a****_'), '<em>a****</em>')
    def test_text2text_combo_eAeeA(self):
        self.assertEqual(hyper.text2text('_a****_b'), '<em>a****</em>b')
    def test_text2text_combo_eAeAe(self):
        self.assertEqual(hyper.text2text('_a****b_'), '<em>a****b</em>')
    def test_text2text_combo_eAeAA(self):
        self.assertEqual(hyper.text2text('_a****b_c'), '<em>a****b</em>c')
    def test_text2text_combo_eAAee(self):
        self.assertEqual(hyper.text2text('_a**b**_'), '<em>a<strong>b</strong></em>')
    def test_text2text_combo_eAAeA(self):
        self.assertEqual(hyper.text2text('_a**b**_c'), '<em>a<strong>b</strong></em>c')
    def test_text2text_combo_eAAAe(self):
        self.assertEqual(hyper.text2text('_a**b**c_'), '<em>a<strong>b</strong>c</em>')
    def test_text2text_combo_eAAAA(self):
        self.assertEqual(hyper.text2text('_a**b**c_d'), '<em>a<strong>b</strong>c</em>d')
    def test_text2text_combo_Aeeee(self):
        self.assertEqual(hyper.text2text('a_****_'), 'a<em>****</em>')
    def test_text2text_combo_AeeeA(self):
        self.assertEqual(hyper.text2text('a_****_b'), 'a<em>****</em>b')
    def test_text2text_combo_AeeAe(self):
        self.assertEqual(hyper.text2text('a_****b_'), 'a<em>****b</em>')
    def test_text2text_combo_AeeAA(self):
        self.assertEqual(hyper.text2text('a_****b_c'), 'a<em>****b</em>c')
    def test_text2text_combo_AeAee(self):
        self.assertEqual(hyper.text2text('a_**b**_'), 'a<em><strong>b</strong></em>')
    def test_text2text_combo_AeAeA(self):
        self.assertEqual(hyper.text2text('a_**b**_c'), 'a<em><strong>b</strong></em>c')
    def test_text2text_combo_AeAAe(self):
        self.assertEqual(hyper.text2text('a_**b**c_'), 'a<em><strong>b</strong>c</em>')
    def test_text2text_combo_AeAAA(self):
        self.assertEqual(hyper.text2text('a_**b**c_d'), 'a<em><strong>b</strong>c</em>d')
    def test_text2text_combo_AAeee(self):
        self.assertEqual(hyper.text2text('a_b****_'), 'a<em>b****</em>')
    def test_text2text_combo_AAeeA(self):
        self.assertEqual(hyper.text2text('a_b****_c'), 'a<em>b****</em>c')
    def test_text2text_combo_AAeAe(self):
        self.assertEqual(hyper.text2text('a_b****c_'), 'a<em>b****c</em>')
    def test_text2text_combo_AAeAA(self):
        self.assertEqual(hyper.text2text('a_b****c_d'), 'a<em>b****c</em>d')
    def test_text2text_combo_AAAee(self):
        self.assertEqual(hyper.text2text('a_b**c**_'), 'a<em>b<strong>c</strong></em>')
    def test_text2text_combo_AAAeA(self):
        self.assertEqual(hyper.text2text('a_b**c**_d'), 'a<em>b<strong>c</strong></em>d')
    def test_text2text_combo_AAAAe(self):
        self.assertEqual(hyper.text2text('a_b**c**d_'), 'a<em>b<strong>c</strong>d</em>')
    def test_text2text_combo_AAAAA(self):
        self.assertEqual(hyper.text2text('a_b**c**d_e'), 'a<em>b<strong>c</strong>d</em>e')


A = '@'
def nextA(x):
    if x != 'A':
        return ''
    global A
    current = A
    A = chr(ord(A)+1)
    return current

def gen():
    global A
    for i in range(0,32):
        A = 'a'
        pattern = bin(i)[2:].replace('0','e').replace('1','A')
        while len(pattern) < 5:
            pattern = 'e' + pattern
        print(f'def test_text2text_combo_{pattern}(self):')
        # pattern = '_'.join(['a' if s == 'A' else '' for s in pattern])
        pattern = f'{nextA(pattern[0])}_{nextA(pattern[1])}**{nextA(pattern[2])}**{nextA(pattern[3])}_{nextA(pattern[4])}'
        print(f"    self.assertEqual(hyper.text2text('{pattern}'), '{hyper.text2text(pattern)}')")

def debug():
    i = '`a``'
    print(f'[$]  INPUT: "{i}"')
    o = hyper.text2text(i)
    print(f'[$] OUTPUT: "{o}"')

if __name__ == '__main__':
    # gen()
    # debug()
    unittest.main()
