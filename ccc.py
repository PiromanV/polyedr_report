class TestModPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """40.0	45.0	-30.0	-60.0
8	2	8
0.0 0.0 0.0
5.0 0.0 0.0
5.0 5.0 0.0
0.0 5.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
6.0 6.0 3.0
1.0 6.0 3.0
4	1    2    3    4
4	5    6    7    8
"""
        fake_file_path = 'data/holey_ccc.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_length(self):
        from common.tk_drawer import TkDrawer
        tk = TkDrawer()
        self.polyedr.draw(tk)
        self.assertAlmostEqual(self.polyedr.length, 15.0)