import datetime as dt

class ProgressReport(object):
    """Report on number of seconds elapsed between initiation 
    and call of method report.
    """
    def __init__(self):
        """Initiate timer and set start time.
        """
        self.start = dt.datetime.now()

    def report(self):
        """Call timer to report on time elapsed since start time.
        Return time elapsed as number of seconds and print string to console.
        """
        d = round((dt.datetime.now() - self.start).total_seconds(), 0)
        self.elapsed = "Time elapsed: %d seconds" %(d)

        print self.elapsed
        return d