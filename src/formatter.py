import sublime
from subprocess import Popen, PIPE
from . import preferences, pathutil

def _get_node_path():
    node = pathutil.find_executable(preferences.get_path(), 'node')
    if not node:
        raise Exception('Could not find Node.js. Check that your configuration is correct.')
    return node


def _get_sql_formatter_path():
    node = pathutil.find_executable(preferences.get_path(), 'sqlformat')
    if not node:
        raise Exception('Could not find sqlformat command. Check that `poor-mans-t-sql-formatter-npm-cli` is installed and your configuration is correct.')
    return node


def _put_option(cmd, name, is_bool=False):
    if preferences.get_pref(name):
        if is_bool and preferences.get_pref(name):
            cmd.extend(['--'+name])
        else:
            cmd.extend(['--'+name, str(preferences.get_pref(name))])

def format_sql(sql):
    cmd = None
    if sublime.platform() == 'windows':
        cmd = [_get_sql_formatter_path()]
    else:
        cmd = [_get_node_path(), _get_sql_formatter_path()]

    for opt in [
        'indent', 
        'maxLineWidth',
        'spacesPerTab',
        'statementBreaks',
        'clauseBreaks',
        'inputEncoding',
        'outputEncoding'
        ]:
        _put_option(cmd, opt)

    for bool_opt in [
        'no-expandCommaLists',     
        'no-trailingCommas',
        'spaceAfterExpandedComma',
        'no-expandBooleanExpressions',
        'no-expandCaseStatements',
        'no-expandBetweenConditions',
        'expandInLists',
        'breakJoinOnSections',
        'no-uppercaseKeywords',
        'keywordStandardization',
        'randomizeKeywordCase',
        'randomizeLineLengths',
        'no-preserveComments',
        'enableKeywordSubstitution',
        'forceOutputBOM'
        ]:
        _put_option(cmd, bool_opt, True)

    print(cmd)

    return Popen(cmd, stdin=PIPE, stdout=PIPE, shell=(sublime.platform() == 'windows')) \
        .communicate(sql.encode('utf-8'))[0] \
        .decode('utf-8')
