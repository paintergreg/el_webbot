#!/usr/bin/env python3
#
#

import requests
chunk_size = 2048

url = 'http://www.emblibrary.com/EL/ColorChange.aspx'
payload = {}
payload['productID'] = 'm14461'
#payload = {'productID': 'm14461'}
data = {'__EVENTTARGET': 'ctl00$MainContent$productRepeater$ctl00$MakePdfProduct',
        '__EVENTARGUMENT': '',
        # '__LASTFOCUS': '',
        '__VIEWSTATE': '/wEPDwUKMTU3MjEwMTMxOQ8WEB4NdlVuaXF1ZUNvbG9yc2ceB3ZJbWFnZXNnHg12Q29sb3JTd2F0Y2hzZx4NdkNvbG9yQ2hhbmdlc2ceBWlTaXplBQJJTB4JcHJvZHVjdGlkBQZtMTQ0NjEeC1Byb2R1Y3RUeXBlBQdQcm9kdWN0Hgd2YXJpLTAwMuUDAAEAAAD/////AQAAAAAAAAAMAgAAAEdBcHBfV2ViX2d5M2FwZ3B3LCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAQBAAAAd1N5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbVmFyaWF0aW9uLCBBcHBfV2ViX2d5M2FwZ3B3LCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24EAAALVmFyaWF0aW9uW10CAAAACAgJAwAAAAEAAAABAAAABwMAAAAAAQAAAAQAAAAECVZhcmlhdGlvbgIAAAAJBAAAAA0DBQQAAAAJVmFyaWF0aW9uBwAAAAt2YXJpYXRvbl9pZA5pbWFnZV9maWxlbmFtZQ52YXJpYXRpb25fbmFtZRFyZXBlYXRlcl9sb2NhdGlvbgh0YWJsZV9pZAZhY3RpdmUIY2Nfb3JkZXIAAQEBAAAACAgBCAIAAAAAAAAABgUAAAAKTTE0NDYxLmpwZwYGAAAAB0RlZmF1bHQGBwAAAAIwMAAAAAABAQAAAAsWAmYPZBYEZg9kFgICAQ8WAh4EVGV4dAVpPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiIGxhbmd1YWdlPSJqYXZhc2NyaXB0Ij52YXIgbm93ID0gbmV3IERhdGUoMjAxNywgNiwgMjgsIDE1LCA2LCAzNik7PC9zY3JpcHQ+ZAIBD2QWBGYPZBYCAgcPDxYCHgtOYXZpZ2F0ZVVybAU3aHR0cHM6Ly93d3cuZW1ibGlicmFyeS5jb20vRUwvUHJvZmlsZS9PcmRlcmhpc3RvcnkuYXNweGRkAhQPZBYIAgEPFgIeB1Zpc2libGVoFgICAQ8PFgIfCGVkZAIDDxYCHwpoZAIFDxYCHwpoZAIHDxYCHgtfIUl0ZW1Db3VudAIBFgJmD2QWDAIBD2QWDGYPZBYEAgEPZBYCZg8VARxEZWxmdCBCbHVlIFNhZmFyaSAtIEVsZXBoYW50ZAIDD2QWAmYPFQFFPGEgaHJlZj1Qcm9kdWN0cy5hc3B4P0NhdGFsb2c9RW1ibGlicmFyeSZQcm9kdWN0SUQ9bTE0NDYxID5NMTQ0NjE8L2E+ZAIBD2QWBAIBD2QWAmYPFQElNy44Iih3KSB4IDcuMzgiKGgpICgxOTguMSB4IDE4Ny41IG1tKWQCAw9kFgJmDxUBATNkAgIPZBYEAgEPZBYCZg8VAQU0MjgzN2QCAw9kFgJmDxUBATNkAgMPZBYCAgEPZBYCZg8VAdQBVGhyZWFkIG51bWJlcnMgbGlzdGVkIGJlbG93IHJlZmVyIHRvIE1hZGVpcmEgNDAgd2VpZ2h0IHJheW9uIHRocmVhZC4mbmJzcDtVc2UgdGhlIGZyZWUgPGEgaHJlZj1NYXRjaC5hc3B4P3Byb2R1Y3RJRD1tMTQ0NjEmdmFyaUlEPTA+IFRocmVhZCBFeGNoYW5nZTwvYT4gdG8gZmluZCBlcXVpdmFsZW50cyBmcm9tIE1hZGVpcmEgdG8gb3RoZXIgYnJhbmRzIG9mIHRocmVhZC5kAgQPFgIfCmhkAgUPFgIfCmgWAmYPZBYCAgEPEA8WAh4LXyFEYXRhQm91bmRnZBAVAQdEZWZhdWx0FQEHRGVmYXVsdBQrAwFnFgFmZAIDDxYCHwpnFgICAQ8QDxYCHwxnZGRkZAIFD2QWBAIFDw8WAh4PQ29tbWFuZEFyZ3VtZW50BUU8YSBocmVmPVByb2R1Y3RzLmFzcHg/Q2F0YWxvZz1FbWJsaWJyYXJ5JlByb2R1Y3RJRD1tMTQ0NjEgPk0xNDQ2MTwvYT5kZAIHDxYCHwgFYDxhIGhyZWY9TWF0Y2guYXNweD9wcm9kdWN0SUQ9bTE0NDYxJnZhcmlJRD0wIGNsYXNzPSdidG4gYnRuLS1ibHVlIG5vLW1hcmdpbic+VGhyZWFkIEV4Y2hhbmdlPC9hPmQCBw9kFgJmDxUBwAc8dGFibGUgY2xhc3M9J2NvbG9yLXRhYmxlLW5lc3RlZCBjb250ZW50LWl0ZW0nPjx0cj48dGggY29sc3Bhbj0nMyc+PGgzPkNvbG9yIC8gVGhyZWFkIENoYW5nZXM8L2gzPjwvdGg+PC90cj48dHI+PHRkIGNsYXNzPSJoYWxmLXdpZHRoIj48dGFibGU+PHRyPjx0ZCByb3dzcGFuPSIyIj48aW1nIGF0bD0iYWx0ImlkPSJpbWd0YzM1MTM1MjE1MSIgc3JjPSJDb250cm9scy9JbWdIYW5kbGVyLmFzaHg/SW1hZ0JsYj0maGV4Q29sPTg4QkJDRiZUaElEPTExMzImVHlJRD0xIiAvPjwvdGQ+PHRkPkNDMTo8L3RkPjx0ZD5DbGVhciBCbHVlICMxMTMyPC90ZD48L3RyPjx0cj48dGQ+Jm5ic3A7PC90ZD4gPHRkPnNoYWRpbmcmbmJzcDs8L3RkPjwvdHI+PC90YWJsZT48L3RkPjx0ZCBjbGFzcz0iaGFsZi13aWR0aCI+PHRhYmxlPjx0cj48dGQgcm93c3Bhbj0iMiI+PGltZyBhdGw9ImFsdCJpZD0iaW1ndGMzNTEzNTIxNTMiIHNyYz0iQ29udHJvbHMvSW1nSGFuZGxlci5hc2h4P0ltYWdCbGI9JmhleENvbD0wMDZEQTcmVGhJRD0xMTc3JlR5SUQ9MSIgLz48L3RkPjx0ZD5DQzM6PC90ZD48dGQ+Qmx1ZSBCaXJkICMxMTc3PC90ZD48L3RyPjx0cj48dGQ+Jm5ic3A7PC90ZD4gPHRkPnNoYWRpbmcsIG91dGxpbmVzLCBkZXRhaWwmbmJzcDs8L3RkPjwvdHI+PC90YWJsZT48L3RkPjwvdHI+PHRyPjx0ZCBjbGFzcz0iaGFsZi13aWR0aCI+PHRhYmxlPjx0cj48dGQgcm93c3Bhbj0iMiI+PGltZyBhdGw9ImFsdCJpZD0iaW1ndGMzNTEzNTIxNTIiIHNyYz0iQ29udHJvbHMvSW1nSGFuZGxlci5hc2h4P0ltYWdCbGI9JmhleENvbD01OTlBQjUmVGhJRD0xMzczJlR5SUQ9MSIgLz48L3RkPjx0ZD5DQzI6PC90ZD48dGQ+Q2VydWxlYW4gRnJvc3QgIzEzNzM8L3RkPjwvdHI+PHRyPjx0ZD4mbmJzcDs8L3RkPiA8dGQ+c2hhZGluZywgb3V0bGluZXMmbmJzcDs8L3RkPjwvdHI+PC90YWJsZT48L3RkPjwvdHI+PC90YWJsZT5kAgkPZBYCZg8VAc8EPHRhYmxlIGNsYXNzPSdjb2xvci10YWJsZSBjb250ZW50LWl0ZW0nPjx0cj48dGggY29sc3Bhbj0nMyc+PGgzPlVuaXF1ZSBDb2xvcnMgVXNlZDwvaDM+PC90aD48L3RyPjx0cj48dGQgY2xhc3M9ImhhbGYtd2lkdGgiPjxpbWcgaWQ9ImltZ3RjMzUxMzUyMTUxIiBzcmM9IkNvbnRyb2xzL0ltZ0hhbmRsZXIuYXNoeD9JbWFnQmxiPSZoZXhDb2w9ODhCQkNGJlRoSUQ9MTEzMiZUeUlEPTEiIC8+Jm5ic3A7Jm5ic3A7Q2xlYXIgQmx1ZSAgIzExMzI8L3RkPjx0ZCBjbGFzcz0iaGFsZi13aWR0aCI+PGltZyBpZD0iaW1ndGMzNTEzNTIxNTMiIHNyYz0iQ29udHJvbHMvSW1nSGFuZGxlci5hc2h4P0ltYWdCbGI9JmhleENvbD0wMDZEQTcmVGhJRD0xMTc3JlR5SUQ9MSIgLz4mbmJzcDsmbmJzcDtCbHVlIEJpcmQgICMxMTc3PC90ZD48L3RyPjx0cj48dGQgY2xhc3M9ImhhbGYtd2lkdGgiPjxpbWcgaWQ9ImltZ3RjMzUxMzUyMTUyIiBzcmM9IkNvbnRyb2xzL0ltZ0hhbmRsZXIuYXNoeD9JbWFnQmxiPSZoZXhDb2w9NTk5QUI1JlRoSUQ9MTM3MyZUeUlEPTEiIC8+Jm5ic3A7Jm5ic3A7Q2VydWxlYW4gRnJvc3QgICMxMzczPC90ZD48L3RyPjwvdGFibGU+ZAILD2QWAgIBDw8WAh4ISW1hZ2VVcmwFGXByb2R1Y3RfaW1hZ2VzXE0xNDQ2MS5qcGdkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBgU6Y3RsMDAkTWFpbkNvbnRlbnQkcHJvZHVjdFJlcGVhdGVyJGN0bDAwJFNob3dNZUNoZWNrQm94ZXMkMAU6Y3RsMDAkTWFpbkNvbnRlbnQkcHJvZHVjdFJlcGVhdGVyJGN0bDAwJFNob3dNZUNoZWNrQm94ZXMkMQU6Y3RsMDAkTWFpbkNvbnRlbnQkcHJvZHVjdFJlcGVhdGVyJGN0bDAwJFNob3dNZUNoZWNrQm94ZXMkMgU6Y3RsMDAkTWFpbkNvbnRlbnQkcHJvZHVjdFJlcGVhdGVyJGN0bDAwJFNob3dNZUNoZWNrQm94ZXMkMwU6Y3RsMDAkTWFpbkNvbnRlbnQkcHJvZHVjdFJlcGVhdGVyJGN0bDAwJFNob3dNZUNoZWNrQm94ZXMkNAU6Y3RsMDAkTWFpbkNvbnRlbnQkcHJvZHVjdFJlcGVhdGVyJGN0bDAwJFNob3dNZUNoZWNrQm94ZXMkNFwCdmOPi6EMgByMUDV+4XdkkqmD3UnbnS05x6Rl/dEY',
        #'__VIEWSTATEGENERATOR': '0569BC85',
        #'__SCROLLPOSITIONX': '0',
        #'__SCROLLPOSITIONY': '0',
        #'ctl00$SearchTextBox': '',
        #'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$0': 'on',
        #'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$1': 'on',
        #'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$2': 'on',
        #'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$3': 'on',
        }

r = requests.post(url, params=payload, data=data)
print(r.url)

with open('./AAATemp/metadata.pdf', 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
