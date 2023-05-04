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
        #New to old and old to new convert
    def test_old_nic_2(self):
        self.assertEqual(NICNold.old_nic_2("199921505390"), 5390)
        self.assertEqual(NICNold.old_nic_2("199921505390"), 5390)
        
    def test_new_nic1(self):
        self.assertEqual(NICNold.new_nic1("123456789V"), 19)
        self.assertEqual(NICNold.new_nic1("987654321X"), 19)
        
    def test_new_nic2(self):
        self.assertEqual(NICNold.new_nic2("123456789V"), 12345)
        self.assertEqual(NICNold.new_nic2("987654321X"), 98765)
        
    def test_new_nic3(self):
        self.assertEqual(NICNold.new_nic3("123456789V"), 0)
        self.assertEqual(NICNold.new_nic3("987654321X"), 0)
        
    def test_new_nic4(self):
        self.assertEqual(NICNold.new_nic4("123456789V"), "6789")
        self.assertEqual(NICNold.new_nic4("987654321X"), "4321")

if __name__ == '__main__':
    unittest.main()
