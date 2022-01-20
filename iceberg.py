#!/Users/grammarware/opt/anaconda3/bin/python
import unittest

import hyper

class TestConverter(unittest.TestCase):
    def test_matched2code_0_a(self):
        self.assertEqual(hyper.matched2code('a'), 'a')

    def test_matched2code_1_ee(self):
        self.assertEqual(hyper.matched2code('`'), '`')
    def test_matched2code_1_ea(self):
        self.assertEqual(hyper.matched2code('`a'), '`a')
    def test_matched2code_1_ae(self):
        self.assertEqual(hyper.matched2code('a`'), 'a`')
    def test_matched2code_1_aa(self):
        self.assertEqual(hyper.matched2code('a`b'), 'a`b')

    def test_matched2code_2_eee(self):
        self.assertEqual(hyper.matched2code('``'), '')
    def test_matched2code_2_eea(self):
        self.assertEqual(hyper.matched2code('``a'), 'a')
    def test_matched2code_2_eae(self):
        self.assertEqual(hyper.matched2code('`a`'), '<code>a</code>')
    def test_matched2code_2_eaa(self):
        self.assertEqual(hyper.matched2code('`a`b'), '<code>a</code>b')
    def test_matched2code_2_aee(self):
        self.assertEqual(hyper.matched2code('a``'), 'a')
    def test_matched2code_2_aea(self):
        self.assertEqual(hyper.matched2code('a``b'), 'ab')
    def test_matched2code_2_aae(self):
        self.assertEqual(hyper.matched2code('a`b`'), 'a<code>b</code>')
    def test_matched2code_2_aaa(self):
        self.assertEqual(hyper.matched2code('a`b`c'), 'a<code>b</code>c')

    def test_matched2code_3_eeee(self):
        self.assertEqual(hyper.matched2code('```'), '')
    def test_matched2code_3_eeea(self):
        self.assertEqual(hyper.matched2code('```a'), '<code>a</code>')
    def test_matched2code_3_eeae(self):
        self.assertEqual(hyper.matched2code('``a`'), 'a')
    def test_matched2code_3_eeaa(self):
        self.assertEqual(hyper.matched2code('``a`b'), 'a<code>b</code>')
    def test_matched2code_3_eaee(self):
        self.assertEqual(hyper.matched2code('`a``'), '<code>a</code>')
    def test_matched2code_3_eaea(self):
        self.assertEqual(hyper.matched2code('`a``b'), '<code>ab</code>')
    def test_matched2code_3_eaae(self):
        self.assertEqual(hyper.matched2code('`a`b`'), '<code>a</code>b')
    def test_matched2code_3_eaaa(self):
        self.assertEqual(hyper.matched2code('`a`b`c'), '<code>a</code>b<code>c</code>')
    def test_matched2code_3_aeee(self):
        self.assertEqual(hyper.matched2code('a```'), 'a')
    def test_matched2code_3_aeea(self):
        self.assertEqual(hyper.matched2code('a```b'), 'a<code>b</code>')
    def test_matched2code_3_aeae(self):
        self.assertEqual(hyper.matched2code('a``b`'), 'ab')
    def test_matched2code_3_aeaa(self):
        self.assertEqual(hyper.matched2code('a``b`c'), 'ab<code>c</code>')
    def test_matched2code_3_aaee(self):
        self.assertEqual(hyper.matched2code('a`b``'), 'a<code>b</code>')
    def test_matched2code_3_aaea(self):
        self.assertEqual(hyper.matched2code('a`b``c'), 'a<code>bc</code>')
    def test_matched2code_3_aaae(self):
        self.assertEqual(hyper.matched2code('a`b`c`'), 'a<code>b</code>c')
    def test_matched2code_3_aaaa(self):
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
        

if __name__ == '__main__':
    unittest.main()