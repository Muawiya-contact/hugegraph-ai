import os, sys
sys.path.insert(0, 'src')
os.environ['SKIP_GREMLIN_TESTS'] = 'true'
from tests.api.test_gremlin import TestGremlin
try:
    TestGremlin.setUpClass()
    print('NO_SKIP')
except Exception as e:
    print('RAISED', type(e).__name__, str(e))
