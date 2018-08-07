import sublime, sublime_plugin

class CopyFilePathAndLineNumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file_name = self.view.file_name()
    (row,col) = self.view.rowcol(self.view.sel()[0].begin())
    s = "rspec %s:%d" % (file_name, row+1)
    sublime.set_clipboard(s)
