#!/usr/bin/env python3
"""Split big .ics/.ical files iinto smaller ones for easy import into Google Calendar

Usage:
	icssplit INFILE [OUTFILE] [--maxsize=<bytes>]

Arguments:
	INFILE				the input .ics file
	OUTFILE				base filename for output .ics files

Options:
	--maxsize=BYTES		maximum size of outfiles [default: 900000]

Example:
	icssplit mycal.ics outcal

 	will split `mycal.ics` into outcal1.ics outcal2.ics outcal3.cs...
"""

__version__ = '1.0.1'
__author__ = 'Bjorn Stabell <bjorn@stabell.org>'
__all__ = []

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
log = logger.info

BEGIN_CALENDAR = 'BEGIN:VCALENDAR'
END_CALENDAR = 'END:VCALENDAR'
BEGIN_EVENT = 'BEGIN:VEVENT'
END_EVENT = 'END:VEVENT'
enc = {'encoding': 'utf8'} # don't rely on LANG, force encoding to UTF-8

def icssplit(src, maxsize):
	"""\
	Split .ics content in `src` into several .ics contents, each
	`maxsize` or smaller, and return them as a list of strings.
	"""
	preamble = []
	postamble = []
	events = []
	event = []
	for (line_no, line) in enumerate(src):
		if not events and not event and not line.startswith(BEGIN_EVENT):
			preamble.append(line) # store pre-amble
			continue

		if line.startswith(BEGIN_EVENT):
			assert not postamble, f"line {line_no}: {BEGIN_EVENT} after starting postamble"
			event = [line,]	# reset event content
			continue

		if line.startswith(END_EVENT):
			assert event, f"line {line_no}: no matching {BEGIN_EVENT} before {END_EVENT}"
			event.append(line)
			events.append(event)
			event = []
			continue

		if event: # in event
			event.append(line)
		else: # not in event
			postamble.append(line)

	log(f"parsed {len(events)} events")

	out_events = []
	out_len = 0
	# make room for pre- and postamble
	maxsize -= len("".join(preamble + postamble))

	for event in events:
		event = "".join(event)
		# yield a new file if we have some events and it exceeds maxsize
		# (min 1 event per file no matter what size)
		if out_events and out_len+len(event) > maxsize:
			yield "".join(preamble + out_events + postamble)
			out_events = [event,]
			out_len = len(event)
			continue
		out_events.append(event)
		out_len += len(event)
	if out_events:
		yield "".join(preamble + out_events + postamble)


def cli():
	from docopt import docopt
	args = docopt(__doc__, version=__version__)

	infile = args['INFILE']
	outfile_base = args['OUTFILE'] or infile
	maxsize = int(args['--maxsize'] or 0) or 1024*1024*0.9


	log(f"parsing {infile} and splitting into files of maxsize={maxsize}")
	for (indx, outf) in enumerate(icssplit(open(infile, 'r', **enc), maxsize)):
		outfile = f"{outfile_base}-{indx}.ics"
		log(f"writing {outfile}")
		with open(outfile, 'w', **enc) as fh:
			fh.write(outf)

if __name__ == '__main__': cli()
