"""Build a deterministic, public skill ZIP using only the Python standard library."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.agents/skills/novatelle'
TARGET = ROOT / 'downloads/novatelle-skill.zip'
FILES = ['SKILL.md', 'assets/template.html', 'references/presentation-contract.md',
         'references/qa-checklist.md', 'references/layout-options.md']

def main():
    TARGET.parent.mkdir(exist_ok=True)
    with ZipFile(TARGET, 'w', compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(FILES):
            info = ZipInfo('novatelle/' + name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (SOURCE / name).read_bytes(), compresslevel=9)
    with ZipFile(TARGET) as archive:
        assert archive.testzip() is None
        assert sorted(archive.namelist()) == sorted('novatelle/' + f for f in FILES)
    print(f'{TARGET.relative_to(ROOT)}: {TARGET.stat().st_size:,} bytes; {len(FILES)} files; ZIP verified')

if __name__ == '__main__':
    main()
