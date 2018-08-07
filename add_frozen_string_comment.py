import sublime
import sublime_plugin

class RubyFileSaveListener(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    file_name = view.file_name()
    if file_name.endswith('.rb'):
      sublime.active_window().run_command("add_frozen_string_comment")

class AddFrozenStringCommentCommand(sublime_plugin.TextCommand):
  COMMENT_STRING = "# frozen_string_literal: true"

  def run(self, edit):
    file_name = self.view.file_name()

    if file_name.endswith('.rb'):
      first_line = self.view.line(0)
      line_contents = self.view.substr(first_line)
      if (line_contents != self.COMMENT_STRING):
        self.view.insert(edit, 0, self.COMMENT_STRING + "\n\n")
