import unittest
import NICNold

class TestSriLankanNICConverter(unittest.TestCase):

    def test_sl_id_to_dob_gender_M(self):
        # Valid old NIC
        dob, gender = NICNold.sl_id_to_dob_gender('861050720V')
        self.assertEqual(dob, '1986-04-14, Monday')
        self.assertEqual(gender, 'Male')
    def test_sl_id_to_dob_gender_F(self):
		# Valid old NIC Female
        dob, gender = NICNold.sl_id_to_dob_gender('866050720V')
        self.assertEqual(dob, '1986-04-14, Monday')
        self.assertEqual(gender, 'Female')
    def test_sl_id_to_dob_gender_N_M(self):
        # Valid new NIC
        dob, gender = NICNold.sl_id_to_dob_gender('200110500708')
        self.assertEqual(dob, '2001-04-14, Saturday')
        self.assertEqual(gender, 'Male')
    def test_sl_id_to_dob_gender_N_F(self):    
		# Valid new NIC Female
        dob, gender = NICNold.sl_id_to_dob_gender('200160500708')
        self.assertEqual(dob, '2001-04-14, Saturday')
        self.assertEqual(gender, 'Female')

if __name__ == '__main__':
    unittest.main()
