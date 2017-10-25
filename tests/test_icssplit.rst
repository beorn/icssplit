Read some sample .ics data:

  >>> from icssplit import icssplit
  >>> ics = open('tests/test_icssplit.ics').read()
  >>> len(ics)
  5846

We've got 18 events here:

  >>> import re; len(re.findall("BEGIN:VEVENT", ics))
  18

We'll just get one file back if we split with maxsize=1MB:

  >>> ics = ics.splitlines(True)
  >>> files = list(icssplit(ics, 1024*1024))
  >>> len(files)
  1
  >>> len(files[0])
  5846

If we use a smaller maxsize we'll get more files back:

  >>> files = list(icssplit(ics, maxsize=2500))
  >>> len(files)
  6
  >>> [ len(file) for file in files ]
  [2471, 2471, 2471, 2471, 2471, 2471]

If we set maxsize to a size smaller than even the preamble and postamble,
then what we'll get back is one event per file.  We could/should perhaps
instead return an error instead of going over the maxsize:

  >>> files = list(icssplit(ics, maxsize=1000))
  >>> len(files)
  18
