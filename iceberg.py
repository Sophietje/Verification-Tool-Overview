#!/Users/grammarware/opt/anaconda3/bin/python
import unittest

import hyper

class TestConverter(unittest.TestCase):
    def test_backticks2code_0_a(self):
        self.assertEqual(hyper.backticks2code('a'), 'a')

    def test_backticks2code_1_ee(self):
        self.assertEqual(hyper.backticks2code('`'), '')
    def test_backticks2code_1_ea(self):
        self.assertEqual(hyper.backticks2code('`a'), '<code>a</code>')
    def test_backticks2code_1_ae(self):
        self.assertEqual(hyper.backticks2code('a`'), 'a')
    def test_backticks2code_1_aa(self):
        self.assertEqual(hyper.backticks2code('a`b'), 'a<code>b</code>')

    def test_backticks2code_2_eee(self):
        self.assertEqual(hyper.backticks2code('``'), '')
    def test_backticks2code_2_eea(self):
        self.assertEqual(hyper.backticks2code('``a'), 'a')
    def test_backticks2code_2_eae(self):
        self.assertEqual(hyper.backticks2code('`a`'), '<code>a</code>')
    def test_backticks2code_2_eaa(self):
        self.assertEqual(hyper.backticks2code('`a`b'), '<code>a</code>b')
    def test_backticks2code_2_aee(self):
        self.assertEqual(hyper.backticks2code('a``'), 'a')
    def test_backticks2code_2_aea(self):
        self.assertEqual(hyper.backticks2code('a``b'), 'ab')
    def test_backticks2code_2_aae(self):
        self.assertEqual(hyper.backticks2code('a`b`'), 'a<code>b</code>')
    def test_backticks2code_2_aaa(self):
        self.assertEqual(hyper.backticks2code('a`b`c'), 'a<code>b</code>c')

    def test_backticks2code_3_eeee(self):
        self.assertEqual(hyper.backticks2code('```'), '')
    def test_backticks2code_3_eeea(self):
        self.assertEqual(hyper.backticks2code('```a'), '<code>a</code>')
    def test_backticks2code_3_eeae(self):
        self.assertEqual(hyper.backticks2code('``a`'), 'a')
    def test_backticks2code_3_eeaa(self):
        self.assertEqual(hyper.backticks2code('``a`b'), 'a<code>b</code>')
    def test_backticks2code_3_eaee(self):
        self.assertEqual(hyper.backticks2code('`a``'), '<code>a</code>')
    def test_backticks2code_3_eaea(self):
        self.assertEqual(hyper.backticks2code('`a``b'), '<code>ab</code>')
    def test_backticks2code_3_eaae(self):
        self.assertEqual(hyper.backticks2code('`a`b`'), '<code>a</code>b')
    def test_backticks2code_3_eaaa(self):
        self.assertEqual(hyper.backticks2code('`a`b`c'), '<code>a</code>b<code>c</code>')
    def test_backticks2code_3_aeee(self):
        self.assertEqual(hyper.backticks2code('a```'), 'a')
    def test_backticks2code_3_aeea(self):
        self.assertEqual(hyper.backticks2code('a```b'), 'a<code>b</code>')
    def test_backticks2code_3_aeae(self):
        self.assertEqual(hyper.backticks2code('a``b`'), 'ab')
    def test_backticks2code_3_aeaa(self):
        self.assertEqual(hyper.backticks2code('a``b`c'), 'ab<code>c</code>')
    def test_backticks2code_3_aaee(self):
        self.assertEqual(hyper.backticks2code('a`b``'), 'a<code>b</code>')
    def test_backticks2code_3_aaea(self):
        self.assertEqual(hyper.backticks2code('a`b``c'), 'a<code>bc</code>')
    def test_backticks2code_3_aaae(self):
        self.assertEqual(hyper.backticks2code('a`b`c`'), 'a<code>b</code>c')
    def test_backticks2code_3_aaaa(self):
        self.assertEqual(hyper.backticks2code('a`b`c`d'), 'a<code>b</code>c<code>d</code>')

if __name__ == '__main__':
    unittest.main()