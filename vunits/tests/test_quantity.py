import os
import unittest
import math

import numpy as np

from vunits.quantity import Quantity, _force_get_quantity, _return_quantity

class TestQuantityModule(unittest.TestCase):
    def test_force_get_quantity(self):
        vel1 = Quantity(mag=10., m=1., s=-1.)
        self.assertEqual(_force_get_quantity(vel1), vel1)
        self.assertEqual(_force_get_quantity(vel1, 'm/s'), vel1)

    def test_return_quantity(self):
        vel1 = Quantity(mag=10., m=1., s=-1.)
        self.assertEqual(_return_quantity(vel1, True), vel1)
        self.assertEqual(_return_quantity(vel1, False, 'm/s'), vel1.mag)
        self.assertEqual(_return_quantity(vel1, False, 'cm/s'), vel1.mag*100.)

class TestQuantityClass(unittest.TestCase):
    def setUp(self):
        self.mag1 = 12.3456
        self.mag2 = 5.
        self.vel1 = Quantity(mag=self.mag1, m=1., s=-1.)
        self.vel2 = Quantity(mag=self.mag2, m=1., s=-1.)
        self.accel1 = Quantity(mag=10., m=1., s=-2)

    def test_neg(self):
        self.assertEqual(-self.vel1, Quantity(mag=-self.mag1, m=1., s=-1.))

    def test_abs(self):
        self.assertEqual(abs(self.vel1), Quantity(mag=self.mag1, m=1., s=-1.))

    def test_round(self):
        n = 5
        self.assertEqual(round(self.vel1, n),
                         Quantity(mag=round(self.mag1, n), m=1., s=-1.))

    def test_floor(self):
        self.assertEqual(math.floor(self.vel1),
                         Quantity(mag=math.floor(self.mag1), m=1., s=-1.))

    def test_ceil(self):
        self.assertEqual(math.ceil(self.vel1),
                         Quantity(mag=math.ceil(self.mag1), m=1., s=-1.))

    def test_trunc(self):
        self.assertEqual(math.trunc(self.vel1),
                         Quantity(mag=math.trunc(self.mag1), m=1., s=-1.))

    def test_iadd(self):
        # Set up the class to use
        mag3 = 5.
        vel3 = Quantity(mag=mag3, m=1., s=-1.)

        # Test with another Quantity object of similar units
        vel3 += self.vel1
        self.assertEqual(vel3, Quantity(mag=self.mag1+mag3, m=1., s=-1))

        # Test if error raised when using incompatible units
        with self.assertRaises(TypeError):
            vel3 += 1.
        with self.assertRaises(TypeError):
            vel3 += Quantity(mag=1., kg=1.)

    def test_isub(self):
        # Set up the class to use
        mag3 = 5.
        vel3 = Quantity(mag=mag3, m=1., s=-1.)

        # Test with another Quantity object of similar units
        vel3 -= self.vel1
        self.assertEqual(vel3, Quantity(mag=mag3-self.mag1, m=1., s=-1))

        # Test if error raised when using incompatible units
        with self.assertRaises(TypeError):
            vel3 -= 1.
        with self.assertRaises(TypeError):
            vel3 -= Quantity(mag=1., kg=1.)

    def test_imul(self):
        # Set up the class to use
        mag3 = 5.
        vel3 = Quantity(mag=mag3, m=1., s=-1.)

        # Test with another Quantity object of similar units
        vel3 *= self.vel1
        self.assertEqual(vel3, Quantity(mag=mag3*self.mag1, m=2., s=-2.))

        mag4 = 10.
        vel4 = Quantity(mag=mag4, m=1., s=-1.)
        vel4 *= 2.
        self.assertEqual(vel4, Quantity(mag=mag4*2., m=1., s=-1.))

    def test_int(self):
        self.assertEqual(int(self.vel1), int(self.mag1))

    def test_float(self):
        self.assertEqual(float(self.vel1), float(self.mag1))

    def test_str(self):
        self.assertEqual(str(self.vel1),
                         '{} m s^-1'.format(self.mag1))

    def test_add(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel1 + self.vel2
        self.assertEqual(vel3, Quantity(mag=self.mag1+self.mag2, m=1., s=-1))

        # Test if error raised when using incompatible units
        with self.assertRaises(TypeError):
            vel3 = self.vel1 + 1.
        with self.assertRaises(TypeError):
            vel3 = self.vel1 + Quantity(mag=1., kg=1.)

    def test_radd(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel2 + self.vel1
        self.assertEqual(vel3, Quantity(mag=self.mag1+self.mag2, m=1., s=-1))

        # Test if error raised when using incompatible units
        with self.assertRaises(TypeError):
            vel3 = 1. + self.vel1
        with self.assertRaises(TypeError):
            vel3 = Quantity(mag=1., kg=1.) + self.vel1

    def test_sub(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel1 - self.vel2
        self.assertEqual(vel3, Quantity(mag=self.mag1-self.mag2, m=1., s=-1))

        # Test if error raised when using incompatible units
        with self.assertRaises(TypeError):
            vel3 = self.vel1 - 1.
        with self.assertRaises(TypeError):
            vel3 = self.vel1 - Quantity(mag=1., kg=1.)

    def test_rsub(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel2 - self.vel1
        self.assertEqual(vel3, Quantity(mag=self.mag2-self.mag1, m=1., s=-1))

        # Test if error raised when using incompatible units
        with self.assertRaises(TypeError):
            vel3 = 1. - self.vel1
        with self.assertRaises(TypeError):
            vel3 = Quantity(mag=1., kg=1.) - self.vel1

    def test_mul(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel1 * self.vel2
        self.assertEqual(vel3, Quantity(mag=self.mag2*self.mag1, m=2., s=-2.))

        vel4 = self.vel1 * 2.
        self.assertEqual(vel4, Quantity(mag=self.mag1*2., m=1., s=-1.))

    def test_rmul(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel2 * self.vel1
        self.assertEqual(vel3, Quantity(mag=self.mag2*self.mag1, m=2., s=-2.))

        vel4 = 2.*self.vel1
        self.assertEqual(vel4, Quantity(mag=self.mag1*2., m=1., s=-1.))

    def test_floordiv(self):
        # Test with another Quantity object of similar units
        time1 = self.vel1 // self.accel1
        self.assertEqual(time1,
                         Quantity(mag=self.mag1 // self.accel1.mag, s=1.))

        vel3 = self.vel1 // 2.
        self.assertEqual(vel3, Quantity(mag=self.mag1 // 2., m=1., s=-1.))

    def test_rfloordiv(self):
        # Test with another Quantity object of similar units
        time1 = self.vel1 // self.accel1
        self.assertEqual(time1,
                         Quantity(mag=self.mag1 // self.accel1.mag, s=1.))

        vel3 = 2 // self.vel1
        self.assertEqual(vel3, Quantity(mag=2 // self.mag1, m=-1., s=1.))

    def test_truediv(self):
        # Test with another Quantity object of similar units
        time1 = self.vel1 / self.accel1
        self.assertEqual(time1,
                         Quantity(mag=self.mag1 / self.accel1.mag, s=1.))

        vel3 = self.vel1 / 2.
        self.assertEqual(vel3, Quantity(mag=self.mag1 / 2., m=1., s=-1.))

    def test_rtruediv(self):
        # Test with another Quantity object of similar units
        time1 = self.vel1 / self.accel1
        self.assertEqual(time1,
                         Quantity(mag=self.mag1 / self.accel1.mag, s=1.))

        inv_vel1 = 2 / self.vel1
        self.assertEqual(inv_vel1, Quantity(mag=2 / self.mag1, m=-1., s=1.))

    def test_pow(self):
        # Test with another Quantity object of similar units
        vel3 = self.vel1 ** 2
        self.assertEqual(vel3, Quantity(mag=self.mag1**2, m=2., s=-2.))

        vel4 = self.vel1 ** Quantity(2.)
        self.assertEqual(vel4, Quantity(mag=self.mag1**2., m=2., s=-2.))

        with self.assertRaises(TypeError):
            self.vel1 ** self.vel2

    def test_lt(self):
        self.assertTrue(self.vel2 < self.vel1)
        self.assertFalse(self.vel1 < self.vel2)
        with self.assertRaises(TypeError):
            self.vel2 < self.accel1            
        with self.assertRaises(TypeError):
            self.vel2 < 1.

    def test_le(self):
        self.assertTrue(self.vel2 <= self.vel1)
        self.assertTrue(self.vel2 <= self.vel2)
        self.assertFalse(self.vel1 <= self.vel2)
        with self.assertRaises(TypeError):
            self.vel2 <= self.accel1            
        with self.assertRaises(TypeError):
            self.vel2 <= 1.

    def test_eq(self):
        self.assertTrue(self.vel1 == self.vel1)
        self.assertFalse(self.vel1 == self.vel2)
        self.assertFalse(self.vel2 == self.accel1)
        self.assertFalse(self.vel2 == 1.)

    def test_ne(self):
        self.assertFalse(self.vel1 != self.vel1)
        self.assertTrue(self.vel1 != self.vel2)
        self.assertTrue(self.vel2 != self.accel1)
        self.assertTrue(self.vel2 != 1.)

    def test_gt(self):
        self.assertTrue(self.vel1 > self.vel2)
        self.assertFalse(self.vel2 > self.vel1)
        with self.assertRaises(TypeError):
            self.vel2 > self.accel1            
        with self.assertRaises(TypeError):
            self.vel2 > 1.

    def test_ge(self):
        self.assertTrue(self.vel1 >= self.vel2)
        self.assertTrue(self.vel1 >= self.vel1)
        self.assertFalse(self.vel2 >= self.vel1)
        with self.assertRaises(TypeError):
            self.vel2 > self.accel1            
        with self.assertRaises(TypeError):
            self.vel2 > 1.

    def test_is_dimless(self):
        self.assertTrue(Quantity(mag=1.)._is_dimless())
        self.assertFalse(self.vel1._is_dimless())

    def test_is_temp(self):
        self.assertTrue(Quantity(mag=1., K=1.)._is_temp())
        self.assertFalse(Quantity(mag=1., K=-1.)._is_temp())
        self.assertFalse(Quantity(mag=1., kg=1., K=1.)._is_temp())
        self.assertFalse(Quantity(mag=1.)._is_temp())
        self.assertFalse(self.vel1._is_temp())

    def test_get_other_units(self):
        self.assertTrue(self.vel2.units.equals(
                self.vel1._get_other_units(self.vel2)))
        self.assertIsNone(self.vel1._get_other_units(1))

    def test_call(self):
        self.assertAlmostEqual(self.vel1(), self.mag1)
        self.assertAlmostEqual(self.vel1('cm/s'), self.mag1*100.)
        self.assertAlmostEqual(self.vel1('cm/min'), self.mag1*100.*60.)
        with self.assertRaises(ValueError):
            self.vel1('cm3')
        
        temp = Quantity(mag=273.15, K=1.)
        self.assertEqual(temp('oC'), temp.mag-273.15)

    def test_from_units(self):
        self.assertEqual(Quantity.from_units(mag=self.mag1, units='m/s'),
                         self.vel1)
        self.assertEqual(Quantity.from_units(mag=self.mag1, units='m s-1'),
                         self.vel1)
        self.assertEqual(Quantity.from_units(mag=self.mag1, units='m s^-1'),
                         self.vel1)
        self.assertEqual(Quantity.from_units(mag=self.accel1.mag, units='m/s2'),
                         self.accel1)

    def test_from_qty(self):
        self.assertEqual(Quantity._from_qty(mag=self.mag1,
                                            units=self.vel1.units),
                         self.vel1)
                         
class TestQuantityNumpyCompatibility(unittest.TestCase):
    def test_prod(self):
        # Testing a 1D array
        mag_1d = np.array([5., 6.])
        speeds_1d = Quantity.from_units(mag=mag_1d, units='m/s')
        units_1d = speeds_1d.units
        expected_prod_1d = Quantity._from_qty(mag=np.prod(mag_1d),
                                              units=units_1d*len(mag_1d))
        self.assertEqual(expected_prod_1d, np.prod(speeds_1d))

        # Testing a 2D array
        mag_2d = np.array([[5., 6.], [7., 8.]])
        speeds_2d = Quantity.from_units(mag=mag_2d, units='m/s')
        units_2d = speeds_2d.units

        # Axis not specified
        expected_prod_2d = Quantity._from_qty(mag=np.prod(mag_2d),
                                              units=units_2d*mag_2d.size)
        self.assertEqual(expected_prod_2d, np.prod(speeds_2d))

        # Axis = 0
        axis = 0
        expected_prod_2d = Quantity._from_qty(mag=np.prod(mag_2d, axis=axis),
                                              units=units_2d*mag_2d.shape[1])
        np.testing.assert_array_equal(expected_prod_2d,
                                      np.prod(speeds_2d, axis=axis))

        # Axis = 1
        axis = 1
        expected_prod_2d = Quantity._from_qty(mag=np.prod(mag_2d, axis=axis),
                                              units=units_2d*mag_2d.shape[0])
        np.testing.assert_array_equal(expected_prod_2d,
                                      np.prod(speeds_2d, axis=axis))

    def test_sum(self):
        # Testing a 1D array
        mag_1d = np.array([5., 6.])
        speeds_1d = Quantity.from_units(mag=mag_1d, units='m/s')
        units_1d = speeds_1d.units
        expected_sum_1d = Quantity._from_qty(mag=np.sum(mag_1d),
                                              units=units_1d)
        self.assertEqual(expected_sum_1d, np.sum(speeds_1d))

        # Testing a 2D array
        mag_2d = np.array([[5., 6.], [7., 8.]])
        speeds_2d = Quantity.from_units(mag=mag_2d, units='m/s')
        units_2d = speeds_2d.units

        # Axis not specified
        expected_sum_2d = Quantity._from_qty(mag=np.sum(mag_2d),
                                              units=units_2d)
        self.assertEqual(expected_sum_2d, np.sum(speeds_2d))

        # Axis = 0
        axis = 0
        expected_sum_2d = Quantity._from_qty(mag=np.sum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_sum_2d,
                                      np.sum(speeds_2d, axis=axis))

        # Axis = 1
        axis = 1
        expected_sum_2d = Quantity._from_qty(mag=np.sum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_sum_2d,
                                      np.sum(speeds_2d, axis=axis))

    def test_nanprod(self):
        # Testing a 1D array
        mag_1d = np.array([5., 6., np.nan])
        speeds_1d = Quantity.from_units(mag=mag_1d, units='m/s')
        units_1d = speeds_1d.units
        expected_nanprod_1d = Quantity._from_qty(mag=np.nanprod(mag_1d),
                                              units=units_1d*len(mag_1d))
        self.assertEqual(expected_nanprod_1d, np.nanprod(speeds_1d))

        # Testing a 2D array
        mag_2d = np.array([[5., 6.], [7., np.nan]])
        speeds_2d = Quantity.from_units(mag=mag_2d, units='m/s')
        units_2d = speeds_2d.units

        # Axis not specified
        expected_nanprod_2d = Quantity._from_qty(mag=np.nanprod(mag_2d),
                                              units=units_2d*mag_2d.size)
        self.assertEqual(expected_nanprod_2d, np.nanprod(speeds_2d))

        # Axis = 0
        axis = 0
        expected_nanprod_2d = Quantity._from_qty(mag=np.nanprod(mag_2d, axis=axis),
                                              units=units_2d*mag_2d.shape[1])
        np.testing.assert_array_equal(expected_nanprod_2d,
                                      np.nanprod(speeds_2d, axis=axis))

        # Axis = 1
        axis = 1
        expected_nanprod_2d = Quantity._from_qty(mag=np.nanprod(mag_2d, axis=axis),
                                              units=units_2d*mag_2d.shape[0])
        np.testing.assert_array_equal(expected_nanprod_2d,
                                      np.nanprod(speeds_2d, axis=axis))

    def test_nansum(self):
        # Testing a 1D array
        mag_1d = np.array([5., 6.])
        speeds_1d = Quantity.from_units(mag=mag_1d, units='m/s')
        units_1d = speeds_1d.units
        expected_nansum_1d = Quantity._from_qty(mag=np.nansum(mag_1d),
                                              units=units_1d)
        self.assertEqual(expected_nansum_1d, np.nansum(speeds_1d))

        # Testing a 2D array
        mag_2d = np.array([[5., 6.], [7., 8.]])
        speeds_2d = Quantity.from_units(mag=mag_2d, units='m/s')
        units_2d = speeds_2d.units

        # Axis not specified
        expected_nansum_2d = Quantity._from_qty(mag=np.nansum(mag_2d),
                                              units=units_2d)
        self.assertEqual(expected_nansum_2d, np.nansum(speeds_2d))

        # Axis = 0
        axis = 0
        expected_nansum_2d = Quantity._from_qty(mag=np.nansum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_nansum_2d,
                                      np.nansum(speeds_2d, axis=axis))

        # Axis = 1
        axis = 1
        expected_nansum_2d = Quantity._from_qty(mag=np.nansum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_nansum_2d,
                                      np.nansum(speeds_2d, axis=axis))

    def test_cumsum(self):
        # Testing a 1D array
        mag_1d = np.array([5., 6.])
        speeds_1d = Quantity.from_units(mag=mag_1d, units='m/s')
        units_1d = speeds_1d.units
        expected_cumsum_1d = Quantity._from_qty(mag=np.cumsum(mag_1d),
                                                units=units_1d)
        np.testing.assert_array_equal(expected_cumsum_1d,
                                      np.cumsum(speeds_1d))

        # Testing a 2D array
        mag_2d = np.array([[5., 6.], [7., 8.]])
        speeds_2d = Quantity.from_units(mag=mag_2d, units='m/s')
        units_2d = speeds_2d.units

        # Axis not specified
        expected_cumsum_2d = Quantity._from_qty(mag=np.cumsum(mag_2d),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_cumsum_2d,
                                      np.cumsum(speeds_2d))

        # Axis = 0
        axis = 0
        expected_cumsum_2d = Quantity._from_qty(mag=np.cumsum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_cumsum_2d,
                                      np.cumsum(speeds_2d, axis=axis))

        # Axis = 1
        axis = 1
        expected_cumsum_2d = Quantity._from_qty(mag=np.cumsum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_cumsum_2d,
                                      np.cumsum(speeds_2d, axis=axis))

    def test_nancumsum(self):
        # Testing a 1D array
        mag_1d = np.array([5., np.nan])
        speeds_1d = Quantity.from_units(mag=mag_1d, units='m/s')
        units_1d = speeds_1d.units
        expected_nancumsum_1d = Quantity._from_qty(mag=np.nancumsum(mag_1d),
                                              units=units_1d)
        np.testing.assert_array_equal(expected_nancumsum_1d,
                                      np.nancumsum(speeds_1d))

        # Testing a 2D array
        mag_2d = np.array([[5., 6.], [7., np.nan]])
        speeds_2d = Quantity.from_units(mag=mag_2d, units='m/s')
        units_2d = speeds_2d.units

        # Axis not specified
        expected_nancumsum_2d = Quantity._from_qty(mag=np.nancumsum(mag_2d),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_nancumsum_2d,
                                      np.nancumsum(speeds_2d))

        # Axis = 0
        axis = 0
        expected_nancumsum_2d = Quantity._from_qty(mag=np.nancumsum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_nancumsum_2d,
                                      np.nancumsum(speeds_2d, axis=axis))

        # Axis = 1
        axis = 1
        expected_nancumsum_2d = Quantity._from_qty(mag=np.nancumsum(mag_2d, axis=axis),
                                              units=units_2d)
        np.testing.assert_array_equal(expected_nancumsum_2d,
                                      np.nancumsum(speeds_2d, axis=axis))

    def test_diff(self):
        pass

    def test_ediff1d(self):
        pass

    def test_exp(self):
        val = Quantity(1., m=1)
        exp_val = Quantity(np.exp(1.))
        self.assertEqual(np.exp(val),
                         exp_val)

    def test_expm1(self):
        pass

    def test_exp2(self):
        pass

    def test_log(self):
        pass

    def test_log10(self):
        pass

    def test_log2(self):
        pass

    def test_log1p(self):
        pass

    def test_logaddexp(self):
        pass

    def test_logaddexp2(self):
        pass

    def test_trapz(self):
        pass

    def test_i0(self):
        pass

    def test_sinc(self):
        pass

    def test_clip(self):
        pass

    def test_sqrt(self):
        pass

    def test_cbrt(self):
        pass

    def test_square(self):
        pass

    def test_absolute(self):
        pass

    def test_fabs(self):
        pass

    def test_sign(self):
        pass

    def test_heaviside(self):
        pass

    def test_maximum(self):
        pass

    def test_minimum(self):
        pass

    def test_fmax(self):
        pass

    def test_fmin(self):
        pass

    def test_nan_to_num(self):
        pass

    def test_interp(self):
        pass

    def test_mean(self):
        pass

    '''Helper functions'''
    def test_get_units_prod(self):
        pass



if __name__ == '__main__':
    unittest.main()