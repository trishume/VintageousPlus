from VintageousPlus.vi.utils import modes

from VintageousPlus.tests import set_text
from VintageousPlus.tests import add_sel
from VintageousPlus.tests import get_sel
from VintageousPlus.tests import first_sel
from VintageousPlus.tests import ViewTest


# The heavy lifting is done by units.* functions, but we refine some cases in the actual motion
# command, so we need to test for that too here.
class Test_vi_e_InNormalMode(ViewTest):
    def testMoveToEndOfWord_OnLastLine(self):
        self.write('abc\nabc\nabc')
        self.clear_sel()
        self.add_sel(self.R((2, 0), (2, 0)))

        self.view.run_command('_vi_e', {'mode': modes.NORMAL, 'count': 1})

        self.assertEqual(self.R((2, 2), (2, 2)), first_sel(self.view))

    def testMoveToEndOfWord_OnMiddleLine_WithTrailingWhitespace(self):
        self.write('abc\nabc   \nabc')
        self.clear_sel()
        self.add_sel(self.R((1, 2), (1, 2)))

        self.view.run_command('_vi_e', {'mode': modes.NORMAL, 'count': 1})

        self.assertEqual(self.R((2, 2), (2, 2)), first_sel(self.view))

    def testMoveToEndOfWord_OnLastLine_WithTrailingWhitespace(self):
        self.write('abc\nabc\nabc   ')
        self.clear_sel()
        self.add_sel(self.R((2, 0), (2, 0)))

        self.view.run_command('_vi_e', {'mode': modes.NORMAL, 'count': 1})

        self.assertEqual(self.R((2, 2), (2, 2)), first_sel(self.view))

        self.view.run_command('_vi_e', {'mode': modes.NORMAL, 'count': 1})

        self.assertEqual(self.R((2, 5), (2, 5)), first_sel(self.view))

class Test_vi_e_InVisualMode(ViewTest):
    def testMoveToEndOfWord_OnLastLine2(self):
        self.write('abc abc abc')
        self.clear_sel()
        self.add_sel(self.R(0, 2))
        self.view.run_command('_vi_e', {'mode': modes.VISUAL, 'count': 3})
        self.assertEqual(self.R((0, 0), (0, 11)), first_sel(self.view))

