#!/usr/bin/env python3
#
#

import requests
import time
import sys

defaultURL = "https://www.emblibrary.com/EL/New.aspx"
def downloadPDF():
    chunk_size = 2048

    url = 'https://www.emblibrary.com/EL/ColorChange.aspx'
    payload = {}
    payload['productID'] = 'm14461'
    #payload = {'productID': 'm14461'}

    data = {'__EVENTTARGET': 'ctl00$MainContent$productRepeater$ctl00$MakePdfProduct',
            # '__EVENTARGUMENT': '',
            # '__LASTFOCUS': '',
            '__VIEWSTATE': '/wEPDwUKMTU3MjEwMTMxOQ8WEB4NdlVuaXF1ZUNvbG9yc2ceB3ZJbWFnZXNnHg12Q29sb3JTd2F0Y2hzZx4NdkNvbG9yQ2hhbmdlc2ceBWlTaXplBQJJTB4JcHJvZHVjdGlkBQZtMTQ0NjEeC1Byb2R1Y3RUeXBlBQdQcm9kdWN0Hgd2YXJpLTAwMuUDAAEAAAD/////AQAAAAAAAAAMAgAAAEdBcHBfV2ViXzRoaHEwbGtwLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAQBAAAAd1N5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbVmFyaWF0aW9uLCBBcHBfV2ViXzRoaHEwbGtwLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24EAAALVmFyaWF0aW9uW10CAAAACAgJAwAAAAEAAAABAAAABwMAAAAAAQAAAAQAAAAECVZhcmlhdGlvbgIAAAAJBAAAAA0DBQQAAAAJVmFyaWF0aW9uBwAAAAt2YXJpYXRvbl9pZA5pbWFnZV9maWxlbmFtZQ52YXJpYXRpb25fbmFtZRFyZXBlYXRlcl9sb2NhdGlvbgh0YWJsZV9pZAZhY3RpdmUIY2Nfb3JkZXIAAQEBAAAACAgBCAIAAAAAAAAABgUAAAAKTTE0NDYxLmpwZwYGAAAAB0RlZmF1bHQGBwAAAAIwMAAAAAABAQAAAAsWAmYPZBYEZg9kFgICAQ8WAh4EVGV4dAVoPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiIGxhbmd1YWdlPSJqYXZhc2NyaXB0Ij52YXIgbm93ID0gbmV3IERhdGUoMjAxNywgNywgMywgMTgsIDgsIDMzKTs8L3NjcmlwdD5kAgEPZBYEZg9kFgICBw8PFgIeC05hdmlnYXRlVXJsBTdodHRwczovL3d3dy5lbWJsaWJyYXJ5LmNvbS9FTC9Qcm9maWxlL09yZGVyaGlzdG9yeS5hc3B4ZGQCFA9kFggCAQ8WAh4HVmlzaWJsZWgWAgIBDw8WAh8IZWRkAgMPFgIfCmhkAgUPFgIfCmhkAgcPFgIeC18hSXRlbUNvdW50AgEWAmYPZBYMAgEPZBYMZg9kFgQCAQ9kFgJmDxUBHERlbGZ0IEJsdWUgU2FmYXJpIC0gRWxlcGhhbnRkAgMPZBYCZg8VAUU8YSBocmVmPVByb2R1Y3RzLmFzcHg/Q2F0YWxvZz1FbWJsaWJyYXJ5JlByb2R1Y3RJRD1tMTQ0NjEgPk0xNDQ2MTwvYT5kAgEPZBYEAgEPZBYCZg8VASU3LjgiKHcpIHggNy4zOCIoaCkgKDE5OC4xIHggMTg3LjUgbW0pZAIDD2QWAmYPFQEBM2QCAg9kFgQCAQ9kFgJmDxUBBTQyODM3ZAIDD2QWAmYPFQEBM2QCAw9kFgICAQ9kFgJmDxUB1AFUaHJlYWQgbnVtYmVycyBsaXN0ZWQgYmVsb3cgcmVmZXIgdG8gTWFkZWlyYSA0MCB3ZWlnaHQgcmF5b24gdGhyZWFkLiZuYnNwO1VzZSB0aGUgZnJlZSA8YSBocmVmPU1hdGNoLmFzcHg/cHJvZHVjdElEPW0xNDQ2MSZ2YXJpSUQ9MD4gVGhyZWFkIEV4Y2hhbmdlPC9hPiB0byBmaW5kIGVxdWl2YWxlbnRzIGZyb20gTWFkZWlyYSB0byBvdGhlciBicmFuZHMgb2YgdGhyZWFkLmQCBA8WAh8KaGQCBQ8WAh8KaBYCZg9kFgICAQ8QDxYCHgtfIURhdGFCb3VuZGdkEBUBB0RlZmF1bHQVAQdEZWZhdWx0FCsDAWcWAWZkAgMPFgIfCmcWAgIBDxAPFgIfDGdkZGRkAgUPZBYEAgUPDxYCHg9Db21tYW5kQXJndW1lbnQFRTxhIGhyZWY9UHJvZHVjdHMuYXNweD9DYXRhbG9nPUVtYmxpYnJhcnkmUHJvZHVjdElEPW0xNDQ2MSA+TTE0NDYxPC9hPmRkAgcPFgIfCAVgPGEgaHJlZj1NYXRjaC5hc3B4P3Byb2R1Y3RJRD1tMTQ0NjEmdmFyaUlEPTAgY2xhc3M9J2J0biBidG4tLWJsdWUgbm8tbWFyZ2luJz5UaHJlYWQgRXhjaGFuZ2U8L2E+ZAIHD2QWAmYPFQHABzx0YWJsZSBjbGFzcz0nY29sb3ItdGFibGUtbmVzdGVkIGNvbnRlbnQtaXRlbSc+PHRyPjx0aCBjb2xzcGFuPSczJz48aDM+Q29sb3IgLyBUaHJlYWQgQ2hhbmdlczwvaDM+PC90aD48L3RyPjx0cj48dGQgY2xhc3M9ImhhbGYtd2lkdGgiPjx0YWJsZT48dHI+PHRkIHJvd3NwYW49IjIiPjxpbWcgYXRsPSJhbHQiaWQ9ImltZ3RjMzUxMzUyMTUxIiBzcmM9IkNvbnRyb2xzL0ltZ0hhbmRsZXIuYXNoeD9JbWFnQmxiPSZoZXhDb2w9ODhCQkNGJlRoSUQ9MTEzMiZUeUlEPTEiIC8+PC90ZD48dGQ+Q0MxOjwvdGQ+PHRkPkNsZWFyIEJsdWUgIzExMzI8L3RkPjwvdHI+PHRyPjx0ZD4mbmJzcDs8L3RkPiA8dGQ+c2hhZGluZyZuYnNwOzwvdGQ+PC90cj48L3RhYmxlPjwvdGQ+PHRkIGNsYXNzPSJoYWxmLXdpZHRoIj48dGFibGU+PHRyPjx0ZCByb3dzcGFuPSIyIj48aW1nIGF0bD0iYWx0ImlkPSJpbWd0YzM1MTM1MjE1MyIgc3JjPSJDb250cm9scy9JbWdIYW5kbGVyLmFzaHg/SW1hZ0JsYj0maGV4Q29sPTAwNkRBNyZUaElEPTExNzcmVHlJRD0xIiAvPjwvdGQ+PHRkPkNDMzo8L3RkPjx0ZD5CbHVlIEJpcmQgIzExNzc8L3RkPjwvdHI+PHRyPjx0ZD4mbmJzcDs8L3RkPiA8dGQ+c2hhZGluZywgb3V0bGluZXMsIGRldGFpbCZuYnNwOzwvdGQ+PC90cj48L3RhYmxlPjwvdGQ+PC90cj48dHI+PHRkIGNsYXNzPSJoYWxmLXdpZHRoIj48dGFibGU+PHRyPjx0ZCByb3dzcGFuPSIyIj48aW1nIGF0bD0iYWx0ImlkPSJpbWd0YzM1MTM1MjE1MiIgc3JjPSJDb250cm9scy9JbWdIYW5kbGVyLmFzaHg/SW1hZ0JsYj0maGV4Q29sPTU5OUFCNSZUaElEPTEzNzMmVHlJRD0xIiAvPjwvdGQ+PHRkPkNDMjo8L3RkPjx0ZD5DZXJ1bGVhbiBGcm9zdCAjMTM3MzwvdGQ+PC90cj48dHI+PHRkPiZuYnNwOzwvdGQ+IDx0ZD5zaGFkaW5nLCBvdXRsaW5lcyZuYnNwOzwvdGQ+PC90cj48L3RhYmxlPjwvdGQ+PC90cj48L3RhYmxlPmQCCQ9kFgJmDxUBzwQ8dGFibGUgY2xhc3M9J2NvbG9yLXRhYmxlIGNvbnRlbnQtaXRlbSc+PHRyPjx0aCBjb2xzcGFuPSczJz48aDM+VW5pcXVlIENvbG9ycyBVc2VkPC9oMz48L3RoPjwvdHI+PHRyPjx0ZCBjbGFzcz0iaGFsZi13aWR0aCI+PGltZyBpZD0iaW1ndGMzNTEzNTIxNTEiIHNyYz0iQ29udHJvbHMvSW1nSGFuZGxlci5hc2h4P0ltYWdCbGI9JmhleENvbD04OEJCQ0YmVGhJRD0xMTMyJlR5SUQ9MSIgLz4mbmJzcDsmbmJzcDtDbGVhciBCbHVlICAjMTEzMjwvdGQ+PHRkIGNsYXNzPSJoYWxmLXdpZHRoIj48aW1nIGlkPSJpbWd0YzM1MTM1MjE1MyIgc3JjPSJDb250cm9scy9JbWdIYW5kbGVyLmFzaHg/SW1hZ0JsYj0maGV4Q29sPTAwNkRBNyZUaElEPTExNzcmVHlJRD0xIiAvPiZuYnNwOyZuYnNwO0JsdWUgQmlyZCAgIzExNzc8L3RkPjwvdHI+PHRyPjx0ZCBjbGFzcz0iaGFsZi13aWR0aCI+PGltZyBpZD0iaW1ndGMzNTEzNTIxNTIiIHNyYz0iQ29udHJvbHMvSW1nSGFuZGxlci5hc2h4P0ltYWdCbGI9JmhleENvbD01OTlBQjUmVGhJRD0xMzczJlR5SUQ9MSIgLz4mbmJzcDsmbmJzcDtDZXJ1bGVhbiBGcm9zdCAgIzEzNzM8L3RkPjwvdHI+PC90YWJsZT5kAgsPZBYCAgEPDxYCHghJbWFnZVVybAUZcHJvZHVjdF9pbWFnZXNcTTE0NDYxLmpwZ2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYGBTpjdGwwMCRNYWluQ29udGVudCRwcm9kdWN0UmVwZWF0ZXIkY3RsMDAkU2hvd01lQ2hlY2tCb3hlcyQwBTpjdGwwMCRNYWluQ29udGVudCRwcm9kdWN0UmVwZWF0ZXIkY3RsMDAkU2hvd01lQ2hlY2tCb3hlcyQxBTpjdGwwMCRNYWluQ29udGVudCRwcm9kdWN0UmVwZWF0ZXIkY3RsMDAkU2hvd01lQ2hlY2tCb3hlcyQyBTpjdGwwMCRNYWluQ29udGVudCRwcm9kdWN0UmVwZWF0ZXIkY3RsMDAkU2hvd01lQ2hlY2tCb3hlcyQzBTpjdGwwMCRNYWluQ29udGVudCRwcm9kdWN0UmVwZWF0ZXIkY3RsMDAkU2hvd01lQ2hlY2tCb3hlcyQ0BTpjdGwwMCRNYWluQ29udGVudCRwcm9kdWN0UmVwZWF0ZXIkY3RsMDAkU2hvd01lQ2hlY2tCb3hlcyQ01TkqDcZ8t1L2t2dVYasvm1hjDMz3zZedGjfGe1BDZ7I=',
            # '__VIEWSTATEGENERATOR': '0569BC85',
            # '__SCROLLPOSITIONX': '0',
            # '__SCROLLPOSITIONY': '342',
            # 'ctl00$SearchTextBox': '',
            # 'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$0': 'on',
            # 'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$1': 'on',
            # 'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$2': 'on',
            # 'ctl00$MainContent$productRepeater$ctl00$ShowMeCheckBoxes$3': 'on'
            }

    r = requests.post(url, params=payload, data=data)
    print(r.url)

    with open('./AAATemp/metadata.pdf', 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)

def printTest():
    a = "M12345"
    b = "Now is the time"
    print(a, b, sep="-")
    i = 0
    while i < 75:
        i += 1
        print('#', end='', flush=True)
        time.sleep(.5)
    print("")

# http://www.emblibrary.com/EL/new.aspx?date=040517
# http://www.emblibrary.com/EL/New.aspx
def keyBoardInput():
    url = defaultURL
    print(sys.platform)
    i = input("Enter MMDDYY or Return: ")
    if i != "":
        url += "?date=" + i
    return(url)

if __name__ == "__main__":
    # printTest()
    url = keyBoardInput()
    print(url)
