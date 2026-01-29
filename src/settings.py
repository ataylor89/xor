from pathlib import Path

project_root = Path(__file__).parent.parent

default_key_path = project_root / 'keys' / 'defaultkey.txt'
default_generated_key_path = project_root / 'keys' / 'generated-key.txt'

default_keylength = 64

default_tmin = 0
default_tmax = 255
