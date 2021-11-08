import sublime
import sublime_plugin
from .src import formatter

class PoorMansTsqlFormatter(sublime_plugin.TextCommand):
    def run(self, edit):
        all_region = sublime.Region(0, self.view.size())
        all_text = self.view.substr(all_region)
        formatted_text = formatter.format_sql(all_text)

        if not formatted_text or formatted_text == all_text:
            return

        self.view.replace(edit, all_region, formatted_text)
