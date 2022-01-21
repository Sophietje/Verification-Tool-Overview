#!/Users/grammarware/opt/anaconda3/bin/python
import unittest

import hyper

class TestConverter(unittest.TestCase):
    def test_matched2code_0_a(self):
        self.assertEqual(hyper.matched2code('a'), 'a')

    def test_matched2code_1_ee(self):
        self.assertEqual(hyper.matched2code('`'), '`')
    def test_matched2code_1_eA(self):
        self.assertEqual(hyper.matched2code('`a'), '`a')
    def test_matched2code_1_Ae(self):
        self.assertEqual(hyper.matched2code('a`'), 'a`')
    def test_matched2code_1_AA(self):
        self.assertEqual(hyper.matched2code('a`b'), 'a`b')

    def test_matched2code_2_eee(self):
        self.assertEqual(hyper.matched2code('``'), '')
    def test_matched2code_2_eeA(self):
        self.assertEqual(hyper.matched2code('``a'), 'a')
    def test_matched2code_2_eAe(self):
        self.assertEqual(hyper.matched2code('`a`'), '<code>a</code>')
    def test_matched2code_2_eAA(self):
        self.assertEqual(hyper.matched2code('`a`b'), '<code>a</code>b')
    def test_matched2code_2_Aee(self):
        self.assertEqual(hyper.matched2code('a``'), 'a')
    def test_matched2code_2_AeA(self):
        self.assertEqual(hyper.matched2code('a``b'), 'ab')
    def test_matched2code_2_AAe(self):
        self.assertEqual(hyper.matched2code('a`b`'), 'a<code>b</code>')
    def test_matched2code_2_AAA(self):
        self.assertEqual(hyper.matched2code('a`b`c'), 'a<code>b</code>c')

    def test_matched2code_3_eeee(self):
        self.assertEqual(hyper.matched2code('```'), '')
    def test_matched2code_3_eeeA(self):
        self.assertEqual(hyper.matched2code('```a'), '<code>a</code>')
    def test_matched2code_3_eeAe(self):
        self.assertEqual(hyper.matched2code('``a`'), 'a')
    def test_matched2code_3_eeAA(self):
        self.assertEqual(hyper.matched2code('``a`b'), 'a<code>b</code>')
    def test_matched2code_3_eAee(self):
        self.assertEqual(hyper.matched2code('`a``'), '<code>a</code>')
    def test_matched2code_3_eAeA(self):
        self.assertEqual(hyper.matched2code('`a``b'), '<code>ab</code>')
    def test_matched2code_3_eAAe(self):
        self.assertEqual(hyper.matched2code('`a`b`'), '<code>a</code>b')
    def test_matched2code_3_eAAA(self):
        self.assertEqual(hyper.matched2code('`a`b`c'), '<code>a</code>b<code>c</code>')
    def test_matched2code_3_Aeee(self):
        self.assertEqual(hyper.matched2code('a```'), 'a')
    def test_matched2code_3_AeeA(self):
        self.assertEqual(hyper.matched2code('a```b'), 'a<code>b</code>')
    def test_matched2code_3_AeAe(self):
        self.assertEqual(hyper.matched2code('a``b`'), 'ab')
    def test_matched2code_3_AeAA(self):
        self.assertEqual(hyper.matched2code('a``b`c'), 'ab<code>c</code>')
    def test_matched2code_3_AAee(self):
        self.assertEqual(hyper.matched2code('a`b``'), 'a<code>b</code>')
    def test_matched2code_3_AAeA(self):
        self.assertEqual(hyper.matched2code('a`b``c'), 'a<code>bc</code>')
    def test_matched2code_3_AAAe(self):
        self.assertEqual(hyper.matched2code('a`b`c`'), 'a<code>b</code>c')
    def test_matched2code_3_AAAA(self):
        self.assertEqual(hyper.matched2code('a`b`c`d'), 'a<code>b</code>c<code>d</code>')

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
        self.assertEqual(hyper.my_md_converter('_'), '_')
    def test_text2text_eA(self):
        self.assertEqual(hyper.my_md_converter('_a'), '_a')
    def test_text2text_Ae(self):
        self.assertEqual(hyper.my_md_converter('a_'), 'a_')
    def test_text2text_AA(self):
        self.assertEqual(hyper.my_md_converter('a_b'), 'a_b')

    def test_text2text_eee(self):
        self.assertEqual(hyper.my_md_converter('__'), '__')
    def test_text2text_eeA(self):
        self.assertEqual(hyper.my_md_converter('__a'), '__a')
    def test_text2text_eAe(self):
        self.assertEqual(hyper.my_md_converter('_a_'), '<em>a</em>')
    def test_text2text_eAA(self):
        self.assertEqual(hyper.my_md_converter('_a_b'), '<em>a</em>b')
    def test_text2text_Aee(self):
        self.assertEqual(hyper.my_md_converter('a__'), 'a__')
    def test_text2text_AAe(self):
        self.assertEqual(hyper.my_md_converter('a_b_'), 'a<em>b</em>')
    def test_text2text_AeA(self):
        self.assertEqual(hyper.my_md_converter('a__b'), 'a__b')
    def test_text2text_AAA(self):
        self.assertEqual(hyper.my_md_converter('a_b_c'), 'a<em>b</em>c')

    def test_text2text_eeee(self):
        self.assertEqual(hyper.my_md_converter('___'), '___')
    def test_text2text_eeeA(self):
        self.assertEqual(hyper.my_md_converter('___a'), '___a')
    def test_text2text_eeAe(self):
        self.assertEqual(hyper.my_md_converter('__a_'), '_<em>a</em>')
    def test_text2text_eeAA(self):
        self.assertEqual(hyper.my_md_converter('__a_b'), '_<em>a</em>b')
    def test_text2text_eAee(self):
        self.assertEqual(hyper.my_md_converter('_a__'), '<em>a</em>_')
    def test_text2text_eAeA(self):
        self.assertEqual(hyper.my_md_converter('_a__b'), '<em>a</em>_b')
    def test_text2text_eAAe(self):
        self.assertEqual(hyper.my_md_converter('_a_b_'), '<em>a</em>b_')
    def test_text2text_eAAA(self):
        self.assertEqual(hyper.my_md_converter('_a_b_c'), '<em>a</em>b_c')
    def test_text2text_Aeee(self):
        self.assertEqual(hyper.my_md_converter('a___'), 'a___')
    def test_text2text_AeeA(self):
        self.assertEqual(hyper.my_md_converter('a___b'), 'a___b')
    def test_text2text_AeAe(self):
        self.assertEqual(hyper.my_md_converter('a__b_'), 'a_<em>b</em>')
    def test_text2text_AeAA(self):
        self.assertEqual(hyper.my_md_converter('a__b_c'), 'a_<em>b</em>c')
    def test_text2text_AAee(self):
        self.assertEqual(hyper.my_md_converter('a_b__'), 'a<em>b</em>_')
    def test_text2text_AAeA(self):
        self.assertEqual(hyper.my_md_converter('a_b__c'), 'a<em>b</em>_c')
    def test_text2text_AAAe(self):
        self.assertEqual(hyper.my_md_converter('a_b_c_'), 'a<em>b</em>c_')
    def test_text2text_AAAA(self):
        self.assertEqual(hyper.my_md_converter('a_b_c_d'), 'a<em>b</em>c_d')

if __name__ == '__main__':
    unittest.main()