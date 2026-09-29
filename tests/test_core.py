import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_mine(self):
        state = core.new_game()
        self.assertTrue(core.mine(state, "V1"))
        self.assertFalse(core.mine(state, "V1"))

    def test_02_mine_capacity(self):
        state = core.new_game()
        core.work(state, "V1")
        core.work(state, "V2")
        result = core.work(state, "V3")
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, "V1", 3), 2)

    def test_04_cancel_refunds_explosive(self):
        state = core.new_game()
        state["explosive"] = 40
        core.cancel(state, "V1")
        self.assertEqual(state["explosive"], 50)

    def test_05_no_produce_on_fault(self):
        state = core.new_game()
        state["vent_fault"] = True
        result = core.produce(state, 5)
        self.assertFalse(result)

    def test_06_collapse_once(self):
        state = core.new_game()
        core.collapse(state)
        self.assertEqual(state["safety"], 90)

    def test_07_no_work_without_support(self):
        state = core.new_game()
        state["supported"] = False
        result = core.support(state, "V1")
        self.assertFalse(result)

    def test_08_load_preserves_shift(self):
        state = core.new_game()
        state["shift_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["shift_id"], 4)


if __name__ == "__main__":
    unittest.main()
